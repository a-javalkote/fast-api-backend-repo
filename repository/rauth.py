from fastapi import Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session
import database, schemas, models, JWTtoken
from hashing import Hash
#All Post Details
def register_user(request: schemas.Login,db: Session = Depends(database.get_db)):
    User = db.query(models.Users).filter(models.Users.username == request.username).first()
    if not User:
        db_User = models.Users(username= request.username, password= Hash.bcrypt(request.password), first_name= request.first_name, last_name= request.last_name, email_id= request.email_id)
        db.add(db_User)
        db.commit()
        db.refresh(db_User)
        msg = 'User created successfully'
    else :
        msg = "Error"
        raise HTTPException(status_code = status.HTTP_302_FOUND, detail = f"{request.username} already present in database")
    return msg

def login_user(request: schemas.Login,db: Session = Depends(database.get_db)):
    User = db.query(models.Users).filter(models.Users.username == request.username).first()
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found")
    if not Hash.verify(request.password, User.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    access_token = JWTtoken.create_access_token(data={"sub": User.username})
    return {"access_token": access_token, "token_type": "bearer"}
