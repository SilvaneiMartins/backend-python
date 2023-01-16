from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
        prefix='/products', 
        tags=["products"] , 
        responses={404: {"Message": "Produto não encontrado!"}}
    )

class Product(BaseModel):
    id: int
    name: str
    category: str
    qtde: int
    price: float


lista_produtos = [
    Product(id=1, name='Coca Cola', category='Bebida' , qtde=10, price=3.50),
    Product(id=2, name='Cerveja Heiniken', category='Bebida' , qtde=5, price=6.50),
    Product(id=3, name='Coca Cola 2 Lt', category='Bebida' , qtde=10, price=9.50),
    Product(id=4, name='Corona Longnek Cx', category='Bebida' , qtde=3, price=36.50),
    Product(id=5, name='Carvão', category='Pacote', qtde=2, price=7.50),
]

@router.get('/')
async def products():
    return lista_produtos

    
@router.get('/{id}')
async def products(id: int):
    return search_products(id)


# Função para buscar produto por ID
def search_products(id: int):
    products = filter(lambda user: user.id == id, lista_produtos)
    try:
        return list(products)[0]
    except:
        return {'Error': 'Produto não encontrado!'}