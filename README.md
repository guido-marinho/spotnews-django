# Spotnews 
O Spot news é uma aplicação web que permite realizar consultas em notícias sobre tecnologia. 

## Como Rodar o Projeto

Clone o Repositório:

```bash
git@github.com:guido-marinho/spotnews-django.git
```
Navegue até o Diretório do Projeto:

```bash
cd spotnews-django
```
Crie o Ambiente Virtual:

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Instale as Dependências:

```bash
python3 -m pip install -r dev-requirements.txt
```

Execute o Docker Compose:

```bash
docker build -t spotnews-db .
```

Execute o MySQL via Docker:

```bash
docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
```

Rode o servidor:

```bash
 python3 manage.py runserver      
```

## Dependências
O Spotnews utiliza as seguintes bibliotecas e ferramentas:

Python==3.10 <br/>

black==23.3.0 <br/>
Django==4.2.3 <br/>
djangorestframework==3.14.0 <br/>
flake8==6.0.0 <br/>
mysqlclient==2.2.0  <br/>
Pillow==10.0.0 <br/>
