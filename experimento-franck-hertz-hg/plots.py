import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import argrelextrema

# Ler os dados do arquivo CSV
data = pd.read_csv('data180_2.csv')

# Encontrar os mínimos locais
minima = argrelextrema(data['U/V'].values, np.less)
minima = minima[0]  # extrair o array de índices da tupla

# Criar um DataFrame com os mínimos locais
minima_df = data.loc[minima]

# Salvar os mínimos locais em um arquivo CSV
minima_df.to_csv('minima.csv', index=False)

# Plotar os dados
plt.figure(figsize=(10,5))
plt.plot(data['U/V.1'], data['U/V'], label='U/V')
plt.scatter(data['U/V.1'][minima], data['U/V'][minima], color='red')  # plotar os mínimos locais
plt.xlabel('U/V.1')
plt.ylabel('U/V')
plt.title('Data from data180_2.csv')
plt.legend()
plt.show()