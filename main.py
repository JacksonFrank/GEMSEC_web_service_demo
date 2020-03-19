from fastapi import FastAPI
from data_wrangler import DataManager
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is a demo of a web API for the GEMSEC group for Winter 2020"}

@app.get("/csvfiles")
async def getCSVData(fileIndex: int = -1):
    manager = DataManager()
    data = {}
    if fileIndex < 0 or fileIndex > len(manager.CSVFiles):
        data = manager.csv_json_all()
    else:
        data = manager.csv_json(fileIndex)
    return data

class ExampleData(BaseModel):
    name: str
    description: str = "No description given"
    index: int

@app.post("/uploaddata")
async def uploadCSVData(*, data: List[ExampleData]):
    manager = DataManager()
    manager.write_json_csv(data, ['name', 'description', 'index'])
    return {"message": "Data uploaded successfully"}
