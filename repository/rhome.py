from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database, models

def get_all(db: Session = Depends(database.get_db)):
    posts = db.query(models.SiteInfo).all()
    return posts

def home_slider(db: Session = Depends(database.get_db)):
     posts = db.query(models.Post).order_by(models.Post.id.desc()).limit(7).all()
     return posts