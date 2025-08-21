# Introdução

Este projeto escrito em `Python` e `Django` consiste em um formulário onde candidatos podem se inscrever em vagas abertas e em um dashboard que apresenta as estatísticas de candidatos inscritos e vagas disponíveis. Para que as instruções abaixo funcionem, estas devem ser executadas em um ambiente Linux.

# Como executar os testes

- Clone este repositório através do seguinte comando: 
```
git clone git@github.com:fczanetti/desafio-full-stack-django.git
```

- acesse a pasta do projeto e crie um ambiente virtual usando estes dois comandos:
```
cd desafio-full-stack-django
python -m venv .venv
```

- ative o ambiente virtual:
```
source .venv/bin/activate
```

- instale as bibliotecas necessárias:
```
pip install -r requirements-dev.txt
```

- copie o arquivo de referência com as variáveis de ambiente para um novo arquivo:
```
cp contrib/env-sample .env
```

- execute os testes:
```
pytest
```

# Como executar o projeto

Para executar o projeto, é necessário seguir todos os passos do tópico anterior (Como executar os testes). Uma vez que isso foi feito, basta seguir os próximos passos.

- Use o comando abaixo para aplicar as migrações no banco de dados:
```
python manage.py migrate
```

- após aplicar as migrações, crie um superusuário do Django:
```
python manage.py createsuperuser
```

- com o superusuário criado, execute o servidor local do Django:
```
python manage.py runserver
```

Neste momento, tanto o formulário quanto o dashboard já estarão acessíveis no endereço `http://127.0.0.1:8000`. Para poder interagir criando algumas vagas, acesse o painel de administração e use as credenciais fornecidas no momento de criar o superusuário para fazer login. Endereço: `http://127.0.0.1:8000/admin`.