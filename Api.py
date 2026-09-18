#para acessar a api, utilize o seguinte comando no terminal: uvicorn Api:app --reload
#como foi uma api criada por mim, ela esta localizada no arquivo Api.py, e para acessar a api, utilize comando do terminal
from fastapi import FastAPI

app = FastAPI()


MATERIAS = {
    "matematica": {
        "nome": "Matemática",
        "area": "Exatas",
        "descricao": "Números, álgebra, geometria e estatística.",
    },
    "portugues": {
        "nome": "Português",
        "area": "Linguagens",
        "descricao": "Gramática, literatura, leitura e produção de texto.",
    },
    "historia": {
        "nome": "História",
        "area": "Humanas",
        "descricao": "Estudo dos acontecimentos e das sociedades ao longo do tempo.",
    },
    "geografia": {
        "nome": "Geografia",
        "area": "Humanas",
        "descricao": "Espaço geográfico, sociedade, natureza e território.",
    },
    "biologia": {
        "nome": "Biologia",
        "area": "Ciências da Natureza",
        "descricao": "Estudo dos seres vivos e dos processos da vida.",
    },
    "fisica": {
        "nome": "Física",
        "area": "Ciências da Natureza",
        "descricao": "Matéria, energia, movimento e fenômenos naturais.",
    },
    "quimica": {
        "nome": "Química",
        "area": "Ciências da Natureza",
        "descricao": "Composição, propriedades e transformações da matéria.",
    },
    "ingles": {
        "nome": "Inglês",
        "area": "Linguagens",
        "descricao": "Vocabulário, gramática, leitura e comunicação em inglês.",
    },
}


@app.get("/")
def read_root():
    return MATERIAS