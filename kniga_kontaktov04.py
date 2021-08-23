import pickle
import os.path


class Personal_data:

    def __init__(self, name):
        self.name = name
        self.info = ['None']

    def add_info(self, info):
        if 'None' in self.info:
            del self.info[self.info.index('None')]
        self.info.append(info)


def privetstvie():
    print('\nВыберете необходимый функционал:\n'
          '"1" Чтение файла\n'
          '"2" Запись в файл нового контакта\n'
          '"3" Дополнение контактной информации\n'
          '"4" Смена контактной информации\n'
          '"5" Смена имени контакта\n'
          '"6" Удаление котакта\n'
          '"7" Проверка в списке. Поиск контактной информации\n'
          '"s" Для сохранения игры\n'
          '"w" Чтобы выйти\n')


#print(os.listdir())
if 'txt1.txt' in os.listdir():
    with open('txt1.txt', 'rb') as f:
        contacts = pickle.load(f)

else :
    with open('txt1.txt', 'wb') as f:
        pickle.dump("", f)
        contacts = {}


def check(a):
    if a in contacts: return True
    else:
        print('The name isnt exist')
        return False


def main():
    print('\n-------Приветствуем в Адресной книге имени Меня!-------\n')

    while True:

        privetstvie()
        vibor = input()

        if vibor == '1':
           for i in contacts:
               print(i + ":" )
               print(*contacts[i].info, sep='\n', end='\n\n')

        elif vibor == '2':
            name = input("Enter name:")
            contacts[name] = Personal_data(name)

        elif vibor == '3':
            name = input('Enter Name of contact :')
            if check(name):
                information = input('Enter information :')
                contacts[name].add_info(information)

        elif vibor == '4':
            name = input('Enter name:')
            if check(name):
                old_info = input("Enter old info:")
                new_info = input("Enter new info:")
                if old_info in contacts[name].info:
                    contacts[name].info[contacts[name].info.index(old_info)] = new_info

        elif vibor == '5':
            old_key = input("Enter old name:")
            if check(old_key):
                new_key = input("Enter new name:")
                contacts[new_key] = contacts.pop(old_key)

        elif vibor == '6':
            name = input("Enter name to delete:")
            if check(name):
                del contacts[name]

        elif vibor == '7':
            name = input("Enter name to find:")
            if check(name): print('Info :' + contacts[name].info)

        elif vibor == 's':
            with open('txt1.txt', 'wb') as f:
                pickle.dump(contacts, f)
            print("Game saved")

        elif vibor == 'w': break
        else :
            print("Try Again")
            continue


main()


with open('txt1.txt', 'wb') as f:
    pickle.dump(contacts, f)


