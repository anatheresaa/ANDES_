#################### Bibliotecas e Módulos ####################
# Fazer os imports necessários
import pandas as pd
import plotly.express as px
import streamlit as st

#################### Configurações da página do Streamlit ####################
st.set_page_config(page_title='Relatório de 20/12/2024', layout='wide', page_icon='📊')

#################### Título da página do Streamlit ####################
st.markdown('# Relatório de Respostas - 20/12/2024')

#################### Leitura e Tratamento dos Dados ####################
# Ler os dados originais
grafico_ativos_totais_df = pd.read_csv('tabela_ativos_totais_20_12.csv')

# Excluindo a última coluna
grafico_ativos_totais_df = grafico_ativos_totais_df.drop(columns=grafico_ativos_totais_df.columns[-1])

# Filtrar as respostas completos
grafico_ativos_completos_df = pd.read_csv('tabela_ativos_completos_20_12.csv')
grafico_ativos_completos_df = grafico_ativos_completos_df.drop(columns=grafico_ativos_completos_df.columns[-1])
# Filtrar as respostas incompletos
grafico_ativos_incompletos_df = pd.read_csv('tabela_ativos_incompletos_20_12.csv')
grafico_ativos_incompletos_df = grafico_ativos_incompletos_df.drop(columns=grafico_ativos_incompletos_df.columns[-1])
#################### Layout do Streamlit ####################
# Criar e nomear as tabs (abas) 
tab_1, tab_2, tab_3, tab_4 = st.tabs(['Métricas', 'Respostas Totais', 'Respostas Completas', 'Respostas Incompletas'])

# Preencher a tab 1 (Relatório Geral)
with tab_1:
        # Criar as métricas gerais
        with st.container():
                st.title('Métricas Gerais')
                col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
                
                # Criar a métrica de restaurantes registrados
                with col_1:
                        col_1.metric('Respostas Totais:', 4525)
                        
                # Criar a métrica de países registrados
                with col_2:
                        col_1.metric('Respostas completos:', 2872)
                        
                # Criar a métrica de cidades registrados
                with col_3:
                        col_1.metric('Respostas Incompletos:', 1653)
                        
                # Criar a métrica do total de avaliações feitas
                with col_4:
                        col_1.metric('Instituições de Ensino Citadas:', 140)

        # Criar as métricas semenais
        with st.container():
                st.title('Crescimento Semanal (17/12/2024 a 20/12/2024)')
                col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
                
                # Criar a métrica de restaurantes registrados
                with col_1:
                        col_1.metric('Respostas Totais:', 465)
                        
                # Criar a métrica de países registrados
                with col_2:
                        col_1.metric('Respostas completos:', 305)
                        
                # Criar a métrica de cidades registrados
                with col_3:
                        col_1.metric('Respostas Incompletos:', 160)
                        
                # Criar a métrica do total de avaliações feitas
                with col_4:
                        col_1.metric('Instituições de Ensino Citadas:', 2)
                        
# Preencher a tab 2 (Respostas Totais)
with tab_2:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_totais_df, x='UF', y='Contagem', color='Instituição de ensino',
                labels = {'UF':'UF', 'Contagem':'Respostas totais',
                        'Instituição de ensino':'Instituição de Ensino'},
                title='Respostas Totais por UF e Instituição de Ensino (20/12/2024) - Ativos')
    fig.update_yaxes(tick0=0, dtick=10)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Totais')
    tabela_ativos_totais_df = pd.read_csv('tabela_ativos_totais_20_12.csv')
    tabela_ativos_totais_df.drop(columns=tabela_ativos_totais_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_totais_df, use_container_width=True) 
       
# Preencher a tab 3 (Respostas completos)
with tab_3:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_completos_df, x='UF', y='Contagem', color='Instituição de ensino',
                labels = {'UF':'UF', 'Contagem':'Respostas completos',
                        'Instituição de ensino':'Instituição de ensino'},
                title='Respostas completos por UF e Instituição de Ensino (20/12/2024) - Ativos')
    fig.update_yaxes(tick0=0, dtick=10)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas completos')
    tabela_ativos_completos_df = pd.read_csv('tabela_ativos_completos_20_12.csv')
    tabela_ativos_completos_df.drop(columns=tabela_ativos_completos_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_completos_df, use_container_width=True) 
       
# Preencher a tab 4 (Respostas Incompletos)
with tab_4:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_incompletos_df, x='UF', y='Contagem', color='Instituição de ensino',
                labels = {'UF':'UF', 'Contagem':'Respostas incompletos',
                        'Instituição de ensino':'Instituição de ensino'},
                title='Respostas Incompletos por UF e Instituição de Ensino (20/12/2024) - Ativos')
    fig.update_yaxes(tick0=0, dtick=10)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
        
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Incompletos')
    tabela_ativos_incompletos_df = pd.read_csv('tabela_ativos_incompletos_20_12.csv')
    tabela_ativos_incompletos_df.drop(columns=tabela_ativos_incompletos_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_incompletos_df, use_container_width=True)
