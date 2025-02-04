install:
	pip install -r requirements.txt

run-scrap:
	cd src/collect/collect && \
	scrapy crawl mercadolivre -o ../../data/data.csv

run-transformation:
	python3 src/transformation/main.py

venv:
	python3 --version && python3 -m venv venv

dashboard:
	streamlit run src/dashboard/app.py
