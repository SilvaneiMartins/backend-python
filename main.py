from fastapi import FastAPI

from routes import products, users

app = FastAPI()

# Rotas de produtos
app.include_router(products.router)
app.include_router(users.router)

@app.get('/')
async def root():
    return 'Silvanei Martins'
