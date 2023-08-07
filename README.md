# API Flask de Gerenciamento de Produtos

Bem-vindo ao projeto da API Flask de Gerenciamento de Produtos! Este projeto foi desenvolvido como parte de um desafio para uma vaga de estágio. A API permite realizar operações CRUD (Create, Read, Update, Delete) em produtos e armazenar os dados em um banco de dados SQLite.

## Instruções de Uso

Siga estas instruções para executar a API em sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Você pode verificar a versão do Python usando o comando:

```bash
python --version
```

### Autenticação

Ao abrir o site, ele pedirá para que você faça login.
O nome de usuário é "cozi.ai"
A senha é "Cozi.ai.Andrey"
### Passos

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/Andreyspl/API-Flask-Cozi.ai.git
    cd API-Flask-Cozi.ai
    ```

2. **Crie e ative o ambiente virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências:**

    ```bash
    python3 -m pip install -r requirements.txt
    ```

4. **Execute a API:**

    ```bash
    flask run
    ```

5. **Faça o CRUD utilizando "curl"**

5.1.  **Criação de produto (POST)**
    
    - Criação de produto: Use o método POST em http://127.0.0.1:5000/v1/products com os dados do produto em formato JSON.
    
    curl -X POST -H "Content-Type: application/json" -d '{"name":"Novo Produto","description":"Descrição do Novo Produto"}' -u <user>:<password> http://127.0.0.1:5000/v1/products

    **Exemplo**
    
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name":"New Product","description":"Description os the new product"}' -u cozi.ai:Cozi.ai.Andrey http://127.0.0.1:5000/v1/products
    ```


5.2.  **Visualização do produto por id (GET)**

    - Visualização de produto por ID: curl -u <user>:<password> http://127.0.0.1:5000/v1/products/<product_id>

    **Exemplo**

    ```bash
    curl -u cozi.ai:Cozi.ai.Andrey http://127.0.0.1:5000/v1/products/<product_id>
    ```


5.3.  **Atualização de produto por ID (PUT)**

    - Atualização de produto por ID: Use o método PUT em http://127.0.0.1:5000/v1/products/<product_id> com os dados do produto a serem atualizados em formato JSON.

    curl -X PUT -H "Content-Type: application/json" -d '{"name":"Produto Atualizado","description":"Nova descrição"}' -u <user>:<password> http://127.0.0.1:5000/v1/products/<product_id>

    **Exemplo**

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Product","description":"New description"}' -u cozi.ai:Cozi.ai.Andrey http://127.0.0.1:5000/v1/products/<product_id>
    ```


5.4. **Exclusão de produto por ID (DELETE)**    

    - Exclusão de produto por ID: Use o método DELETE em http://127.0.0.1:5000/v1/products/<product_id>

    curl -X DELETE -u <user>:<password> http://127.0.0.1:5000/v1/products/<product_id>


    **Exemplo**

    ```bash
    curl -X DELETE -u cozi.ai:Cozi.ai.Andrey http://127.0.0.1:5000/v1/products/<product_id>
    ```

6. **Acesse a API:**

    Acesse a API em seu navegador. Aqui está o endpoint de listagem de produtos:

    - Listagem de produtos: http://127.0.0.1:5000/v1/products

    Aqui, coloque o usuário e senha (cozi.ai /// Cozi.ai.Andrey)

### Observações

- Certifique-se de que a API esteja em execução (`flask run`) enquanto você realiza as requisições.
- Certifique-se de substituir <product_id> pelo ID do produto real que deseja manipular em cada comando curl.
- Certifique-se de substituir <user> e <password> pelo usuário e senha fornecidos, em cada comando curl.
- Lembre-se de editar as informações do produto (nome, descrição, etc.) de acordo com suas necessidades.