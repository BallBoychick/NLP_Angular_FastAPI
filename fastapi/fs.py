from fastapi import FastAPI
import requests
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class Sentence(BaseModel):
    sentence: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipe = pipeline("translation", model="opus-mt-en-ru")

glob = "asd"

@app.post("/fr")
async def send_sentence(sentence: Sentence):
    # Ваш код обработки запроса здесь
    pipe = pipeline("translation", model="opus-mt-en-ru")
    pred = pipe(sentence.sentence)
    return pred[0]["translation_text"]

# @app.get("/translate")
# def translate_text():
#     globs = glob.upper()
#     return globs

# abc = send_sentence()
# @app.get("/fr")
# async def tr():
#     ass 
#     return ass


# @app.get("/fr")
# async def send_sentence(sentence: Sentence):
#     pipe = pipeline("translation", model="opus-mt-en-ru")
#     pred = pipe(sentence)
#     url = 'http://localhost:4200'
#     response = requests.post(url, json={"sentence": pred})
#     return {"message": "Предложение успешно обработано"}

# @app.get("/translate")
# def translate_text():
#     pipe = pipeline("translation", model="opus-mt-en-ru")
#     pred = pipe()
#     return pred[0]["translation_text"]
