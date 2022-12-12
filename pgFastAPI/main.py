import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Author
from models import Author as ModelAuthor
from models import Book
from models import Book as ModelBook
from schema import Author as SchemaAuthor
from schema import Book as SchemaBook

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
def root():
    return {"message": "Hello World"}

