# Функция enumerate() применяется к итерируемому объекту и
# возвращает новый итератор с кортежами из индекса и элементов входных данных.
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]