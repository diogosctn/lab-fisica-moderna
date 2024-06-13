import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados do arquivo CSV
data = pd.read_csv('data_exp2.csv')

# Plotar os dados
plt.figure(figsize=(10,5))
plt.plot(data['VGC'], data['I(microAmpere)'], label='I(microAmpere)')  # note o espaço antes do 'I'
plt.xlabel('VGC')
plt.ylabel('I')
plt.title('Data from data_exp2.csv')
plt.legend()
plt.show()