import pandas as pd
import matplotlib.pyplot as plt

### Experimento foi feito com -50V ao invés de -100V como indicado no roteiro

# Ler os dados do arquivo CSV
data = pd.read_csv('data_exp3.csv')

# Plotar os dados
plt.figure(figsize=(10,5))
plt.plot(data['V'], data['I(microAmpere)'], label='I(microAmpere)')  # note o espaço antes do 'I'
plt.xlabel('V')
plt.ylabel('I(microAmpere)')
plt.title('Data from data_exp3.csv')
plt.legend()
plt.show()