'''
Дан файл california_housing_train.csv.
Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
'''

from pandas import read_csv

data = read_csv ('california_housing_train.csv')

avg = data[(data['population'] > 0) & (data['population'] < 500)]['medianHouseValue'].mean()


'''
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
'''

max_households_in_min_population = data[data['population'] == data['population'].min()] ['households'].max()