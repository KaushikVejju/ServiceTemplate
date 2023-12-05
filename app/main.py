# This is a Python FastAPI template for SIF Projects.
from fastapi import FastAPI

app = FastAPI()

# This is a basic endpoint. Feel free to delete this and add more based on your liking.
@app.get("/")
def read_root():
    return {"Hello": "This is your service template."}
