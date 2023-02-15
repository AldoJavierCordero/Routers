from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Modelo:str
    Marca:str
    Precio:int
    Color:str
   



users_list= [User(id=1,Modelo="Casual", Marca="Levis", Precio="1000",Color="Negro" ),
             User(id=2,Modelo="Deportiva", Marca="Nike", Precio="500",Color="Gris"),
            User(id=3,Modelo="Formal", Marca="Aldo Conti", Precio="1500",Color="Blanco"),  
             User(id=4,Modelo="Casual", Marca="Levis", Precio="1000",Color="dorados"),
             User(id=5,Modelo="Deportiva", Marca="Adidas", Precio="1200",Color="Negro")]
             

@router.get("/Pantalones/")
async def usersclass():
    return (users_list)
