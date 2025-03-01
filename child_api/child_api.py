from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger

app = FastAPI()

class IdPayload(BaseModel):
    id: str

@app.post("/receive_id")
async def receive_id(payload: IdPayload):
    logger.info(f"Received id: {payload.id}")
    return {"message": "Id received"}