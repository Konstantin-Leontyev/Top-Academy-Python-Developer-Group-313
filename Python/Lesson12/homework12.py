data = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

name = 'name'
salary = 'salary'

# От пустой декларации я отказался
# payroll = {name: None, salary: None}

# # Этот трюк не сработал выдал ошибку изменением размера
# # for key, value in data.items():
# #     if key in ('name', 'salary'):
# #         payroll[key] = data.pop(key)


# payroll[name] = data.pop(name)
# payroll[salary] = data.pop(salary)

# payroll = dict(name=data.pop(name), salary=data.pop(salary))

payroll = {
    name: data.pop(name),
    salary: data.pop(salary)
}

print(data)
print(payroll)
# print(type(payroll))

