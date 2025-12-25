'''

Connect mikone databse ro b SQLALCHEMY 
ma fght inja tarif mikonim k b kodom database vasl beshe
tamame code hameja hamine

'''


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine= create_engine(DATABASE_URL,echo=False, future=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine , autoflash=False, autocommit=False,future=True )


def get_session():
    return SessionLocal()
