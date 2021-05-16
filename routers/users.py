from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, status, HTTPException
import database, schemas, main, Oauth2
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from repository import rusers
from fastapi_pagination import add_pagination, paginate, Page, Params

router = APIRouter(
    prefix="/api/user",
    tags= ['Users']
)

get_db = database.get_db
@router.get('', response_model=List[schemas.Users])
def all_users(db : Session = Depends(database.get_db)):
    return rusers.all_users(db)

@router.get('/{username}', status_code=200, response_model=schemas.Users)
def single_user(username: str,db : Session = Depends(database.get_db)):
    return rusers.single_user(username,db)

@router.post('/create', status_code=200)
def create_user(request: schemas.Users, db : Session = Depends(get_db), get_current_user: schemas.Login = Depends(Oauth2.get_current_user)):
    return rusers.create(request, db)

@router.put('/update/{id}', status_code = 200)
def update_user(id: int, request : schemas.UpdateUsers, db : Session = Depends(get_db),  get_current_user: schemas.Login = Depends(Oauth2.get_current_user)):
    return rusers.update(id, request, db)

@router.delete('/delete/{id}', status_code = 200)
def delete_user(id: int, db : Session = Depends(get_db), get_current_user: schemas.Login = Depends(Oauth2.get_current_user)): 
    return rusers.delete(id, db)
