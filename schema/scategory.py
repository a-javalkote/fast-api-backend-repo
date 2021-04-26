from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic.schema import schema

class Category(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    parent_id: int
    counter:int
    status: int

    class Config:
	    orm_mode=True

class SingleCategory(BaseModel):
    id: int
    name: str
    slug: str
    description: str  
    
    class Config():
        orm_mode = True