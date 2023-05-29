# Projeto

Esse código utiliza da técnica de `web scraping` para coletar os dados das atividades complementares disponíveis da minha faculdade ITE _Instituição Toledo de Ensino_ e retornalos em uma lista de objetos `JSON`.


## Requisição

O scraping retorna uma lista com vários objetos `JSON` contendo todas as atividades complementares disponíveis no site das [atividades complementares](https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis).

```json
[
    {
        "date": "21/10/2023 08:00",
        "event": "Curso: Entendendo os demonstrativos contábeis - Bauru/Presencial",
        "professor": "Prof. Esp. Osvaldo Luis Gonçalves da Cunha",
        "observation": "Público alvo: todos os alunos do CEUB e comunidade - Grupo 1: 4h",
        "location": "Sala 203 bloco 5",
        "hours": 4,
        "group": 1
    }
]
```
