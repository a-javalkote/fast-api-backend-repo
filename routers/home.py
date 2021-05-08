from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import database
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
import schemas
from repository import rhome

router = APIRouter(
    prefix="/api/home",
    tags= ['Home']
)
get_db = database.get_db

@router.get('/siteinfo', response_model=List[schemas.SiteInfo])
def all(db : Session = Depends(database.get_db)):
    return rhome.get_all(db)

@router.get('/slider', response_model=List[schemas.SerachwisePost])
def homeslider(db : Session = Depends(database.get_db)):
    return rhome.home_slider(db)