from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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
@app.get('/users/')
async def users():
    return lista_usuario


# Path -> Lista de usuários por ID
@app.get('/user/{id}')
async def user(id: int):
    return search_user(id)


# Query -> Lista de usuários por ID
@app.get('/user/')
async def user(id: int):
    return search_user(id)


# Criar um usuário
@app.post('/user/', status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail='Usuário já cadastrado!')

    lista_usuario.append(user)
    return user


# Atualização de usuário
@app.put('/user/')
async def user(user: User):
    found = False

    for index, saved_user in enumerate(lista_usuario):
        if saved_user.id == user.id:
            lista_usuario[index] = user
            found = True

    if not found:
        return {'Error': 'Usuário não foi atualizado!'}

    return user


# Deletar usuário
@app.delete('/user/{id}')
async def user(id: int):
    found = False

    for index, saved_user in enumerate(lista_usuario):
        if saved_user.id == id:
            del lista_usuario[index]
            found = True

    if not found:
        return {'Error': 'Usuário não foi encontrado!'}

    return {'Exclusão': 'Usuário deletado!'}


# Função para buscar usuário por ID
def search_user(id: int):
    users = filter(lambda user: user.id == id, lista_usuario)

    try:
        return list(users)[0]
    except:
        return {'Error': 'Usuário não encontrado!'}