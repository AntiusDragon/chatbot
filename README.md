![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
![Gluten Status](https://img.shields.io/badge/Gluten-Free-green.svg)
![Eco Status](https://img.shields.io/badge/ECO-Friendly-green.svg)

# ChatBot

_website design project_

<br>

## 🌟 About

This project is for educational porpuses only. Pull request are welcome, but priority for project authors! Thank you for your cooperation!

Site published at: https://antiusdragon.github.io/paskaita-gen-ai/

## 🎯 Project features/goals

-   Github pages
-   [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
-   desktop only

## 🧰 Getting Started

### 💻 Prerequisites

Python.org - _download and install_

```
https://www.python.org/
```

Git - _download and install_

```
https://git-scm.com
```

### 🏃 Run locally

Would like to run this project locally? Open terminal and follow these steps:

1. Clone the repo
    ```sh
    git clone https://github.com/AntiusDragon/paskaita-gen-ai.git
    ```
2. Install all packages
    ```sh
    uv sync
    ```
3. Run
    ```sh
    .venv\Scripts\activate
    ```
4. Run file main.py or main2.py
    ```sh
    streamlit run main.py
    ```

### 🧪 Running tests

There is no tests for this project.

## 🎅 Authors

Antanas: [Github](https://github.com/AntiusDragon)

## ⚠️ License

Distributed under the MIT License. See LICENSE.txt for more information.

## 🔗 Other resources

No other resouces.

# Komandos sukuriant nauja projekta:
## sukuria pradinius failus
```sh
uv init
```
## sukuriam ".gitignore"
## venv dažniausiai naudojamas duomenu biblioteka
```sh
uv venv
```
## turim aktivuoti venv su komanda
```sh
.venv\Scripts\activate
```
## tada tesem terminalo kodus
```sh
uv add openai
```
## naudojam ši komanda kad suprastu ".evn" faila
```sh
uv add python-dotenv
```
## Pastaba turi buti trumpas GIT_KEY raktas
```sh
turi veikti
```
## pridedam dar "rich"
```sh
uv add rich
```
```sh
uv add streamlit
```
```sh
streamlit run main.py
```



## naudojam test koda
```sh
python main.py
```
## rei norim pašalinti openai
```sh
uv remove openai
```
## jei nera aplankalo ".venv" tada insrašom ši komanda kad inrašitu priedus
```sh
uv sync
```
## kai inrašo priedus turim ji pajungti su šio kodu
```sh
.venv\Scripts\activate
```
