import pandas as pd
import matplotlib.pyplot as plt
 
# Carregar o arquivo CSV
df = pd.read_csv('data.csv')
 
# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['r'], df['q_c'], marker='o', linestyle='')
 
# Adicionar títulos e rótulos
plt.title('Gráfico de q_c em função de r')
plt.xlabel('r')
plt.ylabel('q_c')
 
# Mostrar o gráfico
plt.show()