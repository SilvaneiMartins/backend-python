# BACKEND PYTHON

![BACKEND_PYTHON](https://img.shields.io/badge/BACKEND-PYTHON-blue.svg)
<br />
![BACKEND_PYTHON](https://i.imgur.com/u4ttTVE.jpg)


<h3 align="center">
	🚧  APLICAÇÃO BACKEND PYTHON...  🚧
</h3>

# Informação maquina windows:
O tutorial foi criado para ajudar você na sua execução do projeto. Além disso, será considerado que você já possui o ambiente python configurado de desenvolvimento em sua máquina.

# Observação muito importante:
O projeto em fase de desenvolvimento, não é recomendado para uso em produção ou que realize copia de trecho de código para usabilidade, por que muita coisa vai mudar ainda.

# Algumas image do projeto:
<h4 align="left">
	Algumas imagens do projeto em desenvolvimento.
</h4>
<h1 align="center">
 	<a href="https://imgur.com/ReEqzw8"><img src="https://i.imgur.com/ReEqzw8.png" title="source: imgur.com" /></a>
	<br />
	<a href="https://imgur.com/1hUm3cz"><img src="https://i.imgur.com/1hUm3cz.png" title="source: imgur.com" /></a>
	<br />
    <a href="https://imgur.com/GEclW9u"><img src="https://i.imgur.com/GEclW9u.png" title="source: imgur.com" /></a>
	<br />
</h1>

<h4 align="left">
	Image da documentação em desenvolvimento.
</h4>
<h1 align="center">
 	<a href="https://imgur.com/EFS0vTk"><img src="https://i.imgur.com/EFS0vTk.png" title="source: imgur.com" /></a>
	<br />
    <a href="https://imgur.com/dACueTQ"><img src="https://i.imgur.com/dACueTQ.png" title="source: imgur.com" /></a>
	<br />
</h1>

# Features
-   [ X ] Rota lista todos usuários;
-   [ X ] Rota lista um usuário por id (Path);
-   [ X ] Rota lista um usuário por id (Query);
-   [ X ] Rota cria um usuário;
-   [ X ] Rota atualiza um usuário;
-   [ X ] Rota deleta um usuário;
-   [ X ] Função para buscar usuário por ID;

# Instrução para clonar o projeto:
```bash
    # Clonar o repositório
    $ git https://github.com/SilvaneiMartins/backend-python

    # Acessar a pasta do projeto
    $ cd backend-python
```

# Instrução criar ambiente virtual e ativar:
```bash
    # Criação do ambiente virtual
    $ python3 -m venv venv

    # Ativação do ambiente virtual no linux ou mac
    $ source venv/Scripts/activate

    # Ativação do ambiente virtual no windows
    $ ./venv/Scripts/activate
```	

# Instrução de configuração FastAPI:
```bash
    # Instalar framework FastAPI
    $ pip install "fastapi[all]"

    # Criar um arquivo main.py
    $ touch main.py

    # Informar no arquivo main.py
    from fastapi import FastAPI

    app = FastAPI()

    @app.get('/')
    async def root():
        return 'Hello Word'

    # Subir o servidor FastAPI
    $ uvicorn main:app --reload

    # Caminho de execução do servidor FastAPI
    $ http://127.0.0.1:8000
```	

# Instrução para rodar documentação:
```bash
    # Rodar documentação com docs
    $ http://127.0.0.1:8000/docs

    # Rodar documentação com redoc
    $ http://127.0.0.1:8000/redoc
```	

# Tecnologias que estamos utilizando no projeto:
-   [Python](https://www.python.org/)
-   [FastAPI](https://fastapi.tiangolo.com/pt/)
-   [Uvicorn](https://www.uvicorn.org/)

# License
Este projeto está sob a licença CC0-1.0. Caso gostaria de ler, por favor acessar a licença aqui neste link [LICENSE](https://github.com/SilvaneiMartins/backend-python/blob/master/LICENSE) para maiores informações.

# Developer
<a href="https://github.com/SilvaneiMartins">
    <img
        style="border-radius:50%"
        src="https://github.com/SilvaneiMartins.png"
        width="100px;"
        alt="Silvanei Martins"
    />
    <br />
    <sub>
        <b>Silvanei de Almeida Martins</b>
    </sub>
    <br />
</a>
    🚀
 </a>
Feito com ❤️ por Silvanei Martins