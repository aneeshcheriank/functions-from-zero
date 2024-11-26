from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from pydantic import BaseModel

from fireCLI import scrape

app = FastAPI()

class Wiki(BaseModel):
    name: str

@app.get('/')
async def root():
    return {'message': 'Hello'}

@app.post('/wiki')
async def predict_story(wiki: Wiki):
    result = scrape(name = wiki.name)
    payload = {'wikipage': result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """
    Add two numbers tougther
    """
    total = num1+num2
    return {'total': total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
