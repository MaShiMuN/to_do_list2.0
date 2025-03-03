from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_items():
    return {"items": [{"name": "Item One"}, {"name": "Item Two"}]}