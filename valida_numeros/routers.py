from typing import Annotated

from fastapi import APIRouter, Path, Query

router = APIRouter(prefix='/valida/numero', tags=['validações de numeros'])


@router.get('/items/{item_id}')
async def read_items(
        item_id: int = Path(title='The ID of the item to get'),
        q: str | None = Query(default=None, alias='item-query')
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/annotated')
async def read_items(
        item_id: Annotated[int, Path(title='The ID of the item to get')],
        q: Annotated[str  | None, Query(alias='item-query')] = None
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/obrigatorio')
async def read_items(
        q: str, item_id: int = Path(title='The ID of the item to get')
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/obrigatorio/annotated')
async def read_items(
        q: str, item_id: Annotated[int, Path(title='The ID of the item to get')]
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/kwargs')
async def read_items(
        *, item_id: int = Path(title='The ID of the item to get'), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results
