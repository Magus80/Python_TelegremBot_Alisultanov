# Python_TelegremBot_Alisultanov
Проект: Telegram-бот с функцией календаря
Магомед Алисултанов
Magus80
alisultanov@mail.ru

import os
import glob


# функция создающая заметку. Получает название и текст заметки созжает текстовый файл с имененим указанным и соже
def note_build(note_name, note_text):
    print(note_name, note_text)
    with open(note_name + '.zam', 'w') as filename:
        filename.write(note_text)


# ввод заметки и отправка даннных заметки в функцию создающую
def note_create():
    note_name = input('Ведите название заметки без расширения:')
    note_text = input('Введите содержание заметки:')
    note_build(note_name, note_text)


# функция редактируюющая заметку
def note_edit():
    ask = ''
    print('Выберите функционал:\n'
          '1 - Дописать заметку\n'
          '2 - Переписать заметку\n'
          'q - Выйти в главное меню')
    ask = input('Введите код меню:')
    err = 1
    while err == 1:
        if ask == 'q':
            return
        if int(ask) == 1:
            noteedit = input(
                'Введите название заметки без расширения для добавления записи (для возврата в главное меню введите "q"):')
            if noteedit == 'q':
                return
            try:
                test = open(noteedit + '.zam', 'r')
                with open(noteedit + '.zam', 'a') as ne:
                    add_text = '\n' + input('Введите текст, который надо дописать:')
                    err = 0
                    ne.write(add_text)
            except:
                print('Такой заметки не существует! Попробуйте еще раз!')
        if int(ask) == 2:
            noteedit = input(
                'Введите название заметки без расширения для перезаписи (для возврата в главное меню введите "q"):')
            if noteedit == 'q':
                return
            try:
                test = open(noteedit + '.zam', 'r')
                with open(noteedit + '.zam', 'w') as ne:
                    new_text = input('Введите текст, который надо записать:')
                    err = 0
                    ne.write(new_text)
            except:
                print('Такой заметки не существует! Попробуйте еще раз!')


# if ask == 2:


# Функция читающая
def note_read():
    err = 1
    while err == 1:
        try:
            noteread = input(
                'Введите название заметки без расширения для просмотра (для возврата в главное меню введите "q"):')
            if noteread == 'q':
                return
            with open(noteread + '.zam', 'r') as nr:
                err = 0
                print(nr.read())
                nr.close()
        except:
            print('Несуществующая заметка! Проверьте правильность названия!')


# Функция удаляющая заметку
def note_delete():
    err = 1
    while err == 1:
        try:
            notedel = input(
                'Введите название заметки  без расширения для удаления (для возврата в главное меню введите "q"):')
            if notedel == 'q':
                return
            with open(notedel + '.zam', 'r') as nr:
                print(nr.read())
                nr.close()
                err = 0
                ask = input('Вы действительно хотите удалить заметку (y/n) :')
                if ask == 'y':
                    os.remove(notedel + '.zam')
        except:
            print('Несуществующая заметка! Проверьте правильность названия!')


# Основной код программы


code = 25
while True:
    print('\n'
          'Выберите действие:\n'
          '\n'
          '1 - Посмотреть список заметок\n'
          '2 - Создать заметку\n'
          '3 - Просмотреть содержимое заметки\n'
          '4 - Редактировать содержимое заметки\n'
          '5 - Удалить заметку\n'
          'q - Выход')
    try:
        code = input('Введите номер пункта:')
        if code == 'q':
            break
        if int(code) == 1:
            #убираем расшиения и печатаем столбец
            print('Ваши заметки:')
            list = ''.join(glob.glob('*.zam'))
            list2 = list.split('.zam')
            print('\n'.join(list2))
        if int(code) == 2:
            note_create()
        if int(code) == 3:
            note_read()
        if int(code) == 4:
            note_edit()
        if int(code) == 5:
            note_delete()
    except:
        print('Вы ввели неверный ключ! Повторите ввод!')
print('Вы вышли из программы!')

