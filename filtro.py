import pandas as pd
import csv
from pathlib import Path

# Carregar o arquivo CSV
csv_path = Path(__file__).parent / 'include' / 'dados.csv'
csv_path_out = Path(__file__).parent / 'resultados' / 'resultados1.csv'
df = pd.read_csv(csv_path)

# Determinar o valor de "Horário Início" que será usado para filtrar
horario_inicial_alvo = '1:00:00'  # Exemplo: substitua com o horário alvo

# Encontrar as linhas que têm o "Horário Início" desejado
filtro_horario = df['Horário Início'] == horario_inicial_alvo

# Identificar as combinações de valores que devem ser removidas
combinações_para_remover = df.loc[filtro_horario, ['Curso', 'Ano/Semestre Ingresso', 'RGA', 'Ano/Semestre Disciplina', 'Disciplina', 'Média Final', '% Frequência']]

# Criar um filtro para remover todas as linhas com essas combinações
filtro_remover = df[['Curso', 'Ano/Semestre Ingresso', 'RGA', 'Ano/Semestre Disciplina', 'Disciplina', 'Média Final', '% Frequência']].apply(
    lambda x: (x == combinações_para_remover).all(axis=1).any(), axis=1)

# Remover as linhas correspondentes
df_filtrado = df[~filtro_remover]

# Salvar o resultado em um novo arquivo CSV

df_filtrado.to_csv(csv_path_out, index=False)

print(f"Linhas filtradas e o arquivo resultante foi salvo em: {csv_path_out}")