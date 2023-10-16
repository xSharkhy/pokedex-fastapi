from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/pokemon/{id}")
async def pokemon(id):
    if not id:
        return {"message": "Please provide an id"}
    
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        response.raise_for_status()
        data = response.json()
        
        return {
            "id": data["id"],
            "name": data["name"],
        }
    
    except requests.exceptions.RequestException as e:
        return {"message": "Pokemon not found"}
        
        
            