from fastapi import Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session
import database, schemas, models

#All Post Details
def all_post(db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).all()
    return Post

#Create New Post 
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
#Update Post Details
def update(id: int, request: schemas.UpdatePost, db: Session):
    Post = db.query(models.Post).filter(models.Post.id == id)
    if not Post.first():
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post not found")
       
    db.query(models.Post).filter(models.Post.id == id).update({models.Post.name: request.name, models.Post.slug: request.slug, models.Post.description: request.description, models.Post.parent_id: request.parent_id})
    db.commit()
    return "Updated"
#Delete Post 
def delete(id: int, db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.id == id)
    if not Post.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post not found")
    
    Post.delete()
    db.commit()
    return 'Post deleted'

#Single Post View
def single_post(slug: str,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.slug == slug).first()
    if not Post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{slug} is not available")
    return Post

#Category Wise Post
def category_wise_post(id: int,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.category_id == id).all()
    if not Post:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post is not available")
    return Post

#Auther Wise Post
def auther_wise_post(id: int,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.auther_id == id).all()
    if not Post:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post is not available")
    return Post 

#Tag Wise Post
def tag_wise_post(tag_name: str,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(models.Post.post_tag.like(f'%{tag_name}%')).all()
    if not Post:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post is not available")
    return Post 

#Search Post
def search_post(skeyword: str,db: Session = Depends(database.get_db)):
    Post = db.query(models.Post).filter(or_(models.Post.title.like(f'%{skeyword}%'),models.Post.title.like(f'%{skeyword}%'),models.Post.description.like(f'%{skeyword}%'))).all()
    if not Post:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post is not available")
    return Post 