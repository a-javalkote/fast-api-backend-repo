from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from database import Base
from sqlalchemy.orm import relationship

class SiteInfo(Base):
    __tablename__ = 'tblsiteinfo'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Text)
    status = Column(Integer)

class Category(Base):
    __tablename__ = 'tblcategory'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String)
    description = Column(Text)
    parent_id = Column(Integer)
    counter = Column(Integer)
    status = Column(Integer)

class Users(Base):
    __tablename__ = 'tblusers'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email_id = Column(String)
    email_verify = Column(String)
    password_verify = Column(String)
    online_status = Column(String)
    role_id = Column(Integer)
    status = Column(Integer)

class Post(Base):
    __tablename__ = 'tblpost'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String)
    short_desc = Column(Text)
    description = Column(Text)
    post_tag = Column(Text)
    category_id = Column(Integer, ForeignKey('tblcategory.id'))
    auther_id = Column(Integer, ForeignKey('tblusers.id'))
    slug = Column(Text)
    meta_desc = Column(Text)
    meta_keyword = Column(Text)
    created_datetime = Column(DateTime)
    approved = Column(Integer)
    status = Column(Integer)
    
    category = relationship(Category)
    auther = relationship(Users)
    