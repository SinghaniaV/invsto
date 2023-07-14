from fastapi import FastAPI, UploadFile
from database import engine, session, Base
from models import Tick_data
from insert import read_data, insert_data
import io

app = FastAPI()

Base.metadata.create_all(engine)

@app.post("/uploadfile")
async def upload_file(file: UploadFile):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        xlsx = io.BytesIO(f)

        data = read_data(xlsx)
        insert_data(data)
        
        return f'{file.filename} uploaded successfully'

@app.get("/viewfile")
def view_file():
    return session.query(Tick_data).all()