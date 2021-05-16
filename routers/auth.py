from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, status, HTTPException
import database, schemas, main
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from repository import rauth
from fastapi_pagination import add_pagination, paginate, Page, Params

router = APIRouter(
    prefix="/api/auth",
    tags= ['Authentication']
)
get_db = database.get_db

@router.post('/login', status_code=200)
def login(request: schemas.Login, db : Session = Depends(get_db)):
    return rauth.login_user(request, db)

@router.post('/register', status_code=200)
def register(request: schemas.Register, db : Session = Depends(get_db)):
    return rauth.register_user(request, db)


@router.put('/changepassword/{id}', status_code = 200)
def update_user(id: int, request : schemas.ChangePassword, db : Session = Depends(get_db)):
    return rauth.change_password(id, request, db)

@router.get('/activation/{mailid}/{verifycode}', status_code = 200)
def verify_emails_id(mailid: str, verifycode : str, db : Session = Depends(get_db)):
    return rauth.verify_emailid(mailid, verifycode, db)