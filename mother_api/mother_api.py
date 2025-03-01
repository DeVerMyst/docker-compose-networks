from fastapi import FastAPI, HTTPException, Form
import requests

app = FastAPI()

CHILD_API_URL = "http://child:8001"

@app.get("/")
async def root():
    return {"message": "Hello World from Mother API"}

@app.post("/id")
async def send_to_child(id: str = Form(...)):
    try:
        response = requests.post(f"{CHILD_API_URL}/receive_id", json={"id": id})
        response.raise_for_status()
        return {"message": f"Sent id '{id}' to Child API"}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to communicate with Child API: {e}")