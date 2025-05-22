from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from celery_app import celery

app = FastAPI()

class UserSignup(BaseModel):
    email: EmailStr
    name: str

@app.post("/signup")
async def signup(user: UserSignup):
    celery.send_task("worker.tasks.send_email", args=[user.email, user.name])
    return {"message": "User registered. Email queued."}
