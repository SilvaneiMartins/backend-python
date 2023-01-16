from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import products, users

app = FastAPI()

# Rotas da aplicação
app.include_router(products.router)
app.include_router(users.router)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return 'Servidor está rodando!'
