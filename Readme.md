# Shoes Web Scraping in Mercado Livre

This project aims to scrape information about sneakers sold on the Mercado Livre platform, using the Scrapy library to extract the data, and Streamlit to generate graphics and visualize the information interactively.

## Features

- **Web Scraping with Scrapy**: Collects information about sneakers sold on Mercado Livre, such as price, brand, model, reviews, etc.
- **Analysis and Visualization with Streamlit**: Generates interactive graphs for analyzing extracted data, such as price distribution, brand popularity, etc.
- **Data Export**: Exports collected data in CSV format for further analysis.

## Used Technologies

- **Python 3.9**
- **Scrapy**: Framework for web scraping.
- **Streamlit**: Library for creating interactive web interfaces and graphics.
- **Pandas**: Data manipulation.

## Configuring the environment

### 1. Clone Repository

```bash
git clone https://github.com/bfonsek/mercadolivre_scrapy_etl.git
cd web_scrap_etl
```

### 2. Create Virtual Environment
```bash
Make venv
```

### 3. Install Dependencies
```bash
Make install
```

### 4. Run Scrapping
```bash
Make run-scrap
```

### 5. Run Transformation
```bash
Make run-transformation
```

### 6. Run Dashboard
```bash
Make dashboard
```