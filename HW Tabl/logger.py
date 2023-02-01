
from data_create import name_data, surname_data, phone_data, address_data
import csv

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{address}\n\n"
                    f"Выберите номер варианта:"))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f"{name};{surname};{phone};{address}\n\n")
    print('Успешно!')

def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first_variant = file.readlines()
        data_f_second = []
        j = 0
        for i in range(len(data_first_variant)):
            if data_first_variant[i] == '\n' or i == len(data_first_variant) - 1:
                data_f_second.append(''.join(data_first_variant[j:i]))
                j = i
        data_first_variant = data_f_second
        print(''.join(data_first_variant))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)

    return data_first_variant, data_second


def put_data():
    data_first_variant, data_second_variant = print_data()
    var = int(input(f"В каком файле изменить данные?\n"
                    f"Выберите номер файла:"))
    
    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            n = int(input(f"В какой  записи изменить данные?\n"
                        f"Выберите номер записи:"))
            res = file.readlines()
            new_res = []
            count = 1
            i = 0
            while i < len(res):
                if count != n:
                    if res[i] != '\n':
                        new_res.append(f'{res[i]}')
                        i += 1
                    else:
                        new_res.append('\n')
                        count += 1
                        i += 1
                else:
                    name = name_data()
                    surname = surname_data()
                    phone = phone_data()
                    address = address_data()
                    new_res.extend([name + '\n', surname + '\n', phone + '\n', address + '\n', '\n'])
                    count += 1
                    i += 5
            
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
                for i in new_res:
                    file.write(i)
            
    if var == 2:
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            n = int(input(f"В какой  записи удалить данные?\n"
                        f"Выберите номер записи:"))
            res = file.readlines()
            new_res = []
            count = 1
            i = 0
            while i < len(res):
                if count != n:
                    if res[i] != '\n':
                        new_res.append(f'{res[i]}')
                        i += 1
                    else:
                        new_res.append('\n')
                        count += 1
                        i += 1
                else:
                    name = name_data()
                    surname = surname_data()
                    phone = phone_data()
                    address = address_data()
                    new_res.extend([name + ';', surname + ';', phone + ';', address + '\n', '\n'])
                    count += 1
                    i += 2
            
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_res:
                file.write(i)
    print('Успешно!')


def delete_data():
    data_first_variant, data_second_variant = print_data()
    var = int(input(f"В каком файле удалить данные?\n"
                    f"Выберите номер файла:"))
    
    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            n = int(input(f"В какой  записи удалить данные?\n"
                        f"Выберите номер записи:"))
            res = file.readlines()
            new_res = []
            count = 1
            i = 0
            while i < len(res):
                if count != n:
                    if res[i] != '\n':
                        new_res.append(f'{res[i]}')
                        i += 1
                    else:
                        new_res.append('\n')
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 5
            
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
                for i in new_res:
                    file.write(i)
            
    if var == 2:
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            n = int(input(f"В какой  записи удалить данные?\n"
                        f"Выберите номер записи:"))
            res = file.readlines()
            new_res = []
            count = 1
            i = 0
            while i < len(res):
                if count != n:
                    if res[i] != '\n':
                        new_res.append(f'{res[i]}')
                        i += 1
                    else:
                        new_res.append('\n')
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 2
            
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_res:
                file.write(i)
    print('Успешно!')

