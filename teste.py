import csv
from pathlib import Path
from datetime import datetime

csv_path = Path(__file__).parent / 'include' / 'dados_filtrados.csv'
horarios = set()
lista = []
with csv_path.open('r', encoding='utf-8') as file_in:
    reader = csv.reader(file_in)
    for row_in in reader:
        if row_in[9] not in horarios:
            horarios.add(row_in[9])
horarios.remove("Horário Início")

for horario in horarios:
    print(horario)
    