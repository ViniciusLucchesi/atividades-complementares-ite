# :confused: Como rodar o projeto?

```text
ATENÇÃO

Nesta prévia entende-se que você já tem o Python e o PIP instalados e configurados na sua máquina
```

Tendo baixado esse repositório rode os comandos abaixo na ordem em que estão aparecendo para a correta instalação das dependências e inicialização do `web scraping`

>Linux e MacOS
>```bash
>python3 -m venv env
>```
>
>```bash
>source env/bin/activate
>```

> Windows
> ```bash
> python -m venv env
> ```
>
> ```bash
> .env/Scripts/activate
> ```

Os comandos `python3 -m venv env` e `python -m venv env` serão responsáveis por criar um ambiente virtual do python, ele será representado na estrutura do projeto como uma pasta chamada `env`, que foi o nome digitado no comando. _(podendo ser o nome que você quiser)_

Já os comandos `source env/bin/activate` e `.env/Scripts/activate` são utilizados para acessar o seu ambiente virtual do Python, dessa meneira o seu projeto não fica sobrecarregado com bibliotecas que você tenha utilizado em outros projetos.

Após acessar seu ambiente virtual, que pode ser identificado com um `(env)` antes do caminho do seu respositório na linha de comando, basta rodar o código abaixo para instalar todas as bibliotecas que foram utilizadas no projeto

```bash
pip install -r requirements.txt
```

Tendo terminado a instalação você já estará pronto para rodar o **web scraping**, com o comando abaixo:

> Linux e MacOS
> ```bash
> python3 app.py
> ```

> Windows, Linux e MacOS
> ```bash
> python app.py
> ```

# :neutral_face: Do que se trata?

Este é um projeto pessoal desenvolvido para treinar a prática do **web scraping**, que consiste em coletar de maneira automatizada informações de sites na internet. 

Nesse projeto foi realizada a coleta das **Atividades complementares** que estão disponíveis no [site](https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis) da minha faculdade, a **Instituição Toledo de Ensino - ITE**.

# :sunglasses: Por que utilizá-la?

Ao contrário do que é exibido no site, meu script:
- Retorna os dados no formato `JSON`
- Remove campos repetidos da tabela
- Agrupa campos que não precisavam estar separados
- Permite filtros (de maneira crescente e decrescente) por:
  - Grupos
  - Horas Complementares


# :grin: Como o filtro funciona?

Dentro da função **main** você encontrará uma variável chamada **order** que recebe um dicionário, assim como o exibido abaixo:

```python
order = {'element': 'hours', 'reverse': False}
```

Com base nessa especificação do dicionário o **scraping** retornará os dados encontrados, exibindo no terminal de maneira crescente, ou seja, da atividade que oferece o menor número de horas complementares para a atividade que oferece o maior número de horas complementares.

Você pode alterar de `hours` para `group`, permitindo que o **scraping** retorne os dados filtrando do **Grupo 1** ao **Grupo 4**.

Mas também é possível alterar o valor do campo `reverse` de `False` para `True`, permitindo que o filtro seja realizado na ordem **Decrescente**, ou seja, do maior para o menor.

# :hushed: Retorno do Scraping

```json
[    
    {
        "date": "05/08/2023 08:00",
        "event": "Curso 5S – Housekeeping - Comportamento e base para a Melhoria Contínua e Prática da Qualidade - Botucatu/Online",
        "professor": "Prof. Dr. Francisco José Lampkowski",
        "observation": "Público alvo: todos os alunos FAIB e comunidade – Grupo 1: 10 horas – O curso será realizado em dois encontros: 05/08 e 
12/08/2023",
        "location": "Botucatu - zoom",
        "hours": 10,
        "group": 1
    },
    {
        "date": "01/07/2023 07:00",
        "event": "Visita Técnica: Feira de Franquias Associação Brasileira de Franquias-ABF",
        "professor": "Prof. Dr. José Ricardo Scareli Carrijo",
        "observation": "Público alvo: alunos do curso de Administração do CEUB - Grupo 3: 12h – Os alunos interessados devem procurar o 
coordenador do curso de Administração Prof. Dr. José Ricardo Scareli Carrijo",
        "location": "Presencial",
        "hours": 12,
        "group": 3
    }
]
```

Como pode ser observado o retorno desse **scraping** é em formato de `array` contendo os objetos `JSON` extraídos do `HTML` da página da faculdade.