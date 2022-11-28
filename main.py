# Задание 1 (урок 3)
# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элементов списка,
# стоящих на нечетной позиции







# Задача 1
# d = 7
# prices = ['1578.4', '892.4', '354.1', '871.5']
#
# print(list(map(lambda x: round(float(x) * (1-d/100), 2), prices )))


# Задача 2
# user_names = ['Иван', 'Петр', ]
# user_logins = ['ivan', 'petr', 'olga', 'sergey']
# user_roles = ['user', 'staff', 'admin', 'user']
#
# info = list(zip(user_names, user_logins, user_roles))
# print(info)

# Задача 35
# # 35. Есть N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 == A[i-1]. Найдите это число.
# my_str = ‘1 2 3 5 6’ => 4
my_str = '1 2 3 5 6'
my_str = my_str.split()
new_list = list(map(int, my_str))
for i in range(len(new_list) - 1):
    if new_list [i+1] - new_list [i] > 1:
        print(new_list[i]+1) for i in range(len(new_list) - 1) if new_list[i+1] - new_list [i] > 1))
        









