def p1():
    first = [13, 34, 58, 78, 91]
    second = int(input( "Введите желаемое число: "))
    print(*first)
    print("Введите Ваще число", second)
    if second in first:
        print("Поздравляю, Вы угадали число!Вы молодец!")
    else:
        print("К сожалению, нет такого числа! Вы не молодец!")


def p2():
    first = [13, 13, 34, 58, 78, 58]
    print(*first)
    for i in range(0, len(first)-1):
        for j in range(i+1, len(first)):
          if first[i] == first[j]:
             print(first[i])


def p3():
    nedelya = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" )
    dni = int(input("сколько выходных дней?"))
    for i in nedelya:
        print ("Ваши рабочие дни:", *nedelya[:-dni])
        print("Ваши выходные дни:", *nedelya[-dni:])
        break


def p4():
    import random
    list1 = ['Иванов', 'Сухарев', 'Морозова', 'Гладких', 'Францев', 'Бурнева', 'Носов', 'Лобов', 'Моргун', 'Шейкина']
    list2 = ['Жуков', 'Быков', 'Волков', 'Воробьев', 'Беляева', 'Фролов', 'Бородина', 'Григорьев', 'Васильева', 'Петров']
    komand = tuple(random.sample(list1,5) + random.sample(list2, 5))
    print(*list1)
    print(*list2)
    print(*komand)
    print(len(komand))
    if 'Иванов' in komand:
        print(komand.count('Иванов'))
    else:
        print("no")


p1()
p2()
p3()
p4()
