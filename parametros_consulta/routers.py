from typing import Annotated

from fastapi import APIRouter, Query

from parametros_consulta.models import FilterParams

router = APIRouter(prefix='/parametros', tags=['parametros de consulta'])


@router.get('/items')
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
