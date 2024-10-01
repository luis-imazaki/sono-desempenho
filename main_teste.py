import csv
from pathlib import Path
import pandas as pd


# Exemplo de caminho relativo usando pathlib
csv_path = Path(__file__).parent / 'include' / 'dados.csv'
csv_path_out = Path(__file__).parent / 'resultados' / 'resultados.csv'

# Conjunto para rastrear valores únicos de row[2]
valores_unicos = set()
cargas = {}
pesos = {}
horarios1 = ["07:15:00","07:00:00","05:00:00","06:00:00"]
horarios2 = []
horarios3 = []
horarios4 = []
horarios5 = []
horarios6 = []
# Abrindo o arquivo de entrada para leitura
with csv_path.open('r', encoding='utf-8') as file_in:
    reader = csv.reader(file_in)
    
    # Abrindo o arquivo de saída para escrita
    with csv_path_out.open('w', newline='', encoding='utf-8') as file_out:
        writer = csv.writer(file_out)
        cont = 0
        for row_in in reader:
           cont += 1
           # Verifica o semestre do ano e o curso
           if row_in[6] == "2010/1" and row_in[0] == 'ANÁLISE DE SISTEMAS - BACHARELADO':
                
                # Combina os valores que não podem se repetir  (RGA, Ano/Semestre, disciplina, curso) 
                combinacao = (row_in[6], row_in[7], row_in[0], row_in[1], row_in[2])
                
                # Saida com os dados relevantes 
                 

                # Se row não existir no arquivo de saída, escreve o novo
                if combinacao not in valores_unicos:
                    carga = 1
                    cargas[combinacao] = carga
                    if row_in[9] in horarios1:
                        pesos[combinacao] = 1
                    if row_in[9] in horarios2: #precisa ver como serão feitas as
                        pesos[combinacao] = 2 #distribuicoes de carga
                    if row_in[9] in horarios3:
                        pesos[combinacao] = 3
                    if row_in[9] in horarios4:
                        pesos[combinacao] = 4
                    if row_in[9] in horarios5:
                        pesos[combinacao] = 5
                    if row_in[9] in horarios6:
                        pesos[combinacao] = 6
                    saida = row_in[0:3] + row_in[6:13] + carga
                    writer.writerow(saida)
                    
                    valores_unicos.add(combinacao)
                # Se existir, só pega o horário da disciplina e o nome dela
                else:
                    cargas[combinacao] +=1
                    if row_in[9] in horarios1:
                        pesos[combinacao] += 1
                    if row_in[9] in horarios2: #precisa ver como serão feitas as
                        pesos[combinacao] += 2 #distribuicoes de carga
                    if row_in[9] in horarios3:
                        pesos[combinacao] += 3
                    if row_in[9] in horarios4:
                        pesos[combinacao] += 4
                    if row_in[9] in horarios5:
                        pesos[combinacao] += 5
                    if row_in[9] in horarios6:
                        pesos[combinacao] += 6
                    peso_calculado = pesos[combinacao] / carga[combinacao]
                    writer.writerow(row_in[7:11] + carga + peso_calculado)

# Removendo linhas duplicadas dos horários        

df = pd.read_csv(csv_path_out)
df_sem_duplicatas = df.drop_duplicates()
df_sem_duplicatas.to_csv(csv_path_out, index=False)