import pandas as pd
from datetime import datetime

class Transformation:
    
    def __init__(self, path: str) -> None:
        self.path = path

    def read_csv(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)
        return df

    def cleaningData(self) -> pd.DataFrame:
        # Adicionar a coluna de origem
        df = self.read_csv()
        df['_source'] = 'https://lista.mercadolivre.com.br/tenis'

        # Adicionar coluna de data da coleta dos dados
        df['_date_collect'] = datetime.now()

        pd.options.display.max_columns = None

        # Alterar tipagens das colunas e tratar valores nulos
        df['old_price'] = df['old_price'].fillna(0).astype(float)
        df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
        df['new_price'] = df['new_price'].fillna(0).astype(float)
        df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)
        df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

        # Retirar parenteses do numero de reviews
        df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]','', regex=True)
        df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

        # Tratar os preços como floats e calcular os valores com os centavos
        df['old_price_product'] = df['old_price'] + df['old_price_cents'] / 100
        df['new_price_product'] = df['new_price'] + df['new_price_cents'] / 100
        df['old_price_product'].astype(float)
        df['new_price_product'].astype(float)

        # Remover ass colunas com preços separados
        df.drop(columns=['old_price','old_price_cents','new_price','new_price_cents'], inplace=True)

        return df