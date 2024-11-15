import csv
from pathlib import Path
from datetime import datetime

csv_path = Path(__file__).parent / 'include' / 'dados.csv'
horarios = set()

with csv_path.open('r', encoding='utf-8') as file_in:
    reader = csv.reader(file_in)

    for row_in in reader:
        if row_in[10] not in horarios:
            horarios.add(row_in[10])

for horario in horarios:
    print(horario)
    