from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str


users_db = {
    'silvaneimartins': {
        'username': 'silvaneimartins',
        'fullname': 'Silvanei Martins',
        'email': 'oi@silvaneimartins.com.br',
        'disabled': False,
        'password': '123456'
    },
    'silviomartins': {
        'username': 'silviomartins',
        'fullname': 'Silvio Martins',
        'email': 'oi@silviomartins.com.br',
        'disabled': True,
        'password': '654321'
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Credencial de autenticação está invalida!',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Usuário inativo!'
        )

    return user


@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='O usuário não está correto!')

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='A senha ou nome de usuário não está correta!')

    return {'access_token': user.username, 'token_type': 'bearer'}


@router.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user