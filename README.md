# :confused: Como rodar o projeto?

```text
ATENÇÃO

Nesta prévia entende-se que você já tem o Python e o PIP instalados e configurados na sua máquina
```

Tendo baixado esse repositório rode os comandos abaixo na ordem em que estão aparecendo para a correta instalação das dependências e inicialização do `web scraping`

>Linux e MacOS
>```bash
>python3 -m venv .venv
>```
>
>```bash
>source .venv/bin/activate
>```

> Windows
> ```bash
> python -m venv .venv
> ```
>
> ```bash
> .venv/Scripts/activate
> ```

Os comandos `python3 -m venv .venv` e `python -m venv .venv` serão responsáveis por criar um ambiente virtual do python, ele será representado na estrutura do projeto como uma pasta chamada `.venv`, que foi o nome digitado no comando. _(podendo ser o nome que você quiser)_

Já os comandos `source .venv/bin/activate` e `.venv/Scripts/activate` são utilizados para acessar o seu ambiente virtual do Python no terminal, permitindo que você instale pacotes e rode scripts python de maneira individual do Python que você tem instalado no seu Sistema Operacional.

Após acessar seu ambiente virtual, que pode ser identificado com um `(.venv)` antes do caminho do seu respositório na linha de comando, basta rodar o código abaixo para instalar todas as bibliotecas que foram utilizadas no projeto

```bash
pip install -r requirements.txt
```

Tendo terminado a instalação você já estará pronto para rodar o **web scraping**, com o comando abaixo:

> Windows, Linux e MacOS
> ```bash
> uvicorn main:app --reload
> ```

O parâmetro `--reload` é deve ser utilizado somente para ambiente de desenvolvimento, pois ele reiniciará a API do FastAPI para cada alteração salva nos arquivos deste projeto.

# :neutral_face: Do que se trata?

Este é um projeto pessoal desenvolvido para treinar a prática do **web scraping** e do desenvolvimento de **API's** no framework **FastAPI**. 

Nele foi realizado a coleta das **Atividades complementares** que estão disponíveis no [site](https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis) da minha faculdade, a **Instituição Toledo de Ensino - ITE** através da técnica de **web scraping**. 

Após os dados serem coletados eles são disponibilizados no formato **`JSON`** com rotas que permitem a filtragem dos dados por **grupo** e **ordenação**.

# :sunglasses: Modelo de retorno

```json
{
    "date": "%d/%m/%Y %H:%M",
    "event": "str",
    "professor": "str",
    "observation": "str",
    "location": "str",
    "online": "bool",
    "hours": "int",
    "group": "int"
}
```


# :grin: Rotas da API

Se você observar no arquivo `main.py` verá que só existe uma única rota em nossa API, sendo ela acessada através da URL abaixo:

```text
http://127.0.0.1:8000/api/activities
```

No entanto criamos alguns filtros para o retorno dos dados.

- `http://127.0.0.1:8000/api/activities?group={int}`
- `http://127.0.0.1:8000/api/activities?sorted={asc|desc}`


## :bookmark_tabs: group

O parâmetro `group` pode ser utilizado para retornar somente as atividades atribuídas ao grupo especificado. Podendo receber como valor somente números inteiros.

## :bookmark_tabs: sorted

O parâmetro `sorted` pode ser utilizado para retornar os dados de maneira ordenada através da quantidade de horas oferecidas por cada atividade, podendo receber os parâmetros:

 - **asc** => Ordenação `crescente`
 - **desc** => Ordenação `decrescente`

## :book: Combinações

Os parâmetros `group` e `sorted` podem ser combinados para retornarem informações mais relevantes com base no que você está procurando.