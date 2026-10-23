import sys
import json
from storage import read, write

try:
    plants = read()
    if len(plants) == 0:
        print('Каталог пуст. Процесс завершен')
        sys.exit()
except FileNotFoundError:
    print('Каталог не найден. Процесс завершен')
    sys.exit(1)
except json.JSONDecodeError:
    print('Не удалось прочитать каталог: некорректный JSON')
    sys.exit(1)


for number, plant in enumerate(plants):
    if plant["days"] >= 5 or plant["days"] == 0:
        day = 'дней'
    elif plant["days"] == 1:
        day = 'день'
    elif plant["days"] >= 2 and plant["days"] <= 4:
        day = 'дня'
    print(f'{number+1}. {plant["name"]} | {plant["place"]} | Полив раз в {plant["days"]} {day}')

def choose_plant():
    tries = 3
    while tries > 0:
        try:
            answer1 = int(input(f'Выберите номер растения от 1 до {len(plants)} '))
            if answer1 < 1 or answer1 > len(plants):
                tries -= 1
                if tries == 0:
                    print(f'Слишком много неправильных вводов!')
                    return None
                print(f'Пожалуйста, введите число от 1 до {len(plants)}')
            else:
                return answer1-1
        except ValueError:
            tries -= 1
            if tries == 0:
                print(f'Слишком много неправильных вводов!')
                return None
            print(f'Пожалуйста, введите число от 1 до {len(plants)}')



def change_days(selcted_number):
    tries = 3
    while tries > 0:
        try:
            answer2 = int(input(f'Введите актуальный интервал полива (в днях) '))
            if answer2 < 1:
                tries -= 1
                if tries == 0:
                    print('Слишком много неправильных вводов!')
                    return None
                print('Число должно быть положительным!')
            else:
                print(f'Изменения успешно внесены. Теперь интервал полива растения {plants[selcted_number]["name"]} в днях: {answer2}')
                return answer2
        except ValueError:
            tries -= 1
            if tries == 0:
                print(f'Слишком много неправильных вводов!')
                return None
            print(f'Пожалуйста, введите число')



if choose_plant() is not None:
    selected_number = choose_plant()
    if change_days(selected_number) is not None:
        selected_days = change_days(selected_number)
        plants[selected_number]["days"] = selected_days
        write(plants)



