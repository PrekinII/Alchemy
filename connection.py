import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USER = os.getenv("DB_USER")
NAME = os.getenv("DB_NAME")
PASS = os.getenv("DB_PASS")

DSN = f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()
session.close()
