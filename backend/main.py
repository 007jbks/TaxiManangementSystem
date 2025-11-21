from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers.admin import admin
from routers.auth import auth
from routers.booking import booking
from routers.taxi import taxi

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")

app.include_router(auth)
app.include_router(booking)
app.include_router(taxi)
app.include_router(admin)


@app.get("/")
def root():
    return {"message": "Server running!"}
