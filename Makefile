install:
	pip install -r requirements.txt

run-etl:
	cd src/collect/collect && \
	scrapy crawl mercadolivre -o ../data/data.csv

venv:
	python3 --version && python3 -m venv venv

dash:
	streamlit run dashboard/app.py

