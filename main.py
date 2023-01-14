from fastapi import FastAPI
from users import users

app = FastAPI()

@app.get('/')
async def root():
    return 'Silvanei Martins'
