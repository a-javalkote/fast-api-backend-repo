from typing import Optional
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Base, engine, get_db
from routers import auth, home, category, post, users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from repository import rauth
from sqlalchemy.orm import Session

app = FastAPI(
    title="The Prime PR",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
    docs_url="/demo",
    redoc_url=None
)


origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
def read_root(request:Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post('/login', status_code=200)
def login(request: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    return rauth.login_user(request, db)


app.include_router(auth.router)
app.include_router(home.router)
app.include_router(users.router)
app.include_router(category.router)
app.include_router(post.router)
