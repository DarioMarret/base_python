from fastapi import FastAPI
from routes.login import login

from fastapi.middleware.cors import CORSMiddleware
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

DEV = os.getenv("DEV")

app = FastAPI(
    title="XTRIM API",
    description="A simple API to manage contacts",
    version="1.0.0",
    root_path="/incoming" if DEV == "PRO" else "/",
    root_path_in_servers=True,
    authorizations={}
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login)