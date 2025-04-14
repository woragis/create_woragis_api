from fastapi import APIRouter

from app.services.kafka.producer import send_event


router = APIRouter(prefix="/kafka", tags=["Kafka"])


@router.post("/send-metric")
async def send_metric():
    send_event("metrics", {"user_id": 123, "event": "signup"})
    return {"status": "sent"}
