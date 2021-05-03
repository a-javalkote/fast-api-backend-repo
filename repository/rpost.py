from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database, schemas, models

def all_post(db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).all()
    return Post

def single_post(slug: str,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.slug == slug).first()
    if not Post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{slug} is not available")
    return Post

def create(request: schemas.Post, db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.slug == request.slug)
    if not Post.first():
        db_Post = models.Post(**request.dict())
        db.add(db_Post)
        db.commit()
        db.refresh(db_Post)
        msg = 'Post created successfully'
    else :
        msg = "Error"
        raise HTTPException(status_code = status.HTTP_302_FOUND, detail = f"Post already present in database")

    return msg

def update(id: int, request: schemas.UpdatePost, db: Session):
    Post = db.query(models.Post).filter(models.Post.id == id)
    if not Post.first():
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post not found")
       
    db.query(models.Post).filter(models.Post.id == id).update({models.Post.name: request.name, models.Post.slug: request.slug, models.Post.description: request.description, models.Post.parent_id: request.parent_id})
    db.commit()
    return "Updated"

def delete(id: int, db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.id == id)
    if not Post.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post not found")
    
    Post.delete()
    db.commit()
    return 'Post deleted'