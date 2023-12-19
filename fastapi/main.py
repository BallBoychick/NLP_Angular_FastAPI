from fastapi import FastAPI
from transformers import MarianMTModel, MarianTokenizer
from transformers import pipeline

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf


# app = FastAPI()

# @app.get("/translate")
# def translate_text(text: str):
#     pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")
#     pred = pipe(text)
#     return {"translation": pred}