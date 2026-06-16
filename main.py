from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str 
    description: str | None = None
    done: bool = False

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, Mundo! Minha primeira rota com FastAPI funciona."}

@app.post("/tasks/")
async def create_task(task: Task):
    return task