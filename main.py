from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str 
    description: str | None = None
    done: bool = False

app = FastAPI()
banco_de_dados = []

@app.get("/tasks/")
def read_task():
    return banco_de_dados

@app.get("/tasks/{task_id}")
def read_task_item(task_id: int):
    
    for task in banco_de_dados:
        if task.id == task_id:
            return task
    return ["nao encontrado"]
    
    

@app.post("/tasks/")
async def create_task(task: Task):
    banco_de_dados.append(task)
    return task