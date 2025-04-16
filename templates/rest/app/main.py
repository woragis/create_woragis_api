from threading import Thread

from fastapi import FastAPI, WebSocket
from starlette.middleware.cors import CORSMiddleware

from app.routes.index import router as api_router
from app.data.database import Base, engine
from app.services.kafka.consumer import run_consumer

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    Thread(target=run_consumer, daemon=True).start()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
