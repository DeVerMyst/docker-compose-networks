from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel

app = FastAPI()

class IdPayload(BaseModel):
    id: str

@app.post("/receive_id")
async def receive_id(payload: IdPayload):
    logger.info(f"Received id: {payload.id}")
    return {"status": "success", "received": payload.id}