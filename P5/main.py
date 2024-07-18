from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import nltk
import os

nltk.download('punkt')

app = FastAPI()

genai.configure(api_key=os.environ["API_KEY"])

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Summarize the following text in less than 100 words: {request.text}")
        summary = response.text
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/token_count")
async def count_tokens(request: TextRequest):
    try:
        tokens = nltk.word_tokenize(request.text)
        return {"token_count": len(tokens)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))