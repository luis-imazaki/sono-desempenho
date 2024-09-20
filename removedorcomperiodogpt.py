import pandas as pd
import re
from pathlib import Path

csv_path = Path("include/dados.csv")

# Função para corrigir e classificar os horários
def classificar_periodo(horario_inicio):
    try:
        # Remover espaços em branco
        horario_inicio = horario_inicio.strip()
        
        # Corrigir o formato para remover segundos e garantir o formato %H:%M
        # Substitui qualquer hora que tenha mais de dois dígitos após o primeiro ":"
        horario_inicio_corrigido = re.sub(r'(\d{1,2}:\d{2}):\d{2}', r'\1', horario_inicio)
        
        # Tentar converter para o formato datetime
        hora = pd.to_datetime(horario_inicio_corrigido, format='%H:%M', errors='coerce').time()
        
        if hora is None:
            return 'Horário Inválido'
        
        # Classificar o horário
        if hora >= pd.to_datetime('05:00', format='%H:%M').time() and hora <= pd.to_datetime('11:59', format='%H:%M').time():
            return 'Manhã'
        elif hora >= pd.to_datetime('12:00', format='%H:%M').time() and hora <= pd.to_datetime('17:59', format='%H:%M').time():
            return 'Tarde'
        else:
            return 'Noite'
    except Exception as e:
        # Retorna 'Horário Inválido' se não for possível processar
        return 'Horário Inválido'

# Carregar o arquivo CSV
df = pd.read_csv(csv_path)

# Verifique se há valores nulos ou vazios em 'Horário Início' e substitua-os por um valor padrão ou trate-os de acordo
df['Horário Início'].fillna('00:00', inplace=True)

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

# Aplicar a função de classificação nos horários
df_sem_duplicatas['Período'] = df_sem_duplicatas['Horário Início'].apply(classificar_periodo)

# Manter as colunas relevantes e descartar 'Horário Início' e 'Horário Fim'
df_resultante = df_sem_duplicatas[['Curso', 'Ano/Semestre Ingresso', 'RGA', 'Nome Aluno', 'Sexo', 'Data Nascimento', 
                                   'Ano/Semestre Disciplina', 'Disciplina', 'Dia da Semana', 
                                   'Período', 'Média Final', '% Frequência', 'Situação Final']]

# Salvar o resultado em um novo arquivo CSV
df_resultante.to_csv('arquivo_sem_duplicatas_com_periodo.csv', index=False)