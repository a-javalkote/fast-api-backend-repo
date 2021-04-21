from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(
    prefix="/api/post",
    tags= ['Posts']
)

@router.get('/')
def read_root():
    return {"Hello": "World"}