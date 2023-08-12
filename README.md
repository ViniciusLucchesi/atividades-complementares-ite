<div align="center">

<div class="img-bg">
  <img src="assets/ite_logo.svg" width="100" height="100" alt="ITE Logo svg">
</div>

# Atividades Complementares

![programming_language](https://img.shields.io/badge/python-3.10.12-yellow) &nbsp;
![fastapi](https://img.shields.io/badge/fastapi-0.100.0-success) &nbsp;
![pandas](https://img.shields.io/badge/pandas-2.0.3-blue)

API que coleta e disponibiliza informações sobre as atividades complementares da faculdade. 

Coletados via `Web Scraping` e disponibilizados no formato `JSON`


[Versões](#pushpin-versões) &nbsp; • &nbsp; [Rotas](#telescope-rotas) &nbsp; • &nbsp; [Modelos](#book-modelos)

<br/>
<br/>

</div>

# :pushpin: Versões

Ambas as versões possuem o mesmo objetivo, mas utilizam métodos diferentes para alcaça-lo.

## Métodos

- **Versão 1:** 
  - Realiza o `web scraping` de maneira manual, utilizando as bibliotecas `httpx`, `selectolax`.
  - Faz toda a formatação dos dados também de maneira manual.
<br/>

- **Versão 2:** 
    - Realiza o `web scraping` de maneira automática, utilizando a função `read_html` da biblioteca `pandas`.
    - Faz toda a formatação dos dados utlizando a biblioteca `pandas`.

<br/>
<br/>

# :telescope: Rotas

## :traffic_light: API - V1

```text
http://127.0.0.1:8000/api/v1/activities
```

Filtros que podem ser aplicados:

- `http://127.0.0.1:8000/api/v1/activities?group={int}`
- `http://127.0.0.1:8000/api/v1/activities?sorted={asc|desc}`


### :bookmark_tabs: group

O parâmetro `group` pode ser utilizado para retornar somente as atividades atribuídas ao grupo especificado. Podendo receber como valor somente números inteiros entre 1 e 4.

### :bookmark_tabs: sorted

O parâmetro `sorted` pode ser utilizado para retornar os dados de maneira ordenada através da quantidade de horas oferecidas por cada atividade, podendo receber os parâmetros:

 - **asc** => Ordenação `crescente`
 - **desc** => Ordenação `decrescente`

## :book: Combinações

Os parâmetros `group` e `sorted` podem ser combinados para retornarem informações mais relevantes com base no que você está procurando.

<br/>

## :traffic_light: API - V2

```text
http://127.0.0.1:8000/api/v2/activities
```

Filtros que podem ser aplicados

- `http://127.0.0.1:8000/api/v2/activities?group={int}`

### :bookmark_tabs: group

O parâmetro `group` pode ser utilizado para retornar somente as atividades atribuídas ao grupo especificado. Podendo receber como valor somente números inteiros entre 1 e 4.

### :bookmark_tabs: sorted

Por padrão essa rota já ordena os objetos retornados de maneira `decrescente` com base na quantidade de horas complementares que serão ganhas ao participar da atividade.


<br/>
<br/>

# :mailbox: Modelos

## :ticket: Modelo de retorno - V1

```json
[
    {
        "date": "%d/%m/%Y %H:%M",
        "event": "str",
        "professor": "str",
        "observation": "str",
        "location": "str",
        "online": true,
        "hours": 0,
        "group": 0
    }
]
```

## :ticket: Modelo de retorno - V2

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


<br/>
<br/>

## :beginner: Retornos

### :negative_squared_cross_mark: Filtro inválido

Se o usuário utilizar o filtro para buscar um grupo específico, mas o número passado como parâmetro for diferente dos valores de 1 a 4, será retornado o seguinte `json`:

```text
GET http://127.0.0.1:8000/api/{v1|v2}/activities?group=5
```

```json
[
  {
    "error": "O parâmetro (group) deve ser de 1 á 4"
  }
]
```

<br/>
<br/>

### :negative_squared_cross_mark: Dados não encontrados

Se o grupo pesquisado estiver dentro dos valores permitidos, mas nenhuma dado for encontrado, será retornado uma mensagem infromando o ocorrido.

```text
GET http://127.0.0.1:8000/api/{v1|v2}/activities?group=4
```

```json
[
  {
    "error": "Não há atividades para o grupo 4"
  }
]
```

<br/>
<br/>

### :white_check_mark: Dados encontrados

Se o filtro estiver correto e os dados existirem, eles serão retornados no formato abaixo:


#### Versão 1

```text
GET http://127.0.0.1:8000/api/v1/activities?group=1
```

```json
[
  {
    "date": "21/10/2023 08:00",
    "event": "Curso: Entendendo os demonstrativos contábeis - Bauru/Presencial",
    "professor": "Prof. Esp. Osvaldo Luis Gonçalves Da Cunha",
    "observation": "Público alvo: todos os alunos do CEUB e comunidade - Grupo 1: 4h",
    "location": "Sala 203 bloco 5",
    "online": false,
    "hours": 4,
    "group": 1
  },
  {
    "date": "21/10/2023 08:00",
    "event": "Curso: Entendendo os demonstrativos contábeis - Bauru/Online",
    "professor": "Prof. Esp. Osvaldo Luis Gonçalves Da Cunha",
    "observation": "Público alvo: todos os alunos do CEUB e comunidade - Grupo 1: 4h - ; O Acesso remoto à sala de aula deve ser feito utilizando o NOME COMPLETO e RA.",
    "location": "Bauru - zoom",
    "online": true,
    "hours": 4,
    "group": 1
  },
  {
    "date": "21/10/2023 08:00",
    "event": "Curso: Entendendo os demonstrativos contábeis - Botucatu/Online",
    "professor": "Prof. Esp. Osvaldo Luis Gonçalves Da Cunha",
    "observation": "Público alvo: todos os alunos FAIB e comunidade - Grupo 1: 4h - ; O Acesso remoto à sala de aula deve ser feito utilizando o NOME COMPLETO e RA.",
    "location": "Botucatu - zoom",
    "online": true,
    "hours": 4,
    "group": 1
  }
]
```

<br/>

#### Versão 2

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

<br/>
