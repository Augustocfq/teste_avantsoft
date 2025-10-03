# Teste Avantsoft - API RESTful

Uma API desenvolvida para o teste técnico da Avantsoft, utilizando Flask e SQLAlchemy para criar um serviço RESTful de gerenciamento de estudantes.

## Principais Tecnologias

- **Flask**: Microframework para desenvolvimento web em Python, utilizado para construir a base da API.
- **SQLAlchemy**: ORM (Object Relational Mapper) para facilitar a comunicação com o banco de dados.
- **Pipenv**: Gerenciador de dependências do projeto e do ambiente virtual.

## Estrutura do Projeto

```tree
.
├─── api/
├─── services/
├─── models/
├─── app.py
└─── config.py
```

- **`api/`**: Administra todos os endpoints da API.
- **`services/`**: Administra as regras de negócio da API.
- **`models/`**: Define os modelos de dados utilizando SQLAlchemy.
- **`app.py`**: Inicializador do servidor Flask.
- **`config.py`**: Configurações do servidor flask.

## Como Executar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/Augustocfq/teste_avantsoft.git
    ```

2. **Instale o Pipenv (caso não o tenha):**

    ```bash
    pip install pipenv
    ```

3. **Instale as dependências do projeto:**

    ```bash
    pipenv install
    ```

4. **Ative o ambiente virtual:**

    ```bash
    pipenv shell
    ```

5. **Inicie o servidor de desenvolvimento:**

    ```bash
    python app.py
    ```

## Uso

### students endpoint

#### POST .../students

eg. REQUEST:

```json
{
    "nome": "Gabriel",
    "nota": 9.2
}
```

eg. RESPONSE:

```json
{
    "id": 2,
    "message": "Estudante adicionado com sucesso.",
    "nome": "Gabriel",
    "nota": 9.2
}
```

#### GET .../students

eg. RESPONSE:

```json
[
    {
        "id": 1,
        "nome": "Gabriel",
        "nota": 9.2,
        "primeira letra do nome que não se repete.": "g"
    },
    {
        "id": 2,
        "nome": "Marcos",
        "nota": 5.2,
        "primeira letra do nome que não se repete.": "m"
    },
    {
        "id": 3,
        "nome": "Augusto",
        "nota": 10.0,
        "primeira letra do nome que não se repete.": "a"
    },
    {
        "id": 4,
        "nome": "Anna",
        "nota": 2.1,
        "primeira letra do nome que não se repete.": "_"
    }
]
```

#### GET .../students/{id}

eg. RESPONSE:

```json
{
    "id": 3,
    "nome": "Augusto",
    "nota": 10.0,
    "primeira letra do nome que não se repete.": "a"
}
```
