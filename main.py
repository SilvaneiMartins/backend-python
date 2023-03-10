from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import basic_auth_users, jwt_auth_users, products, users

app = FastAPI()

# Rotas da aplicação
app.include_router(products.router)
app.include_router(users.router)

# Rotas de autenticação
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return 'Servidor está rodando!'
