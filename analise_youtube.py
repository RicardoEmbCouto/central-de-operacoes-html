#Aprendendo a Programar com Inteligencia artificial me ensinando!

#Passo 01: Importar a biblioteca Pandas, que é a nossa principal ferramenta

import pandas as pd

#Passo 02: Inserir os dados do video xx em uma estrutura de dicionario.

#Inserimos os dados que informamos para inteligencia artificial anteriormente para comparação

dados_video_1 = {
        'Video_ID': [1],
        'Titulo': ['Reserva de Emergencia: O guia completo'],
        'Visualizacoes': [7],
        'Impressoes': [4],
        'Inscritos_Ganhos': [1],
        'Duracao_Total_Segundos': [280], # 4 minutos e 40 segundos
        'Duracao_Media_Segundos': [86]   # 1 minuto  e 26 segundos
        }
# Passo 03: Criar o DataFrame a partir do dicionario.

df_videos = pd.DataFrame(dados_video_1)

#Passo 04: Engenharia de Metricas - Calcular nossos KPIs de qualidade.
#Formula: (Duração Média / Duração Total) * 100

df_videos['Retencao_Percentual'] = (df_videos['Duracao_Media_Segundos'] / df_videos['Duracao_Total_Segundos']) * 100

# Fórmula: (Inscritos Ganhos / Visualizações) * 100

df_videos['Conversao_Inscritos_Percentual'] = (df_videos['Inscritos_Ganhos'] / df_videos['Visualizacoes']) * 100

# --- APRESENTAÇÃO DO RELATÓRIO ---

print("="*60)
print("Relatório de Performance de Vídeos - Canal Mapa das Rendas")
print("="*60)

# Itera sobre cada vídeo no nosso DataFrame (atualmente, apenas um)
for index, video in df_videos.iterrows():
    print(f"\nAnalisando o vídeo: '{video['Titulo']}'")
    print("-" * 50)
    print(f"Visualizações: {video['Visualizacoes']}")
    print(f"Novos Inscritos: {video['Inscritos_Ganhos']}")

# Apresenta as métricas calculadas com formatação
    print(f"Retenção Média da Audiência: {video['Retencao_Percentual']:.2f}%")
    print(f"Taxa de Conversão para Inscritos: {video['Conversao_Inscritos_Percentual']:.2f}%")
    print("-" * 50)

# Adiciona uma análise qualitativa, assim como eu faria em um relatório.
    print("\n[Análise Estratégica de JARVIS]")
    if video['Retencao_Percentual'] >= 30:
        print("  [SINAL POSITIVO] A retenção de audiência está em um nível saudável.")
    else:
        print("  [PONTO DE ATENÇÃO] A retenção está abaixo da meta de 30%.")

    if video['Conversao_Inscritos_Percentual'] > 5: # Um valor alto como exemplo
        print("  [SINAL EXCELENTE] A taxa de conversão para inscritos é muito forte.")
    else:
        print("  [INFO] A taxa de conversão para inscritos é um ponto a ser monitorado.")
    print("\n")

print("="*60)
print("Fim do Relatório.")
print("="*60)
