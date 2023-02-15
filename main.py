from fastapi import FastAPI
from routers import routers_5, routers2_5 , routers3_5 , router4_5, routers5_5 , routers6_5 , routers7_5 , routers8_5, routers_9_5, routers_10_5 

app= FastAPI()

app.include_router(routers_5.router)
app.include_router(routers2_5.router)
app.include_router(routers3_5.router)
app.include_router(router4_5.router)
app.include_router(routers5_5.router)
app.include_router(routers6_5.router)
app.include_router(routers7_5.router)
app.include_router(routers8_5.router)
app.include_router(routers_9_5.router)
app.include_router(routers_10_5.router)



@app.get("/")

async def imprimir():
    return "Trabajo de Routers"