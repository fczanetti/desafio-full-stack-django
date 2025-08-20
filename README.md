# desafio-full-stack-django
Desafio Django

- [ ] Adicionar instruções para rodar testes e projeto no readme;
- [ ] Adicionar ci/cd;
- [x] Adicionar navbar ou opção para o usuário ir para o dashboard;
- [x] Adicionar dashboard;

# Introdução

Este projeto escrito em `Python` e `Django` consiste em um formulário onde candidatos podem se inscrever em vagas abertas, e em um dashboard que apresenta as estatísticas de candidatos inscritos e vagas disponíveis.

# Como executar os testes

- clone este repositório através do seguinte comando: 
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