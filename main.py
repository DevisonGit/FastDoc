from typing import Union

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {'item_name': 'foo'}, {'item_name': 'bar'}, {'item_name': 'baz'}
]


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/union/items/{item_id}')
async def read_item_union(item_id: str, q: Union[str, None] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/bool/items/{item_id}')
async def read_item_bool(
        item_id: str, q: str | None = None, short: bool = False
):
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {
                'description':
                    'this is a amazing item that has a long description'
            }
        )
    return item


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {'item_id': item_id ,'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {
                'description':
                    'this is a amazing item that has a long description'
            }
        )
    return item


@app.get('/needy/items/{item_id}')
async def read_user_item(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item


@app.get('/mixer/items/{item_id}')
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
    return item
