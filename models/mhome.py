from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class SiteInfo(Base):
    __tablename__ = 'tblsiteinfo'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Text)
    status = Column(Integer)
    