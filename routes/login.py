from fastapi import APIRouter, Response, Depends, HTTPException, status
from database.mongodb import db
from datetime import datetime
from middleware.validacionToken import ValidacionToken
from fastapi.security import OAuth2PasswordRequestForm

from starlette.status import HTTP_204_NO_CONTENT

from model.ModelLogin import LoginModel, LoginResponse


login = APIRouter(
    route_class=ValidacionToken,
    tags=["Login"],
)


@login.post("/login")
async def Login(user:LoginModel, response: LoginResponse):
    return {
        "message": "Login",
        "status": 200,
        "data": {
            "token": "token"
        }
    }


