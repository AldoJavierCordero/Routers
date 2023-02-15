from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Modelo:str
    Marca:str
    Pies:int
    Color:str
   



users_list= [User(id=1,Modelo="French Door", Marca="Whirlpool", Pies="22",Color="Blanco" ),
             User(id=2,Modelo="GMDS", Marca="Samsung", Pies="18",Color="Gris"),
            User(id=3,Modelo="ATG", Marca="Acros", Pies="15",Color="Blanco"),  
             User(id=4,Modelo="Frigo bar", Marca="Lg", Pies="15",Color="dNegro onix"),
             User(id=5,Modelo="Mini refri", Marca="Lg", Pies="15",Color="Platino")]
             

@router.get("/Refris/")
async def usersclass():
    return (users_list)
