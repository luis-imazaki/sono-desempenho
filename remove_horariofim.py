import csv
import pandas as pd
from pathlib import Path
from datetime import datetime

csv_path = Path(__file__).parent / 'include' / 'dados.csv'
csv_path_out = Path(__file__).parent / 'resultados' / 'semhorarioinicio.csv'

df = pd.read_csv(csv_path)


df.drop('Horário Início', axis=1, inplace=True)



df.to_csv(csv_path_out, index=False, header=False) 