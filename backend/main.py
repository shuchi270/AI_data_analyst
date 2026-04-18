from fastapi import FastAPI, UploadFile, File
import pandas as pd
from utils.loader import get_schema

app = FastAPI()

GLOBAL_DF = None
GLOBAL_SCHEMA = None

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    global GLOBAL_DF, GLOBAL_SCHEMA

    GLOBAL_DF = pd.read_csv(file.file)
    GLOBAL_SCHEMA = get_schema(GLOBAL_DF)

    return {"message": "Uploaded", "schema": GLOBAL_SCHEMA}