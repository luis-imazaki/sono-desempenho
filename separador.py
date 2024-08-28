import csv
from pathlib import Path

csv_path = Path("include/dados.csv") #entrada 
csv_saida = Path("resultados/outros.csv") #saida

sem_repetição = set()
cursos = ['engenharia de computação','ciência da computação','engenharia de software','sistemas de informação']

with open(csv_path, "r", encoding='utf-8') as linha:
    reader = csv.reader(linha)
    with open(csv_saida, "a", newline='', encoding='utf-8') as linhas_saida:
        writer = csv.writer(linhas_saida)
        for row in reader:  # Percorre as linhas do arquivo CSV
            if  cursos[0] not in row[0].lower() and cursos[1] not in row[0].lower() and cursos[2] not in row[0].lower() and cursos[3] not in row[0].lower() :
                writer.writerow(row)