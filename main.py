from openai import OpenAI
import os
from dotenv import load_dotenv
from rich import print
import streamlit as st

st.title("ChatGPT-like clone")
# Load environment variables from .env file
load_dotenv()

# Access the secret
secret_key = os.getenv("GITHUB_TOKEN2")

# Sukuriame OpenAI klientą
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=secret_key
)

# Tikriname, ar jau yra išsaugota žinučių istorija (jei ne – sukuriame)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Tu esi naudingas asistentas ir visada atsakai tik lietuvių kalba."}
    ]

# **Failo įkėlimo funkcija**
uploaded_file = st.file_uploader("Įkelkite failą", type=["txt", "pdf"])

if uploaded_file is not None:
    st.success(f"Failas {uploaded_file.name} sėkmingai įkeltas.")

# **Pokalbio istorijos rodymas**
for message in st.session_state.messages:
    # Neparodyti sistemos pranešimo
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# **Vartotojo įvesties laukelis**
if prompt := st.chat_input("Klausk bet ko..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
