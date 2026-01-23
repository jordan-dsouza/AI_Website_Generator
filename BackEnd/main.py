from fastapi import FastAPI
from pydantic import BaseModel  # For data validation
from llm import generate_spec
from templates import generate_css, generate_html
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def root():
    return {"status": "AI Website Generator backend running"}


class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_site(req: PromptRequest):
    print("Received prompt:", req.prompt)
    spec = generate_spec(req.prompt)
    html = generate_html(spec)
    css = generate_css(spec.get("theme", "light"))

    return {
        "spec": spec,
        "html": html,
        "css": css
    }
