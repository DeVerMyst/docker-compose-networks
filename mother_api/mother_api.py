import requests
from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# Réseau interne Docker : on utilise le nom du service 'child'
CHILD_API_URL = "http://child:8001"

@app.post("/id")
async def send_to_child(id: str = Form(...)):
    try:
        response = requests.post(f"{CHILD_API_URL}/receive_id", json={"id": id})
        response.raise_for_status()
        return {"message": f"Sent id '{id}' to Child API"}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Communication error: {e}")