from typing import Optional
from fastapi import FastAPI, Request
from routers import home, category, post
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Base, engine, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="The Prime PR",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
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

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router)
app.include_router(category.router)
app.include_router(post.router)

templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
def read_root(request:Request):
    return templates.TemplateResponse("index.html",{"request": request})

