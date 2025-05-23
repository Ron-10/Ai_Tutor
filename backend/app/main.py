from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import lessons

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lessons.router)

@app.get("/")
def root():
    return {"message": "I-Tutor360 Backend is running"}
