from fastapi import FastAPI
from routes import audio

app = FastAPI()
app.include_router(audio.router)
