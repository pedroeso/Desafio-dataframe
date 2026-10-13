import pandas as pd

dfNull = pd.read_csv(r"C:\Senac analista de dados\Desafio dataframe\funcionarios - Null.csv")


dfNullPreenchido = dfNull.fillna({'departamento': "nenhum"})

dfNullRemovido = dfNull.dropna(subset=['lucro'])

print(dfNullRemovido)
