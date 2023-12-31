"""
Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

from pandas import read_csv


data = read_csv ('california_housing_test.csv')
# # print(data.info())
# # print(data.shape)
# # print(data.dtypes)

"""
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""


# print(data.isnull().sum())
# print(data[data['median_income'] < 2]['median_house_value'])


# print(data[['longitude', 'latitude']])
# print(data.iloc[:, 2])

# print(data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)])
