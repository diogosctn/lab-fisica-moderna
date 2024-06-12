import pandas as pd
import math
 
# Definir as constantes
DISTANCE = 0.0015
VISCOSITY = 1.869*10**(-5) #Viscosidade para T=29°
DENSITY = 886
GRAVITY = 9.81
VOLTAGE = 376
CORRECTION_FACTOR = (8.22*10**(-8)) / (1.01*10**(5))
 
# Carregar o arquivo CSV
df = pd.read_csv('measures.csv')
 
# Criar uma nova coluna 'vs' que é a divisão da distância pela coluna 'ts'
df['vs'] = DISTANCE / df['ts']
 
# Criar uma nova coluna 'vd' que é a divisão da distância pela coluna 'td'
df['vd'] = DISTANCE / df['td']
 
# Criar uma nova coluna 'vd - vs' que é a subtração de 'vd' por 'vs'
df['vd - vs'] = df['vd'] - df['vs']
 
# Criar uma nova coluna 'vd - vs' que é a soma entre 'vd' e 'vs'
df['vd + vs'] = df['vd'] + df['vs']
 
def droplet_radius(df):
    # Verificar se a coluna 'vd - vs' existe no DataFrame
    if 'vd - vs' not in df.columns:
        return "Error: Column 'vd - vs' does not exist in the DataFrame."
   
    # Definir a constante
    CONSTANT = (3/2)*math.sqrt(VISCOSITY/(GRAVITY*DENSITY))
    print('Constante no cálculo do raio')
    print(CONSTANT)
 
    # Criar uma nova coluna 'r' que é a raiz quadrada de 'vd - vs' multiplicado por uma constante
    df['r'] = df['vd - vs'].apply(lambda x: CONSTANT * math.sqrt(x) if x >= 0 else "Error: Cannot calculate the square root of a negative number.")
 
    return df
 
droplet_radius(df)
 
def droplet_charge(df):
    # Verificar se a coluna 'vd - vs' existe no DataFrame
    if 'vd - vs' not in df.columns:
        return "Error: Column 'vd - vs' does not exist in the DataFrame."
   
    # Definir a constante
    CONSTANT = (3*math.pi*DISTANCE*VISCOSITY)
 
    print('Constante no cálculo da carga')
    print(CONSTANT)
 
    # Criar uma nova coluna 'r' que é a raiz quadrada de 'vd - vs' multiplicado por uma constante
    df['q'] =CONSTANT * (df['r'] / VOLTAGE) * df['vd + vs']
    return df
 
droplet_charge(df)
 
def droplet_charge_correction(df):
 
    # Verificar se a coluna 'q' existe no DataFrame
    if 'q' not in df.columns:
        return "Error: Column 'q' does not exist in the DataFrame."
   
    # Criar uma nova coluna 'q' que é a divisão da coluna 'q' pela correção
    df['q_c'] = df['q'] * (1 + (CORRECTION_FACTOR * df['r']))**(-3/2)
 
    return df
 
droplet_charge_correction(df)
 
print(df)
 
df.to_csv('data.csv', index=False)