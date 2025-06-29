from typing import Annotated, List, Union

from dns.resolver import query
from fastapi import APIRouter, Query

router = APIRouter(prefix='/items', tags=['valida texto'])


# Query com valor padrão
@router.get('/')
async def read_items(
        q: Union[str, None] = Query(
            default=None, min_length=3, max_length=50, pattern='^fixedquery$'
        )
):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# Usando Annotated
@router.get('/annotated')
async def read_items(
        q: Annotated[str, None, Query(
            min_length=3, max_length=50, pattern='^fixedquery$')
        ] = None
):
    results = { 'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# valores padrão
@router.get('/default')
async def read_items(q: str = Query(default='fixedquery', min_length=3)):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# valor padrão com annotated
@router.get('/default/annotated')
async def read_items(q: Annotated[str, Query(min_length=3)] = 'fixedquery'):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# valor obrigatorio
@router.get('/obrigatorio')
async def read_items(q: str = Query(min_length=3)):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


@router.get('/obrigatorio/annotated')
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# lista de parametros
@router.get('/lista')
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {'q': q}
    return query_items


@router.get('/lista/annotated')
async def read_items(q: Annotated[List[str] | None, Query(min_length=3)] = None):
    query_items = {'q': q}
    return query_items


# lista de parametros valor padrão
@router.get('/lista/valor')
async def read_items(q: List[str] = Query(default=['foo', 'bar'])):
    query_items = {'q': q}
    return query_items


@router.get('/lista/valor/annotated')
async def read_items(q: Annotated[List[str], Query()] = ['foo', 'bar']):
    query_items = {'q': q}
    return query_items


# usando list
@router.get('/lista/tipo')
async def read_items(q: list = Query(default=[])):
    query_items = {'q': q}
    return query_items


@router.get('/lista/tipo/annotated')
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {'q': q}
    return query_items


# declarando metadados
@router.get('/metadados')
async def read_items(
        q: Union[str, None] = Query(
            default=None,
            title="Query string",
            description='Query string for the items to search in the database that have a good match',
            min_length=3
        )
):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results


@router.get('/metadados/annotated')
async def read_items(
        q: Annotated[str | None, Query(
            title='Query string',
            min_length=3,
            description='Query string for the items to search in the database that have a good match'

        )
        ] = None
):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results


# alias de parametros
@router.get('/alias')
async def read_items(
        q: Union[str, None] = Query(default=None, alias='item-query')
):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results


@router.get('/alias/annotated')
async def read_items(q: Annotated[str | None, Query(alias='item-query')] = None):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results


# parametros descontinuados
@router.get('/descontinuado')
async def read_items(
        q: Union[str, None] = Query(
            default=None,
            alias='item-query',
            title='Query string',
            description='Query string for the items to search in the database that have a good match',
            min_length=3,
            max_length=50,
            pattern='^fixedquery$',
            deprecated=True
        )
):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results


@router.get('/descontinuado/annotated')
async def read_items(
        q: Annotated[str | None, Query(
            alias='item-query',
            title='Query string',
            description='Query string for the items to search in the database that have a good match',
            min_length=3,
            max_length=50,
            pattern='^fixedquery$',
            deprecated=True
        ) ] = None
):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results