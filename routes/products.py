from fastapi import APIRouter

router = APIRouter()

@router.get('/products')
async def products():
    return ["Produtos 1", "Produtos 2", "Produtos 3", "Produtos 4", "Produtos 5"]