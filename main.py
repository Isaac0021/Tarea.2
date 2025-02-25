from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Lista para almacenar usuarios (podrías usar una base de datos si lo prefieres)
users = []

# Modelo para la información del usuario
class User(BaseModel):
    name: str
    email: str

# Endpoint POST para agregar un usuario
@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente"}

# Endpoint GET para obtener la lista de usuarios
@app.get("/user", response_model=List[User])
def get_users():
    return users
