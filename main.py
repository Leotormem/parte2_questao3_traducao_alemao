
import logging

import torch
from fastapi import FastAPI, HTTPException
from langchain_core.runnables import RunnableLambda
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from models import TranslationRequest, TranslationResponse


app = FastAPI(
    title="TP2 - Parte 2 - Questao 3 - Hugging Face",
    description="Traducao de ingles para alemao com FastAPI e LangChain",
    version="1.0.0"
)

MODEL_NAME = "Helsinki-NLP/opus-mt-en-de"

# Carregamento do modelo uma unica vez
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.eval()


# Funcao que executa a traducao
def translate_with_huggingface(text: str) -> str:

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=512
        )

    translated_text = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return translated_text


# Integracao da funcao com o LangChain
translation_chain = RunnableLambda(
    translate_with_huggingface
)


@app.post("/translate", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):

    try:
        translated_text = translation_chain.invoke(
            request.text
        )

        return TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            source_language="English",
            target_language="German"
        )

    except Exception:
        logging.exception("Erro durante a traducao")

        raise HTTPException(
            status_code=500,
            detail="Nao foi possivel traduzir o texto."
        )
