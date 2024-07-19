# Biblioteca de Músicas com FastAPI


## Estrutura do Projeto

A aplicação será uma API de Biblioteca de Músicas que permitirá realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em uma coleção de músicas.

## Funcionalidades

A API deve permitir:

- **Criar uma música:** Adicionar uma nova música à biblioteca.
- **Listar todas as músicas:** Obter uma lista de todas as músicas na biblioteca.
- **Selecionar música aleatória:** Selecionar uma música da biblioteca aleatoriamente.
- **Obter uma música específica:** Buscar uma música pelo seu ID.
- **Atualizar uma música:** Atualizar as informações de uma música existente.
- **Deletar uma música:** Remover uma música da biblioteca.

## Tecnologias Utilizadas

- **FastAPI:** Framework principal para a criação da API.
- **Uvicorn:** Servidor ASGI para rodar a aplicação FastAPI.
- **Pydantic:** Para validação de dados e criação de modelos.

## Estrutura Inicial de Arquivos

```
music_library/
├── app/
│ ├── models.py # Definição dos modelos de dados
│ ├── database.py # Configuração do banco de dados
│ └── main.py # Ponto de entrada da aplicação
├── requirements.txt # Lista de dependências
├── dev-requirements.txt # Lista de dependências para desenvolvimento
├── README.md # Documentação do projeto
└── musics.mongodb # Seed para banco de dados
```

## Instruções para Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Virtualenv (opcional, mas recomendado)

### Passos para Configuração

1. Clone o repositório
2. Crie um ambiente virtual
3. Instale as dependências
4. Popule o banco de dados com o arquivo seed
5. Execute a aplicação com:
```
 uvicorn app.main:app --reload
```

## Endpoints

### Criar uma música
- URL: /songs
- Método: POST
- Body:
```
{
        name: 'Song name',
        artist: 'Song artist',
        album: 'Song album',
        release_year: 2024,
        genre: 'Song genre',
        image: 'Song image file path',
    }
```

### Listar todas as músicas
- URL: /songs
- Método: GET

### Selecionar música aleatória
- URL: /songs/random
- Método: GET


### Obter uma música específica
- URL: /songs/{song_id}
- Método: GET

### Atualizar uma música
- URL: /songs/{song_id}
- Método: PUT
- Body:
```
{
        name: 'Updated song name',
        artist: 'Updated song artist',
        album: 'Updated song album',
        release_year: 2024,
        genre: 'Updated song genre',
        image: 'Updated song image file path',
    }
```

### Deletar uma música
- URL: /musicas/{id}
- Método: DELETE


#### Boa sorte no desafio e divirta-se codando com FastAPI! 🚀