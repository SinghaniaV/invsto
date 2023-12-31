from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

try:
	SQLALCHEMY_DATABASE_URL = 'mysql://<user>:<password>@<host>:<post>/<database>'
	engine = create_engine(SQLALCHEMY_DATABASE_URL)

except Exception as e:
	print('Unable to access mysql database', repr(e))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()