# def greet(name):
#     return ('glhf', *name)
# name = input()
# while name == '':
#     print('кто ты ?')
#     name = input()
# print(greet(name))

# def sqr(n):
#     return int(n)**2
# n = input()
# if n.isdigit():
#     n = int(n)
#     print(sqr(n))
# else:
#     print('ошибка')

# def mot(a, b):
#     if int(a) < int(b):
#         return b
#     elif int(a) > int(b):
#         return a
#     else:
#         return (a, '=', b)
#
#
# a = input()
# b = input()
# if a.isdigit() and b.isdigit():
#     print(mot(a, b))
# else:
#     print('буквы не могут быть больше или меньше')



# def greet(name, age):
#     if age.isdigit():
#         return (name, age)
#     else:
#         return (name, '30')
#
#
# name = input();
# age = input()
# while name == '':
#     print('введите имя')
#     name = input()
# print(greet(name, age))



# def is_pr(n):
#     k = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             k += 1
#             print(k)
#     if k == 2:
#         return n, 'is prime'
#     else:
#         return n, 'not is prime'
#
#
# n = input()
# if n.isdigit():
#     n = int(n)
#     print(is_pr(n))
# else:
#     print('error')




