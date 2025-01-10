from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers.contracts import router as contract_router
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()

app.include_router(contract_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Carbon Credit Smart Contract Generator!"}
