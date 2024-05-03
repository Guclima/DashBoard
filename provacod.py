# -*- coding: utf-8 -*-
"""ProvaCod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VB0QcI0dPGIwv3LiIIlamCsJC8SOCGBa
"""

import pandas as pd
caminho_arquivo = '/content/sample_data/Prova.csv'

dados = pd.read_csv(caminho_arquivo)
dados.head()

dados.info()

dados = dados.drop(columns=['ED'])
dados = dados.drop(columns=['Unnamed: 5'])
dados = dados.drop(columns=['Unnamed: 6'])
dados = dados.drop(columns=['CAMPUS DA CARGA'])
dados = dados.drop(columns=['NÚMERO DE SÉRIE'])
dados.head()

dados_agrupados = dados[['STATUS', 'DESCRICAO', 'ESTADO DE CONSERVAÇÃO']]
dados_agrupados