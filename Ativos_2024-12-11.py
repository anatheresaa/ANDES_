#################### Bibliotecas e Módulos ####################
# Fazer os imports necessários
import pandas as pd
import plotly.express as px
import streamlit as st

#################### Configurações da página do Streamlit ####################
st.set_page_config(page_title='Relatório de 11/12/2024', layout='wide', page_icon='📊')

#################### Título da página do Streamlit ####################
st.markdown('# Relatório de Respostas - 11/12/2024')

#################### Leitura e Tratamento dos Dados ####################
# Ler os dados originais
grafico_ativos_totais_df = pd.read_csv('tabela_ativos_totais_11_12.csv')

# Excluindo a última coluna
grafico_ativos_totais_df = grafico_ativos_totais_df.drop(columns=grafico_ativos_totais_df.columns[-1])


# Filtrar as respostas completas
grafico_ativos_completas_df = pd.read_csv('tabela_ativos_completos_11_12.csv')
grafico_ativos_completas_df = grafico_ativos_completas_df.drop(columns=grafico_ativos_completas_df.columns[-1])
# Filtrar as respostas incompletas
grafico_ativos_incompletas_df = pd.read_csv('tabela_ativos_incompletos_11_12.csv')
grafico_ativos_incompletas_df = grafico_ativos_incompletas_df.drop(columns=grafico_ativos_incompletas_df.columns[-1])
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
                        col_1.metric('Respostas Totais:', 408)
                        
                # Criar a métrica de países registrados
                with col_2:
                        col_1.metric('Respostas Completas:', 208)
                        
                # Criar a métrica de cidades registrados
                with col_3:
                        col_1.metric('Respostas Incompletas:', 200)
                        
                # Criar a métrica do total de avaliações feitas
                with col_4:
                        col_1.metric('Instituições de Ensino Citadas:', 61)

        # Criar as métricas semenais
        with st.container():
                st.title('Crescimento Semanal (03/12/2024 a 11/12/2024)')
                col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
                
                # Criar a métrica de restaurantes registrados
                with col_1:
                        col_1.metric('Respostas Totais:', 40)
                        
                # Criar a métrica de países registrados
                with col_2:
                        col_1.metric('Respostas Completas:', 16)
                        
                # Criar a métrica de cidades registrados
                with col_3:
                        col_1.metric('Respostas Incompletas:', 34)
                        
                # Criar a métrica do total de avaliações feitas
                with col_4:
                        col_1.metric('Instituições de Ensino Citadas:', 4)
                        
# Preencher a tab 2 (Respostas Totais)
with tab_2:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_totais_df, x='UF', y='Respostas Incompletas', color='Instituição de Ensino',
                labels = {'UF':'UF', 'Respostas Incompletas':'Respostas totais',
                        'Instituição de Ensino':'Instituição de Ensino'},
                title='Respostas Totais por UF e Instituição de Ensino (11/12/2024) - ativos Não-ativos')
    fig.update_yaxes(tick0=0, dtick=10)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Totais')
    tabela_ativos_totais_df = pd.read_csv('tabela_ativos_totais_11_12.csv')
    tabela_ativos_totais_df.drop(columns=tabela_ativos_totais_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_totais_df, use_container_width=True) 
       
# Preencher a tab 3 (Respostas Completas)
with tab_3:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_completas_df, x='UF', y='Respostas Incompletas', color='Instituição de Ensino',
                labels = {'UF':'UF', 'Respostas Incompletas':'Respostas completas',
                        'Instituição de Ensino':'Instituição de ensino'},
                title='Respostas Completas por UF e Instituição de Ensino (11/12/2024) - ativos Não-ativos')
    fig.update_yaxes(tick0=0, dtick=10)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Completas')
    tabela_ativos_completas_df = pd.read_csv('tabela_ativos_completos_11_12.csv')
    tabela_ativos_completas_df.drop(columns=tabela_ativos_completas_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_completas_df, use_container_width=True) 
       
# Preencher a tab 4 (Respostas Incompletas)
with tab_4:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_incompletas_df, x='UF', y='Respostas Incompletas', color='Instituição de Ensino',
                labels = {'UF':'UF', 'Respostas Incompletas':'Respostas incompletas',
                        'Instituição de Ensino':'Instituição de ensino'},
                title='Respostas Incompletas por UF e Instituição de Ensino (11/12/2024) - ativos Não-ativos')
    fig.update_yaxes(tick0=0, dtick=10)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
        
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Incompletas')
    tabela_ativos_incompletas_df = pd.read_csv('tabela_ativos_incompletos_11_12.csv')
    tabela_ativos_incompletas_df.drop(columns=tabela_ativos_incompletas_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_incompletas_df, use_container_width=True)
