# Tech Start Talk - DRF
Esse repositório contém um exemplo de CRUD de produtos e categorias utilizando o Django REST Framework.

## Roteiro
O roteiro com a explicação passo-a-passo para a criação da aplicação pode ser acessado [aqui](https://docs.google.com/document/d/1a4OffwSFvH0PTeZ6CkM_eNAV77GULActgiv2Fjy3XMg/edit?usp=sharing). 

## Instruções de desenvolvimento
Clonar o repositório e entrar na pasta do projeto:

```bash
git clone git@github.com:julianaklulo/TST-DRF.git
cd TST-DRF
```

Criar o virtualenv e instalar as dependências:
```bash
virtualenv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```

Rodar as migrações e criar o super usuário:
```bash
(venv) python manage.py migrate
(venv) python manage.py createsuperuser
```

Executar o servidor de desenvolvimento:
```bash
(venv) python manage.py runserver
```

Acessar o servidor em: http://127.0.0.1/8000