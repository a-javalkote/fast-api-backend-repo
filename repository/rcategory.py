from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database, schemas, models

def all_category(db: Session = Depends(database.get_db)):
    Category = db.query(models.Category).all()
    return Category

def single_category(slug: str,db: Session = Depends(database.get_db)):
    Category = db.query(models.Category).filter(models.Category.slug == slug).first()
    if not Category:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{slug} is not available")
    return Category

def create(request: schemas.Category, db: Session = Depends(database.get_db)):
    Category = db.query(models.Category).filter(models.Category.slug == request.slug)
    if not Category.first():
        db_category = models.Category(**request.dict())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        msg = 'Category created successfully'
    else :
        msg = "Error"
        raise HTTPException(status_code = status.HTTP_302_FOUND, detail = f"Category already present in database")

    return msg

def update(id: int, request: schemas.UpdateCategory, db: Session):
    Category = db.query(models.Category).filter(models.Category.id == id)
    if not Category.first():
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Category not found")
       
    db.query(models.Category).filter(models.Category.id == id).update({models.Category.name: request.name, models.Category.slug: request.slug, models.Category.description: request.description, models.Category.parent_id: request.parent_id})
    db.commit()
    return "Updated"

def delete(id: int, db: Session = Depends(database.get_db)):
    Category = db.query(models.Category).filter(models.Category.id == id)
    if not Category.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Category not found")
    
    Category.delete()
    db.commit()
    return 'Category deleted'