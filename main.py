from typing import Optional
from deepface import DeepFace
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/face")
async def face():
    objs = DeepFace.analyze(
        img_path="img4.jpg",
        actions=["age"],
    )
    return objs


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
