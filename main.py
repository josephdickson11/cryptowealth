from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get("/")
def welcome_boldd():
    return {"msg":"BOLDD WAY"}