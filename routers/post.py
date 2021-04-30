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

@router.get('/{slug}', status_code=200,response_model=schemas.SinglePost)
def single_post(slug:str, db : Session = Depends(database.get_db)):
    return rpost.single_post(slug,db)