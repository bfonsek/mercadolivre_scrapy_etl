# Web Scraping de Tênis no Mercado Livre

Este projeto tem como objetivo realizar scraping de informações sobre tênis vendidos na plataforma Mercado Livre, utilizando a biblioteca Scrapy para extrair os dados, e o Streamlit para gerar gráficos e visualizar as informações de forma interativa.

## Funcionalidades

- **Web Scraping com Scrapy**: Coleta informações de tênis vendidos no Mercado Livre, como preço, marca, modelo, quantidade de vendas, avaliações, etc.
- **Análise e Visualização com Streamlit**: Gera gráficos interativos para análise dos dados extraídos, como distribuição de preços, popularidade das marcas, etc.
- **Exportação de Dados**: Exporta os dados coletados em formato CSV para análise adicional.

## Tecnologias Utilizadas

- **Python 3.x**
- **Scrapy**: Framework para web scraping.
- **Streamlit**: Biblioteca para criação de interfaces web interativas e gráficos.
- **Pandas**: Manipulação de dados.

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/bfonsek/mercadolivre_scrapy_etl.git
cd web_scrap_etl
```

### 2. Criar ambiente virtual
```bash
Make venv
```

### 3. Instalar Dependencias
```bash
Make install
```

### 4. Executar Scrapping
```bash
Make run-scrap
```

### 5. Executar Transformacao
```bash
Make run-transformation
```

### 6. Executar Dashboard
```
Make dashboard
```