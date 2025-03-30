import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('./Tasks/transformacao_de_dados/data.csv')

print(df.head(10))
print(df.shape)