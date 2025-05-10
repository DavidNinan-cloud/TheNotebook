from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "The Notebook FastAPI backend is running!"}
