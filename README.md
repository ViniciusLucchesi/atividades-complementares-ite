# :confused: Como rodar o projeto?

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
> venv/Scripts/activate
> ```

Os comandos `python3 -m venv env` e `python -m venv env` serão responsáveis por criar um ambiente virtual do python que você tem instalado em seu computador, ele será representado na estrutura do projeto como uma pasta chamada `env`, que foi o nome digitado no comando. _(podendo ser o nome que você quiser)_

Já os comandos `source env/bin/activate` e `venv/Scripts/activate` são utilizados para acessar o seu ambiente virtual do Python, dessa meneira o seu projeto não fica sobrecarregado com bibliotecas que você tenha utilizado em outros projetos.

Após acessar seu ambiente virtual, que pode ser identificado com um `(env)` antes do caminho do seu respositório na linha de comando, basta rodar o código abaixo para instalar todas as bibliotecas que foram utilizadas no projeto

```bash
pip install requirements.txt
```

Tendo terminado a instalação você já estará pronto para rodar o **web scraping**, podendo utilizar o comando a seguir:

> Windows, Linux e MacOS
> ```bash
> python app.py
> ```

# :neutral_face: Do que se trata?

Este é um projeto pessoal desenvolvido para treinar a prática do **web scraping**, que consiste em coletar de maneira automatizada informações de sites na internet. 

Nesse projeto foi realizada a coleta das **Atividades complementares** que estão disponíveis no site da faculdade.

# :sunglasses: Por que utilizá-la?

Ao contrário do que é exibido no site, meu script:
- Agrupa o **dia** e o **horário** melhorando a visibilidade da **data**
- Permite filtros (de maneira crescente e decrescente):
  - Grupos
  - Horas Complementares


# :grin: Como o filtro funciona?

Dentro da função **main** você encontrará uma variável chamada **order** que recebe um dicionário, assim como o exibido abaixo:

```python
order = {'element': 'hours', 'reverse': False}
```

Com base nessa especificação do dicionário o **scraping** retornará os dados encontrados exibindo no terminal da atividade com menor número de horas complementares oferecidas para a atividade com o maior número.

Você pode alterar de `hours` para `group`, permitindo que o **scraping** retorne os dados filtrando do **Grupo 1** ao **Grupo 4**.

Mas também é possível alterar o valor do campo `reverse` de `False` para `True`, permitindo que o filtro seja realizado na ordem **Decrescente**.