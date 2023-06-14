from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n')


def print_data():
    print('Вывожу данные для Вас данные из 1-ого файла\n')
    with open('data_first_variant.txt', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас данные из 2-ого файла\n')
    with open('data_second_variant.txt', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
   
    data_first, data_second = print_data()
    # print("__________11_____________________")
    # print(data_first[1].split('\n'))
    # print(data_second[1].split(';'))
    # print("___________22____________________")
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    # Можно добавить проверку, чтобы человек не выходил за пределы записей
    if number_file == 1:
        print(f'Изменить данную запись\n', data_first[number_journal].split("\n"))
    else:
        print(f'Изменить данную запись\n', data_second[number_journal].split(";"))

    var = int(input(f"Какой элемент вы хотите изменить?\n"
                    f"1 - Имя\n"
                    f"2 - Фамилия\n"
                    f"3 - Телефон\n"
                    f"4- Адрес\n"
                    f"Выберите номер варианта: "))
               
# name = name_data()
# surname = surname_data()
# phone = phone_data()
# address = address_data()
  
    if number_file == 1:  # Можно сделать нумерацию внутри файла
        # data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
        #              data_first[number_journal + 1:]
        item_list=data_first[number_journal].split("\n")
        if var==1:
            change_string=name_data()+'\n'+item_list[2]+'\n'+item_list[3]+'\n'+item_list[4]+'\n'
        elif var==2:
            change_string=name = item_list[1]+'\n'+surname_data()+'\n'+item_list[3]+'\n'+item_list[4]+'\n'
        elif var==3:
            change_string=name = item_list[1]+'\n'+item_list[2]+'\n'+phone_data()+'\n'+item_list[4]+'\n'
        elif var==4:
            change_string=name = item_list[1]+'\n'+item_list[2]+'\n'+item_list[3]+'\n'+address_data()+'\n'  
        data_first = data_first[:number_journal] + [change_string] + data_first[number_journal + 1:]
        with open('data_first_variant.txt', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        # data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                    #   data_second[number_journal + 1:]
        
        item_list=data_second[number_journal].split(";")
        if var==1:
            change_string=name_data()+';'+item_list[1]+';'+item_list[2]+';'+item_list[3]+'\n'
        elif var==2:
            change_string=name = item_list[0]+';'+surname_data()+';'+item_list[2]+';'+item_list[3]+'\n'
        elif var==3:
            change_string=name = item_list[0]+';'+item_list[1]+';'+phone_data()+';'+item_list[3]+'\n'
        elif var==4:
            change_string=name = item_list[0]+';'+item_list[1]+';'+item_list[2]+';'+address_data()+'\n'  
        data_second = data_second[:number_journal] + [change_string] + data_second[number_journal + 1:]
        with open('data_second_variant.txt', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.txt', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.txt', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные
