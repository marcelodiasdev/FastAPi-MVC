from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Usuários"]) # tags para exibir o nome da coleção no swagger


@users_routes.post("/users")
async def criar_usuario():
    return JSONResponse(content={"Ola": "mundo"}, status_code=200)
