from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
        prefix='/users',
        tags=["users"], 
        responses={404: {"Message": "Usuário não encontrado!"}}
    )

class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int

lista_usuario = [
    User(id=1, name='Silvanei', lastname='Martins', url='http://silvaneimartins.com.br', age=44), 
    User(id=2, name='Silvio', lastname='Dev', url='http://silviodev.com.br', age=43),
    User(id=3, name='Silvana', lastname='Aparecida', url='http://silvanaaparecida.com.br', age=37)
]


# Lista de todos usuários
@router.get('/')
async def users():
    return lista_usuario


# Path -> Lista de usuários por ID
@router.get('/{id}')
async def users(id: int):
    return search_users(id)


# Query -> Lista de usuários por ID
@router.get('/')
async def users(id: int):
    return search_users(id)


# Criar um usuário
@router.post('/', response_model=User ,status_code=201)
async def users(user: User):
    if type(search_users(user.id)) == User:
        raise HTTPException(status_code=404, detail='Usuário já cadastrado!')

    lista_usuario.append(user)
    return user


# Atualização de usuário
@router.put('/')
async def users(user: User):
    found = False

    for index, saved_user in enumerate(lista_usuario):
        if saved_user.id == user.id:
            lista_usuario[index] = user
            found = True

    if not found:
        return {'Error': 'Usuário não foi atualizado!'}

    return user


# Deletar usuário
@router.delete('/{id}')
async def users(id: int):
    found = False

    for index, saved_user in enumerate(lista_usuario):
        if saved_user.id == id:
            del lista_usuario[index]
            found = True

    if not found:
        return {'Error': 'Usuário não foi encontrado!'}

    return {'Exclusão': 'Usuário deletado!'}


# Função para buscar usuário por ID
def search_users(id: int):
    users = filter(lambda user: user.id == id, lista_usuario)

    try:
        return list(users)[0]
    except:
        return {'Error': 'Usuário não encontrado!'}