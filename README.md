<div align="center">

# Atividades Complementares

![programming_language](https://img.shields.io/badge/python-3.10.12-informational) &nbsp;
![fastapi](https://img.shields.io/badge/fastapi-0.100.0-success) &nbsp;
![test](https://img.shields.io/badge/test_coverage-100-success)

API que coleta e disponibiliza informações sobre as atividades complementares da faculdade. 

Coletados via `Web Scraping` e disponibilizados no formato `JSON`


[Rotas](#telescope-rotas) &nbsp; • &nbsp; [Modelos](#book-modelos)


<br />
<br />

</div>

# :telescope: Rotas

###  :ledger: GET /activities

```text
http://127.0.0.1:8000/api/v2/activities
```

Filtros que podem ser aplicados

- `http://127.0.0.1:8000/api/v2/activities?group={int}`

#### :bookmark_tabs: group

O parâmetro `group` pode ser utilizado para retornar somente as atividades atribuídas ao grupo especificado. Podendo receber como valor somente números inteiros entre 1 e 4.

#### :bookmark_tabs: sorted

Por padrão essa rota já ordena os objetos retornados de maneira `decrescente` com base na quantidade de horas complementares que serão ganhas ao participar da atividade.

<br />

### :ledger: GET /activiteis/auth

```text
http://127.0.0.1:8000/api/v2/activities/auth
```

Requisitos:

- usuário
- senha


<br />
<br />

# :mailbox: Modelos

**GET - /activities**

```json
[
    {
        "date": "%d/%m/%Y %H:%M",
        "event": "str",
        "professor": "str",
        "local": "str",
        "city": "str",
        "group": 0,
        "hours": 0
    }
]
```

**GET - /activities/auth**

```json
[  
  {
    "group": 0,
    "event": "str",
    "event_url": "str",
    "remaining_vacancies": 0
  }
]
```


<br />
<br />

## :beginner: Retornos

### :negative_squared_cross_mark: Filtro inválido

Se o usuário utilizar o filtro para buscar um grupo específico, mas o número passado como parâmetro for diferente dos valores de 1 a 4, será retornado o seguinte `json`:

```text
GET http://127.0.0.1:8000/api/v2/activities?group=5
```

```json
[
  {
    "error": "O parâmetro (group) deve ser de 1 á 4"
  }
]
```

<br />
<br />

### :negative_squared_cross_mark: Dados não encontrados

Se o grupo pesquisado estiver dentro dos valores permitidos, mas nenhuma dado for encontrado, será retornado uma mensagem infromando o ocorrido.

```text
GET http://127.0.0.1:8000/api/v2/activities?group=4
```

```json
[
  {
    "error": "Não há atividades para o grupo 4"
  }
]
```

<br />
<br />

### :negative_squared_cross_mark: Sem autenticação

```text
GET http://127.0.0.1:8000/api/v2/activities/auth
```

```json
{
  "detail": "Not authenticated"
}
```

<br />
<br />

### :negative_squared_cross_mark: Autenticação inválida

```text
GET http://127.0.0.1:8000/api/v2/activities/auth
```

```json
[
  {
    "error": "Matricula ou senha incorretos"
  }
]
```

<br />
<br />

### :white_check_mark: Dados encontrados

Se o filtro estiver correto e os dados existirem, eles serão retornados no formato abaixo:

```text
GET http://127.0.0.1:8000/api/v2/activities?group=1
```

```json
[
  {
    "date": "21/10/2023 08:00",
    "event": "Curso: Entendendo os demonstrativos contábeis",
    "professor": "Prof. Esp. Osvaldo Luis Gonçalves da Cunha",
    "local": "Sala 203 bloco 5",
    "city": "Bauru",
    "group": 1,
    "hours": 4
  },
  {
    "date": "21/10/2023 08:00",
    "event": "Curso: Entendendo os demonstrativos contábeis",
    "professor": "Prof. Esp. Osvaldo Luis Gonçalves da Cunha",
    "local": "zoom",
    "city": "Bauru/Botucatu",
    "group": 1,
    "hours": 4
  }
]
```

<br />

```text
GET http://127.0.0.1:8000/api/v2/activities/auth

auth = {
  "username": "<seu_RA>"
  "password": "<sua_senha>"
}
```

```json
[  
  {
    "group": 3,
    "event": "Palestra: Perícia para Administradores - Bauru/Online",
    "event_url": "https://portal.ite.edu.br/atividadescomplementares/eventos?atividade=NAC2023%2095",
    "remaining_vacancies": 139
  }
]
```

<br />



