from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers.contracts import router as contract_router
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.include_router(contract_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Carbon Credit Smart Contract Generator!"}
