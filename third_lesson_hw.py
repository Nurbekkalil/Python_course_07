# name = 'Nurbek'
# my_first_variable = f'ego zovut {name} i on veteran'
#
# print(my_first_variable)
#
#
# name = 'nurbek'.upper()
# print(name)



# is_asian = True
# is_american = False

# name = input()

# if name == 'Oskar':
#     print('Asian')
# else:
#     print('American')

#
# name = input()
# age = int(input())
# print(name)
#
# if name == 'Oskar':
#     print('Asian')
# else:
#     print('American')
#
# if age > 18:
#     print('Pass')
# else:
#     print('Not pass')
#
#
# if False:
#     print("dfdf")
# else:
#     print('dfmdkf')
#
#


# name = input()
# avtandil = 'avtandil'
# age = int(input())
#
#
# if name == avtandil and age == 35:
#
#     print(True, 'Vy Avtandil')
#
# else:
#     print(False, 'Vy ne avtandil')
#
#


# n1 = True + True + True
# n2 = False + False
#
# print(n1)
# print(n2)
# print()
# print(type(n1))
# print(type(n2))
# print()
#
#
# if 1:
#     print(True)
# else:
#     print(False)


#
# name = input()
# print(len(name))
#
# if name:
#     print(True)
# else:
#     print(False)



number = 23
running = False
while running:
    guess = int(input('Введите целое число :'))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False# это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')