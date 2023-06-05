# Задача 49:
# Создать телефонный справочник с возможностью импорта и экспорта данных в # формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла

def choose_action(phonebook):
    while True:
        print('Choose your option:')
        user_choice = input('1 - Import data\n2 - Find contact\n3 - Add contact\n\
4 - Change contact\n5 - Delete contact\n6 - See all concacts\n0 - Exit programm\n')
        print()
        if user_choice == '1':
            file_to_add = input('Enter the name of the imported file: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('Adios!')
            break
        else:
            print('Wrong command')
            print()
            continue

# Импортирование данных (файла)


def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} not found')


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Last name', 'First name', 'Phone number', 'Description']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

# Поиск контакта


def search_parameters():
    print('Enter search parameter')
    search_field = input(
        '1 - Last name\n2 - First name\n3 - Phone number\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Enter last name for search: ')
        print()
    elif search_field == '2':
        search_value = input('Enter first name for search: ')
        print()
    elif search_field == '3':
        search_value = input('Enter number for search: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Last name', '2': 'First name', '3': 'Phone number'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Contact not found!')
    else:
        print_contacts(found_contacts)
    print()

# Добавление контакта


def get_new_number():
    last_name = input('Enter last name: ')
    first_name = input('Enter first name: ')
    phone_number = input('Enter phone number: ')
    cont_descr = input('Add description: ')
    return last_name, first_name, phone_number, cont_descr


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Last name'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Found multiple contacts')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(
            input('Select the contact you want to edit/delete: '))
        return search_result[num_count - 1]
    else:
        print('Contact not found')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Which parameter do you want to change?')
    field = input(
        '1 - Last name\n2 - First name\n3 - Phone number\n4 - Description\n')
    print()
    if field == '1':
        number_to_change[0] = input('Enter last name: ')
    elif field == '2':
        number_to_change[1] = input('Enter first name: ')
    elif field == '3':
        number_to_change[2] = input('Enter phone number: ')
    elif field == '4':
        number_to_change[3] = input('Enter description: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

# Удаление контакта

def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)