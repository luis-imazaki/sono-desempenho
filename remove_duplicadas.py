import pandas as pd
from pathlib import Path

# Carregar o arquivo CSV
csv_path = Path("include/dados.csv")
df = pd.read_csv(csv_path)

# Remover duplicatas com base nas colunas especificadas
df_sem_duplicatas = df.drop_duplicates(subset=[
    'Curso', 
    'Ano/Semestre Ingresso', 
    'RGA', 
    'Data Nascimento', 
    'Ano/Semestre Disciplina', 
    'Disciplina', 
    'Média Final'
])

# Manter o Horário Início e Fim
df_resultante = df_sem_duplicatas[['Curso', 'Ano/Semestre Ingresso', 'RGA', 'Nome Aluno', 'Sexo', 'Data Nascimento', 
                                   'Ano/Semestre Disciplina', 'Disciplina', 'Dia da Semana', 
                                   'Horário Início', 'Horário Fim', 'Média Final', '% Frequência', 'Situação Final']]

# Salvar o resultado em um novo arquivo CSV
df_resultante.to_csv('arquivo_sem_duplicatas.csv', index=False)