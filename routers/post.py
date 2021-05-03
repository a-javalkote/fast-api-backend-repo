from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import database, schemas
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from repository import rpost

router = APIRouter(
    prefix="/api/post",
    tags= ['Posts']
)

get_db = database.get_db


@router.get('', response_model=List[schemas.SinglePost])
def all_post(db : Session = Depends(database.get_db)):
    return rpost.all_post(db)

@router.get('/{slug}', status_code=200,response_model=schemas.SinglePost)
def single_post(slug:str, db : Session = Depends(database.get_db)):
    return rpost.single_post(slug,db) 

@router.post('/create', status_code=200)
def create_post(request: schemas.Post, db : Session = Depends(get_db)):
    return rpost.create(request, db)

@router.put('/update/{id}', status_code = 200)
def update_post(id: int, request : schemas.UpdatePost, db : Session = Depends(get_db)):
    return rpost.update(id, request, db)

@router.delete('/delete/{id}', status_code = 200)
def delete_post(id: int, db : Session = Depends(get_db)): 
    return rpost.delete(id, db)