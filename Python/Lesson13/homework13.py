data = {
    'January': {
        'Total Sales': 52_000.0,
        'Production Cost': 46_800.0
    },
    'February': {
        'Total Sales': 51_000.0,
        'Production Cost': 45_900.0
    },
    'March': {
        'Total Sales': 48_000.0,
        'Production Cost': 43_200.0
    }
}

# Тут я пытаюсь понять где и зачем может пригодиться zip
# for month in data:
#     print(f'Общая прибыль в {month} = {data[month]['Total Sales'] - data[month]['Production Cost']}')

# for month in data:
#     total_sales = data[month]['Total Sales']
#     production_cost = data[month]['Production Cost']
#     monthly_profit = total_sales - production_cost
#     print(f'Общая прибыль в {month} = {monthly_profit}')


# data1 = {
#     'January': {
#         'Total Sales': 52_000.0,
#         'Production Cost': 46_800.0
#     }
# }
#
# a, b = zip(data1['January'].values())
# print(a)  # (52000.0,)
# print(b)  # (46800.0,)

# for month in data:
#     # tmp = tuple(zip(list(data[month].values())))
#     # print(tmp)
#     total_sales, production_cost = zip((data[month].values()))
#     print(total_sales, production_cost)
# monthly_profit = total_sales[0] - production_cost[0]
# print(monthly_profit)
# print(f'Общая прибыль в {month} = {monthly_profit}')


# list_of_month_values = list(zip(data.values()))
# print(list_of_month_values)
# a, b, c = list_of_month_values
#
# print(a, b, c)
# a = a[0]
# b = b[0]
# c = c[0]
# print(a, b, c)
# z, x = a.values()
# print(z, x)
# for (k, v), (k1, v1), (k2, v2) in zip(a.items(), b.items(), c.items()):
#     print(k, v, k1, v1, k2, v2)

# list_of_month_values = list(zip(data.values()))
# print(list_of_month_values)
# print(type(list_of_month_values[0][0]))
# print({**list_of_month_values[0][0]})

# print({**data})
# for month, values_dictionary in {**data}.items():
#     # print(month, values_dictionary)
#     # print(value)
#     # print({**value}.values())
#     # for key, value in {**tuple(values_dictionary.values())}:
#     #     print(key, value)
#     # print(values_dictionary.values())
#     total_sales, production_cost = tuple(values_dictionary.values())
#     # for total_sales, production_cost in tuple(values_dictionary.values()):
#     #     print(y)
#     # print(total_sales, production_cost)
#     monthly_profit = total_sales - production_cost
#     print(f'Общая прибыль в {month} = {monthly_profit}')
#
# print({**data})
# for month, values_dictionary in {**data}.items():
#     total_sales, production_cost = tuple(values_dictionary.values())
#     monthly_profit = total_sales - production_cost
#     print(f'Общая прибыль в {month} = {monthly_profit}')

# print({**data})
# for month, values_dictionary in {**data}.items():
#     print(values_dictionary)
#     values_tuple = tuple({**values_dictionary}.values())
#     print(values_tuple)
#     total_sales, production_cost = zip{*values_tuple}
#     # print(total_sales)
#     # total_sales, production_cost = tuple(values_dictionary.values())
#     # monthly_profit = total_sales - production_cost
#     # print(f'Общая прибыль в {month} = {monthly_profit}')

# #   Если в условии даны списки
# month_list = ['January', 'February', 'March']
# total_sales_list = [52_000.0, 51_000.0, 48_000.0]
# production_cost_list = [46_800.0, 45_900.0, 43_200.0]
#
# # Поочередно собираем картеж из значений списков и упаковываем в список.
# # Распаковываем список.
# for month, total_sales, production_cost in zip(month_list, total_sales_list, production_cost_list):
#     # Работаем с полученными элементами
#     monthly_profit = total_sales - production_cost
#     print(f'Общая прибыль в {month} = {monthly_profit}')

#   Если в условии даны словари
dict1 = {'Month': 'January', 'Total sales': 52_000.0, 'Production cost': 46_800.0}
dict2 = {'Month': 'February', 'Total sales': 51_000.0, 'Production cost': 45_900.0}
dict3 = {'Month': 'March', 'Total sales': 48_000.0, 'Production cost': 43_200.0}

dict4 = [dict1, dict2, dict3]

# a, b, c = zip(dict1.values())  # ('January',) (52000.0,) (46800.0,)
# a, b, c = list(zip(dict1.values()))  # January 52_000.0 46_800.0
# a, b, c = dict1.values()  # January 52_000.0 46_800.0
#
# print(a, b, c)

for month, total_sales, production_cost in list(zip(dict1, dict2, dict3)):
    print(month, total_sales, production_cost)