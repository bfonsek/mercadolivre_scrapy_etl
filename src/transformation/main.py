import pandas as pd
import  sqlite3
from transformation import Transformation

transform = Transformation('data/data.csv')

df = transform.cleaningData()

conn = sqlite3.connect('data/quotes.db')

df.to_sql('mercadolibre_itens', conn, if_exists='replace', index=False)

conn.close()

