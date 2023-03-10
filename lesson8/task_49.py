# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0]) # -1 это значит последняя строка массива и 0 значит первый элемент в последней строке
        return all_data

def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")

def add_new_contact():
    global id
    tel_book = ["surname", "name", "second_name", "phone-number"]
    string = ""
    for i in tel_book:
        string += input(f"enter {i} ") + " "
    id += 1
    # print(f"{id} {string}")
    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{id} {string}\n")

def search_a_record():
    input("Enter ")
    print(all_data[i] for i in all_data if )


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete\n"
                       "5. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_a_record()
            case "4":
                delete_contact()
            case "5":
                play = False
            case _:
                print("Try again!\n")
main_menu()