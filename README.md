# API Flask de Gerenciamento de Produtos

Bem-vindo ao projeto da API Flask de Gerenciamento de Produtos! Este projeto foi desenvolvido como parte de um desafio para uma vaga de estágio. A API permite realizar operações CRUD (Create, Read, Update, Delete) em produtos e armazenar os dados em um banco de dados SQLite.

## Instruções de Uso

Siga estas instruções para executar a API em sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Você pode verificar a versão do Python usando o comando:

```bash
python --version
```

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
    pip install -r requirements.txt
    ```

4. **Execute a API:**

    ```bash
    flask run
    ```

5. **Faça o CRUD utilizando "curl"**

5.1 **Criação de produto**
    
    - Criação de produto: Use o método POST em http://127.0.0.1:5000/products com os dados do produto em formato JSON.
    
    **Exemplo**
    
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name":"Novo Produto","description":"Descrição do Novo Produto"}' http://127.0.0.1:5000/products
    ```


5.2 **Visualização do produto por id**

    - Visualização de produto por ID: http://127.0.0.1:5000/products/<product_id>

    **Exemplo**

    ```bash
    curl http://127.0.0.1:5000/products/<product_id>
    ```


5.3 **Atualização de produto por ID**

    - Atualização de produto por ID: Use o método PUT em http://127.0.0.1:5000/products/<product_id> com os dados do produto a serem atualizados em formato JSON.

    **Exemplo**

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated product","description":"New description"}' http://127.0.0.1:5000/products/<product_id>
    ```

5.4 **Exclusão de produto por ID**    

    - Exclusão de produto por ID: Use o método DELETE em http://127.0.0.1:5000/products/<product_id>

    **Exemplo**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/products/<product_id>
    ```

6. **Acesse a API:**

    Acesse a API em seu navegador. Aqui está o endpoint de listagem de produtos:

    - Listagem de produtos: http://127.0.0.1:5000/products

### Observações

- Certifique-se de que a API esteja em execução (`flask run`) enquanto você realiza as requisições.
- Certifique-se de substituir <product_id> pelo ID do produto real que deseja manipular em cada comando curl.
- Lembre-se de editar as informações do produto (nome, descrição, etc.) de acordo com suas necessidades.