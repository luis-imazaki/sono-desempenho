import csv
from pathlib import Path

csv_path = Path("include/dados.csv") #entrada 
csv_saida = Path("resultados/ciencia20232.csv") #saida

sem_repetição = set()
cursos = ['engenharia de computação','ciência da computação','engenharia de software','sistemas de informação','ANÁLISE DE SISTEMAS - BACHARELADO'] 

with open(csv_path, "r", encoding='utf-8') as linha:
    reader = csv.reader(linha)
    with open(csv_saida, "a", newline='', encoding='utf-8') as linhas_saida:
        writer = csv.writer(linhas_saida)
        for row in reader:  # Percorre as linhas do arquivo CSV
            if  row[0] == "Ciência da Computação" and row[6] == "2023/2" and row[8] != "EAD":
                writer.writerow(row)