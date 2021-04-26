from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import database
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from schema import shome
from repository import rhome

router = APIRouter(
    prefix="/api/home",
    tags= ['Home']
)
get_db = database.get_db

@router.get('/siteinfo', response_model=List[shome.SiteInfo])
def all(db : Session = Depends(database.get_db)):
    return rhome.get_all(db)