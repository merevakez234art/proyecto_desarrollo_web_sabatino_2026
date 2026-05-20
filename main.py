from fastapi import FastAPI
import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

mis_mascotas = {
    1: {
        "nombre": "baly",
        "raza": "perro"
    },
    2:{
        "nombre": "sorucho",
        "raza": "gato"
    },
    3: {
        "nombre": "pepe",
        "raza": "cotorro"
    }
}

@app.get("/")
def Hola_mundo():
    return {
        "mensaje":"Hola mundo"
    }


@app.get("mascotas/{id}")
def detalle_mascotas(id : int, response:Response):
    #consultar base de datos
    mascota = mis_mascotas.get(id,None)
    print(mascota)
    if not mascota:
        mascota = {} 
        response.status_code =status.HTTP_404_NOT_FOUND
        return mascota
    class Mascota(BaseModel):
        id:int
        nombre:str
        raza:str
   
    @app.get("/mascotas")
    def registra_mascotas(mascota:mascota):
        mis_mascotas [mascota.id ] = mascota

