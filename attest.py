import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из csv файла
df = pd.readcsv('spotify.csv')

# Создание графика для столбца "streams"
plt.figure(figsize=(10,6))
#plt.scatter(df'streams', df'valence_%')
plt.xlabel('Streams')
plt.ylabel('Valence (%)')
plt.title('Relationship between Streams and Valence of Songs')
plt.show()

# Создание графика для столбца "valence%"
plt.figure(figsize=(10))
plt.hist(df['valence%'], bins=20)
plt.xlabel('Valence (%)')
plt.ylabel('Number of Songs')
plt.title('Distribution of Valence (%) in Songs')
plt.show()


# Подсчет количества уникальных значений для каждого столбца
uniquevalues = df.nunique()

# Получение двух признаков с наибольшим количеством уникальных значений
toptwofeatures = uniquevalues.nlargest(2)

print(toptwofeatures)



# Разбиение названия песен на категории по первой букве
df['tracknamecategory'] = df['trackname'].apply(lambda x: x0)
df['track_name_category'] = df['track_name_category'].astype('category')

# Разбиение имени исполнителей по длине имени
df['artist_name_length'] = df['artist_name'].apply(lambda x: len(x))
df['artist_name_length'] = pd.cut(df['artist_name_length'], bins=[0, 5, 10, 15, 20, 25], labels=['<5', '5-10', '10-15', '15-20', '20-25'])


# График взаимосвязи между Streams, Valence (%) с учетом категорий названия песен
plt.figure(figsize=(10))
sns.scatterplot(data=df, x='streams', y='valence%', hue='tracknamecategory')
plt.xlabel('Streams')
plt.ylabel('Valence (%)')
plt.title('Relationship between Streams, Valence of Songs with Track Name Categories')
plt.show()

# Гистограмма распределения Valence (%) с учетом категорий длины имени исполнителей
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='valence%', hue='artistnamelength')
plt.xlabel('Valence (%)')
plt.ylabel('Number of Songs')
plt.title('Distribution of Valence (%) in Songs with Artist Name Length Categories')
plt.show()


# Круговая диаграмма для общего количества прослушиваний на Spotify в зависимости от того, присутствует песня в чартах Apple Music или нет
applechartscounts = df['in_apple_charts'].valuecounts()
plt.figure(figsize=(9))
plt.pie(applechartscounts, labels=applechartscounts.index, autopct='%1.1f%%')
plt.title('Presence of Songs in Apple Music Charts')
plt.show()

# Ящик с усами для сравнения энергетичности песен по категориям длины имени исполнителей
plt.figure(figsize=(10))
sns.boxplot(data=df, x='artistnamelength', y='energy%')
plt.xlabel('Artist Name Length')
plt.ylabel('Energy (%)')
plt.title('Comparison of Energy in Songs based on Artist Name Length Categories')
plt.show()

