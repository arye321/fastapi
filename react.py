#uvicorn react:app --reload
from fastapi import FastAPI
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/build/static", StaticFiles(directory="build/static"), name="build/static")

@app.get("/")
async def read_index():
    return FileResponse('build/index.html')