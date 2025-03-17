mkdir stremlit-demo

// sukuria pradinius failus
uv init

// sukuriam ".gitignore"

// venv dažniausiai naudojamas duomenu biblioteka
uv venv

// turim aktivuoti venv su komanda
.venv\Scripts\activate

// tada tesem terminalo kodus
uv add openai

// naudojam ši komanda kad suprastu ".evn" faila
uv add python-dotenv

uv add rich
uv add streamlit
streamlit run main.py



// rei norim pašalinti openai
uv remove openai
// jei nera aplankalo ".venv" tada insrašom ši komanda kad inrašitu priedus
uv sync
//kai inrašo priedus turim ji pajungti su šio kodu
.venv\Scripts\activate