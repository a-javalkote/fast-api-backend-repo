from typing import Optional
from fastapi import FastAPI,Request
from routers import post,home
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Base, engine, get_db

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router)

templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
def read_root(request:Request):
    return templates.TemplateResponse("index.html",{"request": request})

