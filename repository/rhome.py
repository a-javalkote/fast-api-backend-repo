from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database
from models import mhome
from schema import shome



def get_all(db: Session = Depends(database.get_db)):
    posts = db.query(mhome.SiteInfo).all()
    return posts