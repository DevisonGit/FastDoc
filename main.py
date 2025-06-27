from pydantic import BaseModel
from typing import Union

from fastapi import FastAPI

from burgers import get_burgers

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
def read_root():
    return {'hello': 'word'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}


@app.get('/burgers')
async def read_burgers():
    burgers  = await get_burgers(2)
    return burgers
