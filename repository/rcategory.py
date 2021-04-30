from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database
import models

def single_category(slug: str,db: Session = Depends(database.get_db)):
    Category = db.query(models.Category).filter(models.Category.slug == slug).first()
    if not Category:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{slug} is not available")
    return Category