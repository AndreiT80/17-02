# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами." module_17_2

from fastapi import FastAPI
from app.models import user, task

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)

# загрузка    uvicorn main:app --reload
