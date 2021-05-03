from pydantic import BaseModel, Field, Json
from datetime import datetime
from typing import List, Optional
from pydantic.schema import schema

class SiteInfo(BaseModel):
    name: Optional[str]
    value: Json

    class Config:
	    orm_mode=True

class Category(BaseModel):
    name: str
    slug: str
    description: str
    parent_id: int
    counter:int
    status: int

    class Config:
	    orm_mode=True

class UpdateCategory(BaseModel):
    name: str
    slug: str
    description: str
    parent_id: int

    class Config:
        orm_mode=True

class SingleCategory(BaseModel):
    id: int
    name: str
    slug: str
    description: str 

    class Config():
        orm_mode = True

class CategoryForPost(BaseModel):
    id: int
    name: str
    slug: str

    class Config():
        orm_mode = True

class Users(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    parent_id: int
    counter:int
    status: int

    class Config:
	    orm_mode=True

class AutherName(BaseModel):
    id: int
    first_name: str
    last_name: str 

    class Config():
        orm_mode = True


class Post(BaseModel):
    title: str
    slug: str
    short_desc: str
    description: str
    meta_desc: str
    meta_keyword: str
    post_tag: str
    category_id: int
    auther_id: int
    approved:int
    created_datetime: datetime
    status: int

    class Config:
	    orm_mode=True

class SinglePost(BaseModel):
    id: int
    title: str
    slug: str
    description: str 
    post_tag: str
    category: CategoryForPost
    auther : AutherName
    meta_desc: str
    meta_keyword: str 
    created_datetime: datetime   
    
    class Config():
        orm_mode = True

class UpdatePost(BaseModel):
    title: str
    slug: str
    short_desc: str
    description: str 
    post_tag: str
    category: CategoryForPost
    auther : AutherName
    meta_desc: str
    meta_keyword: str   
    
    class Config():
        orm_mode = True

class CategorywisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str 
    post_tag: str
    auther : AutherName  
    created_datetime: datetime   
    
    class Config():
        orm_mode = True

class AutherwisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str 
    post_tag: str
    category: CategoryForPost
    created_datetime: datetime   
    
    class Config():
        orm_mode = True

class TagwisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str 
    post_tag: str 
    category: CategoryForPost
    auther : AutherName 
    created_datetime: datetime   
    
    class Config():
        orm_mode = True

class SerachwisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str
    post_tag: str
    category: CategoryForPost
    auther : AutherName
    created_datetime: datetime   
    
    class Config():
        orm_mode = True
