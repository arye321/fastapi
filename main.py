from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
from starlette.responses import FileResponse

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/", response_class=PlainTextResponse)
async def create_item(item: Item):
    return "ok"
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/", response_class=PlainTextResponse)
async def lol():
    return 'lol'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')