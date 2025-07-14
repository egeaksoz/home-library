from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books")
def get_books():
    return {"title": "My Name is Red", "author": "Orhan Pamuk", "language": "Turkish"}