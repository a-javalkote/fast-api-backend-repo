from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import database, schemas
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from repository import rcategory

router = APIRouter(
    prefix="/api/category",
    tags= ['Category']
)

get_db = database.get_db
@router.get('', response_model=List[schemas.UpdateCategory])
def all_category(db : Session = Depends(database.get_db)):
    return rcategory.all_category(db)

@router.get('/{slug}', status_code=200, response_model=schemas.SingleCategory)
def single_category(slug: str,db : Session = Depends(database.get_db)):
    return rcategory.single_category(slug,db)

@router.post('/create', status_code=200)
def create_category(request: schemas.Category, db : Session = Depends(get_db)):
    return rcategory.create(request, db)

@router.put('/update/{id}', status_code = 200)
def update_category(id: int, request : schemas.UpdateCategory, db : Session = Depends(get_db)):
    return rcategory.update(id, request, db)

@router.delete('/delete/{id}', status_code = 200)
def delete_category(id: int, db : Session = Depends(get_db)): 
    return rcategory.delete(id, db)