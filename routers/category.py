from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(
    prefix="/api/category",
    tags= ['Category']
)

@router.get('/homeslider')
def read_root():
    return {"Hello": "World"}