from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..translation.translator import translate_text

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("translate.html", {"request": request})

@app.post("/translate/")
async def translate(source_text: str = Form(...), target_language: str = Form(...)):
    translated_text = translate_text(source_text, target_language)
    return {"translated_text": translated_text}