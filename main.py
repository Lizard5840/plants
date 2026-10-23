import sys
import json
from storage import read, write

try:
    plants = read()
except FileNotFoundError:
    print('Каталог не найден. Процесс завершен')
    sys.exit(1)
except json.JSONDecodeError:
    print('Не удалось прочитать каталог: некорректный JSON')
    sys.exit(1)




def add_plant():
    tries = 3
    while tries > 0:
        name = input("Введите название растения ").strip()
        if name.strip() == '':
            tries -= 1
            if tries == 0:
                print('Слишком много неправильных вводов')
                return None
            print('Поле не может быть пустым')
        else:
            break
    tries = 3
    while tries > 0:
        place = input("Введите комнату, где будет находиться растение ").strip()
        if place.strip() == '':
            tries -= 1
            if tries == 0:
                print('Слишком много неправильных вводов')
                return None
            print('Поле не может быть пустым')
        else:
            break
    tries = 3
    while tries > 0:
        try:
            days = int(input("Введите интервал полива в днях "))
            if days < 1:
                tries -= 1
                if tries == 0:
                    print('Слишком много неправильных вводов!')
                    return None
                print('Введите положительное число')
            else:
                break
        except ValueError:
            tries -= 1
            if tries == 0:
                print('Слишком много неправильных вводов!')
                return None
            print('Введите положительное число')

    plant = {
        "name": name,
        "place": place,
        "days": days
    }
    plants.append(plant)
    return plants

def user():
    tries = 3
    while tries > 0:
        try:
            answer = int(input(f'Вы хотите:\n1. Добавить растение\n2. Изменить интервал полива существующего '))
            if answer < 1 or answer > 2:
                tries -= 1
                if tries == 0:
                    print(f'Слишком много неправильных вводов!')
                    return None
                print(f'Пожалуйста, введите 1 или 2')
            else:
                return answer
        except ValueError:
            tries -= 1
            if tries == 0:
                print(f'Слишком много неправильных вводов!')
                return None
            print(f'Пожалуйста, введите 1 или 2')

choise = user()
if choise == 2:
    if len(plants) == 0:
        print('Каталог пуст. Процесс завершен')
        sys.exit()
    print()
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


    selected_number = choose_plant()
    if selected_number is not None:
        selected_days = change_days(selected_number)
        if selected_days is not None:
            plants[selected_number]["days"] = selected_days
            write(plants)
elif choise == 1:
    result = add_plant()
    if result is not None:
        write(plants)



