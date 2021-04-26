from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import database
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from schema import scategory
from repository import rcategory

router = APIRouter(
    prefix="/api/category",
    tags= ['Category']
)

get_db = database.get_db

@router.get('/{slug}', status_code=200, response_model=scategory.SingleCategory)
def single_category(slug: str,db : Session = Depends(database.get_db)):
    return rcategory.single_category(slug,db)