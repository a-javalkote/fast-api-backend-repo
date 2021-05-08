from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, status, HTTPException
import database, schemas, main, Oauth2
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from repository import rpost
from fastapi_pagination import add_pagination, paginate, Page, Params

router = APIRouter(
    prefix="/api/post",
    tags= ['Posts']
)

get_db = database.get_db

@router.get('', response_model=List[schemas.SinglePost])
async def all_post(db : Session = Depends(database.get_db)):
    return rpost.all_post(db)
    
@router.get('/category/{id}', status_code=200,response_model=Page[schemas.CategorywisePost])
async def category_wise_post(id:int, params: Params = Depends() ,db : Session = Depends(database.get_db)):
    return paginate(rpost.category_wise_post(id,db), params)

@router.get('/auther/{id}', status_code=200,response_model=Page[schemas.AutherwisePost])
async def auther_wise_post(id:int, params: Params = Depends() ,db : Session = Depends(database.get_db)):
    return paginate(rpost.auther_wise_post(id,db), params)

@router.get('/tag/{tag_name}', status_code=200,response_model=Page[schemas.TagwisePost])
async def tag_wise_post(tag_name:str, params: Params = Depends() ,db : Session = Depends(database.get_db)):
    return paginate(rpost.tag_wise_post(tag_name,db), params)

@router.get('/find', status_code=200, response_model=Page[schemas.SerachwisePost])
async def search_post(q: Optional[str] = None, params: Params = Depends(), db : Session = Depends(database.get_db)):
    skeyword=q.replace('-',' ')
    return paginate(rpost.search_post(skeyword,db), params)

@router.get('/{slug}', status_code=200,response_model=schemas.SinglePost)
async def single_post(slug:str, db : Session = Depends(database.get_db)):
    return rpost.single_post(slug,db) 

@router.post('/create', status_code=200)
async def create_post(request: schemas.Post, db : Session = Depends(get_db), get_current_user: schemas.Login = Depends(Oauth2.get_current_user)):
    return rpost.create(request, db)

@router.put('/update/{id}', status_code = 200)
async def update_post(id: int, request : schemas.UpdatePost, db : Session = Depends(get_db), get_current_user: schemas.Login = Depends(Oauth2.get_current_user)):
    return rpost.update(id, request, db)

@router.delete('/delete/{id}', status_code = 200)
async def delete_post(id: int, db : Session = Depends(get_db), get_current_user: schemas.Login = Depends(Oauth2.get_current_user)): 
    return rpost.delete(id, db)

add_pagination(router)