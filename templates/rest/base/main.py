from fastapi import FastAPI
from routes.index import router as api_router
from data.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)
