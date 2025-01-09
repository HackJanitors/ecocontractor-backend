from fastapi import FastAPI
from dotenv import load_dotenv
from routers.contracts import router as contract_router

load_dotenv()

app = FastAPI()

app.include_router(contract_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Carbon Credit Smart Contract Generator!"}
