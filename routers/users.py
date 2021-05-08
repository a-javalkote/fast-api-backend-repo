from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, status, HTTPException
import database, schemas, main, Oauth2
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from repository import rusers
from fastapi_pagination import add_pagination, paginate, Page, Params

router = APIRouter(
    prefix="/api/user",
    tags= ['Users']
)