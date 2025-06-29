from fastapi import APIRouter

from corpo_requisicao.item import Item

router = APIRouter(prefix='/items')


# corpo da requisição
@router.post('/')
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict


# corpo da requisição + parametros de rota
@router.put('/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, **item.model_dump()}


# corpo + parametros de rota e consulta
@router.put('/all/{item_id}')
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {'item_id': item_id, **item.model_dump()}
    if q:
        result.update({'q': q})
    return result
