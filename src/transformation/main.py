import pandas as pd
import  sqlite3
from transformation import Transformation
import logging

transform = Transformation('data/data.csv')

df = transform.cleaningData()

logging.info("Connecting to sqlite databse")
conn = sqlite3.connect('data/quotes.db')

df.to_sql('mercadolibre_itens', conn, if_exists='replace', index=False)

conn.close()

