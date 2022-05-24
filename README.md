# Projeto Análise de Imóveis
<img src ='https://user-images.githubusercontent.com/71283631/153653859-ef94ab73-aa6f-4b28-94ce-5a091803bf4e.jpeg' height=280>


O objetivo desse projeto é buscar informações sobre imóveis que estão para alugar e que estão á venda na cidade de São Paulo. As informações serão reunidas atráves de um web scraping e depois serão tratadas, armazenadas para uma análise mais aprofundada para novos insights e desenvolver dashboards.
### Pré requisitos
São necessários alguns softwares para rodar a aplicação:
* Python 3.x
* bibliotecas Python
### Pacotes necessários
* Pandas - Biblioteca para análise de dados
* Scrapy - Framework python para WebCrawling
* mysql-connector-python - Para acessar o MySQL pelo Python

## Parte 1 Web Scraping:
Web scraping é uma coleta de dados de sites da web, onde são usados scripts para "raspar" informações destes sites e que poderão ser usadas para análises futuras.
O site do <a href='https://www.olx.com.br/'>Olx</a> foi utilizado para realizar o scraping.<br>
Nessa parte o dados foram armazenados na forma que foram adquiridos, ou seja, na sua forma "crua" e sem nenhum tratamento. Esse tratamento será realizado posteriormente.<br>
### Rodando o script do scraping
O script grava os dados no Banco de Dados MySQL.
Vamos rodar o script para fazer o scraping para obter dados de imóveis á venda e alugados na cidade de São Paulo:
#### Para rodar o script:

Antes de rodar o script é preciso colocar suas credencias do banco de dados no script do pipeline:<br>
<br>
<a href='https://github.com/SMarkus27/Projeto_Imoveis_SP/blob/main/imoveis/pipelines.py'>Arquivo Pipeline</a><br>
```
cd scrapping/imoveis
```
```
python -m scrapy crawl olx
```
## Parte 2 Tratamento dos Dados:
Abaixo teremos os comandos SQL realizados para o tratamento dos dados, poderia ter usado o python para realizar esse tratamento, mas vamos deixar o python para ser usado no EDA dos dados. 
* Vamos manter somente os dados relacionados com Apartamentos e Casas:
```
DELETE FROM olx_crawl
WHERE olx_crawl.category not in ('Apartamentos', 'Casas')
```
