# API Produtos Inteligente

Este projeto é uma API desenvolvida em **Django + Django REST Framework** para gerenciar produtos de informática. Ela permite criar, listar, atualizar e excluir produtos, além de fornecer endpoints inteligentes, como média de preços, soma de preços, itens mais caros/baratos e filtragem por preço mínimo. A documentação automática é gerada pelo **Swagger**.

## Tecnologias utilizadas

- Python 3.13
- Django
- Django REST Framework
- drf-yasg (Swagger para documentação)
- SQLite (banco de dados)

## Como usar

1. **Clone o repositório**

git clone https://github.com/anabichequin-bit/api-produtos-inteligente.git
cd api-produtos-inteligente

Criar e ativar o ambiente virtual (opcional)
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

Instalar dependências
Copiar código
pip install -r requirements.txt

Rodar as migrations
Copiar código
python manage.py migrate

Rodar o servidor
Copiar código
python manage.py runserver

Acessar a API

Endpoints: http://127.0.0.1:8000/api/items/

Documentação Swagger: http://127.0.0.1:8000/swagger/

Documentação Redoc: http://127.0.0.1:8000/redoc/

Endpoints inteligentes
/api/items/mais_caro/ → Retorna o item mais caro

/api/items/mais_barato/ → Retorna o item mais barato

/api/items/soma_precos/ → Soma de todos os preços

/api/items/media_precos/ → Média de todos os preços

/api/items/contagem_itens/ → Total de itens

/api/items_acima_preco/?min_preco=X → Retorna itens com preço acima de X
