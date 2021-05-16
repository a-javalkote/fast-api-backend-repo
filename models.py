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

    _post = relationship("Post", back_populates="category")

class Role(Base):
    __tablename__ = 'tblrole'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(Integer)

    role = relationship("Users", back_populates="_role")

class Users(Base):
    __tablename__ = 'tblusers'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email_id = Column(String)
    email_verify = Column(String)
    email_verify_code = Column(String)
    password_verify = Column(String)
    online_status = Column(String)
    role_id = Column(Integer, ForeignKey('tblrole.id'))
    status = Column(Integer)

    _post = relationship("Post", back_populates="auther")
    _role = relationship("Role", back_populates="role")

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
    published_datetime = Column(DateTime)
    approved = Column(Integer)
    status = Column(Integer)
    
    category = relationship("Category", back_populates="_post")
    auther = relationship("Users", back_populates="_post")
    