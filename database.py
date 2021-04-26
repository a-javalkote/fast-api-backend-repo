from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL ="mysql+mysqlconnector://treadte1_treadte1:treadte1_treadte1@treadtechnology.com:3306/treadte1_apitheprimepr"
SQLALCHEMY_DATABASE_URL ="mysql+mysqlconnector://root:@localhost:3306/apitheprimepr"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind= engine, autocommit= False, autoflush = False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()