from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from routers import partners
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Partner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for testing first
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(partners.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"message": "Partner API is running"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("static/favicon.ico")