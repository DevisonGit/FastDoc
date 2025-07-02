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


@router.get('/items/{items_id}/kwargs/annotated')
async def read_items(
        item_id: Annotated[int, Path(title='The ID of the item to get')], q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/maior')
async def read_items(
        *, item_id: int = Path(ge=1), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/maior/annotated')
async def read_items(
        item_id: Annotated[int, Path(ge=1)], q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/item/{item_id}/maior/menor')
async def read_items(
        *, item_id: int = Path(gt=0, le=1000), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/item/{item_id}/maior/menor')
async def read_items(
        item_id: Annotated[int, Path(gt=0, le=1000)], q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


@router.get('/item/{item_id}/float')
async def read_items(
        item_id: Annotated[int, Path(gt=0, le=1000)],
        q: str,
        size: Annotated[float, Query(gt=0, lt=10.5)]
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if size:
        results.update({'size': size})
    return results
