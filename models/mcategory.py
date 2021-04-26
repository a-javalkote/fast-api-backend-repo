from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'tblcategory'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String)
    description = Column(Text)
    parent_id = Column(Integer)
    counter = Column(Integer)
    status = Column(Integer)
    