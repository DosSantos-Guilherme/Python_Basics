import pandas as pd
import matplotlib.pyplot as plt

DataFr = pd.read_csv('Exercícios - Apostila.csv',decimal=',')

print(DataFr[:10])

mediaColunaX = DataFr['Coluna_X'].mean()
print()
DataFr['Coluna_X'] = DataFr['Coluna_X'].fillna(f"%.1f"%(mediaColunaX))

print(DataFr)

print(DataFr[(DataFr['Coluna_Y']>50.0)])

GroupedCategoryDataFr = DataFr.groupby('Categoria')['Valor'].sum().reset_index()
print(GroupedCategoryDataFr)
DataFr['Coluna_X'] = pd.to_numeric(DataFr['Coluna_X'], errors='coerce')
DataFr['Coluna_Y'] = pd.to_numeric(DataFr['Coluna_Y'], errors='coerce')

DataFr["Produto_Colunas_X_Y"] = DataFr['Coluna_X']*DataFr['Coluna_Y']
print(DataFr)

FrequencyCategoryDataFr = DataFr.groupby("Categoria")["Categoria"].count()
plt.figure(figsize=(10,6))
FrequencyCategoryDataFr.plot(kind='bar')
plt.xticks(rotation=0)
plt.title("Gráfico mostrando quantidade de produtos por categoria")
plt.xlabel("Categorias")
plt.ylabel("Quantidades")
plt.savefig("Frequency.png")


plt.figure(figsize=(10,6))
plt.hist(DataFr['Coluna_Y'], bins=5, color='skyblue', edgecolor='black')
plt.title("Histograma da coluna Y")
plt.savefig("Histogram.png")

#DataFr['Coluna_X']=DataFr['Coluna_X'].fillna(mediaColunaX)
#print(DataFr)