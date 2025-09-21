from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
user_name=os.getenv("DB_USERNAME")
pwd=os.getenv("DB_PASSWORD")
host=os.getenv("DB_HOST")
port=os.getenv("DB_PORT")
db_name=os.getenv("DB_NAME")

# getting url
db_url=f"mysql+pymysql://{user_name}:{pwd}@{host}:{port}/{db_name}"
# creating engine
engine=create_engine(db_url,echo=True,future=True)
# binding engine object with the session
SessionLocal=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)

# Creating base for all model objects
Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

