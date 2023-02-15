from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Modelo:str
    Marca:str
    Precio:int
    Color:str
   



users_list= [User(id=1,Modelo="Pans", Marca="Puma", Precio="50000",Color="Negro" ),
             User(id=2,Modelo="Playera", Marca="Nike", Precio="60000",Color="Gris"),
             User(id=3,Modelo="Sudadera", Marca="Nike", Precio="80000",Color="Azul"),  
             User(id=4,Modelo="Short", Marca="Nike", Precio="10000",Color="Rojos"),
             User(id=5,Modelo="Top", Marca="Nike", Precio="12000",Color="Blancos")]
             

@router.get("/ropa/")
async def usersclass():
    return (users_list)
