import pandas as pd
from pathlib import Path

# Carregar o arquivo CSV
csv_path = Path(__file__).parent / 'include' / 'dados.csv'
csv_path_out = Path(__file__).parent / 'include' / 'dados_filtrados.csv'
df = pd.read_csv(csv_path)

# Determinar a lista de horários de "Horário Início" que serão usados para filtrar
horarios_iniciais_alvo = ['00:00:00','1:00:00','01:00:00', '02:00:00', '03:00:00','04:00:00','05:00:00'] 

# Encontrar as linhas que têm algum dos "Horário Início" desejados
filtro_horarios = df['Horário Início'].isin(horarios_iniciais_alvo)

# Selecionar as colunas que identificam as combinações que devem ser removidas
colunas_combinar = ['Curso', 'Ano/Semestre Ingresso', 'RGA', 'Ano/Semestre Disciplina', 'Disciplina', 'Média Final', '% Frequência']

# Identificar as combinações de valores a remover
combinações_para_remover = df.loc[filtro_horarios, colunas_combinar].drop_duplicates()

# Realizar a junção (merge) com o DataFrame original, mantendo apenas as linhas que não devem ser removidas
df_filtrado = df.merge(combinações_para_remover, on=colunas_combinar, how='left', indicator=True)

# Manter apenas as linhas que não foram identificadas para remoção
df_filtrado = df_filtrado[df_filtrado['_merge'] == 'left_only']

# Remover a coluna auxiliar criada pelo merge
df_filtrado = df_filtrado.drop(columns=['_merge'])

# Salvar o resultado em um novo arquivo CSV
df_filtrado.to_csv(csv_path_out, index=False)

print(f"Linhas filtradas e o arquivo resultante foi salvo em: {csv_path_out}")
