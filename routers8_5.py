from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Modelo:str
    Marca:str
    Precio:int
    Color:str
   



users_list= [User(id=1,Modelo="Porcelanato", Marca="Lamosa", Precio="500",Color="Negro" ),
             User(id=2,Modelo="Azulejo", Marca="Lamosa", Precio="600",Color="Gris"),
            User(id=3,Modelo="Azulejo", Marca="Interseramic", Precio="4500",Color="Blanco"),  
             User(id=4,Modelo="Marmol", Marca="Interceramic", Precio="1000",Color="dorados"),
             User(id=5,Modelo="Porcelanato", Marca="interceramic", Precio="12000",Color="Negro")]
             

@router.get("/Azulejos/")
async def usersclass():
    return (users_list)
