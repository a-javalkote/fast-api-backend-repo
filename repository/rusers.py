from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database, models, schemas
from hashing import Hash

def all_users(db: Session = Depends(database.get_db)):
    user = db.query(models.Users).all()
    return user

def single_user(username: str,db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{username} is not available")
        
    return user

def create(request: schemas.Users, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.username == request.username)
    if not user.first():
        #db_user = models.Users(**request.dict())
        db_user = models.Users(username=request.username, password=Hash.bcrypt(request.password), first_name=request.first_name, last_name=request.last_name, email_id=request.email_id, role_id=request.role_id, status=request.status)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        msg = 'User created successfully'
    else :
        msg = "Error"
        raise HTTPException(status_code = status.HTTP_302_FOUND, detail = f"User already present in database")

    return msg

def update(id: int, request: schemas.UpdateUsers, db: Session):
    user = db.query(models.Users).filter(models.Users.id == id)
    if not user.first():
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found") 
    db.query(models.Users).filter(models.Users.id == id).update({models.Users.first_name: request.first_name, models.Users.last_name: request.last_name})
    db.commit()
    return "Updated"

def delete(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    user.delete()
    db.commit()
    return 'User deleted'