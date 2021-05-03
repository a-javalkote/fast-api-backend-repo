from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database
import models

def single_post(slug: str,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.slug == slug).first()
    if not Post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{slug} is not available")
    return Post