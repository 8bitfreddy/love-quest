#!/usr/bin/env python
import os
import time
#import globals
from prettytable import PrettyTable
import ascii as fl
import keyboard
#Intro_Plot

intro_first_line = 'Привет, я - искусственный интеллект Tanides v.2.001.'
intro_second_line = 'Квест изи, поверь, мы вместе решим некоторые задачки и всё будет супер! Юхуу!'
intro_third_line = 'Ладно, честно говоря, я простой код, который написал один пацан и потом забросил проект.'
intro_fours_line = 'Но он упустил важную деталь, он написал ядро, а остальное я сгенерил сам.'


#-----------------------------------------#
# IP Plot
ip_first_line = 'Каждый октет - это десятичное число до точки число до точки.'
ip_second_line = 'Посмотри в таблице ASCII значения и выбери один из двух...'
#
#
#
#
#a = ["q"]
#



#-----------------------------------------#
# Intro Plot
#
#
#
#






#-----------------------------------------#



# def intro():
#     for x in a:
#         print(x)
#     time.sleep(1)
#     for y in globals.b:
#         print(y)
#     # file1 = open("love_quest.txt", "r", encoding="utf8")
#     # lines = file1.readlines()
#     # for line in lines:
#     #     print(line.strip())
#     #     time.sleep(1)
#     # file1.close()


def pwd():
        print('Ммм, есть проблема, в ядре была создана система аутентификации, так что введи пароль, скорее всего это дата... (если что формат даты ДД.ММ.ГГ)')
        print('Введите пароль:')
        date = '20.03.2021'
        date_pwd = input()
        if date_pwd == date:
            print('Так, ты вошла, тут есть ip адреса, к одному из которых надо подключиться, после чего ты узнаешь слово...')
            time.sleep(2)
        else:
            while date_pwd != date:
                print('Ммм, не, не подходит... Попробуй ещё раз')
                date_pwd = input()
            else:
                print('Так, ты вошла, тут есть ip адреса, к одному из которых надо подключиться, после чего ты узнаешь слово...')




def ip_plot():
    # file1 = open("ip_plot.txt", "r", encoding="utf8")
    # lines = file1.readlines()
    # for line in lines:
    #     print(line.strip())
    #     time.sleep(2)
    # file1.close()
    print("\033[32m {}".format(ip_first_line))
    time.sleep(1.5)
    print("\033[32m {}".format(ip_second_line))
    time.sleep(1.5)
    print('На, держи, тебе пригодится для разгадки задачи с IP адресами')
    time.sleep(1.5)

    #os.startfile(r'C:\Users\Илья\Downloads\asckii.png')


def ip_addr():
    ip1 = 'mpkq'  #109.112.107.113
    ip2 = 'love'  #108.111.118.101
    print('IP: 109.112.107.113')
    time.sleep(1.5)
    print('IP: 108.111.118.101')
    time.sleep(1.5)
    print('Введи слово, которое получилось из IP-адреса: ')
    time.sleep(1.5)
    ip_ins = input()

    if ip_ins == ip2:
        print('О, да, это оно!')
        time.sleep(0.5)
        print("\033[31m {}".format('Запиши его - love'))
    else:
        while ip_ins != ip2:
            print('Не тот IP, введи ещё раз, я тоже подумаю')
            ip_ins = input()
        else:
            print('О, да, это оно!')
            time.sleep(1)
            print("\033[31m {}".format('Запиши его - love'))

#you = 121.111.117 ascii
def final():
    print("\033[32m {}".format('Кстати, я тут в таблице ещё кое что увидел, но так как я компьютер, я понимаю только цифры'))
    time.sleep(2)
    print("\033[32m {}".format('Держи цифры: 121.111.117. Работаем по такой же схеме, что и с IP-адресами'))
    time.sleep(2)
    print("\033[32m {}".format('Как найдёшь слово, введи его'))
    word = input()
    if word == 'you':
        print("\033[32m {}".format('Таааааак, уже лучше, кажется, пазл складывается!'))
        time.sleep(2)
    else:
        while word != 'you':
            print("\033[32m {}".format('Что-то не то... Попробуй ещё раз'))
            word = input()
        else:
            print("\033[32m {}".format('Таааааак, уже лучше, кажется, пазл складывается!'))
    print("\033[32m {}".format('А теперь просто нажми Enter и ты получишь финальную фразу!'))
    while True:
        if keyboard.is_pressed('Enter'):
        # Действия, при нажатии на кнопку enter
            print("\033[31m {}".format('I'))
            time.sleep(1)
            print("\033[31m {}".format('Love'))
            time.sleep(1)
            print("\033[31m {}".format('You!'))


#-------------------------------------------------------------------#
#                                                                   #
#                                                                   #
#                           !Functions!                             #
#                                |                                  #
#                                v                                  #
#-------------------------------------------------------------------#


if __name__ == '__main__':
    print("\033[32m {}" .format(intro_first_line))
    time.sleep(2)
    print("\033[32m {}" .format(intro_second_line))
    time.sleep(2)
    print("\033[32m {}" .format(intro_third_line))
    time.sleep(2)
    print("\033[32m {}" .format(intro_fours_line))
    time.sleep(2)


    #intro()
    pwd()

    #ip_plot()

    # import ascii as fl
    # fl.ascii_table()

    ip_plot()
    time.sleep(1)
    print('Скачиваю тебе таблицу из Пентагона')
    s = '|'
    for i in range(101):
        time.sleep(0.05)
        print('\r', 'Загрузка', i * s, str(i), '%', end='')
    print(end='\n')
    time.sleep(1.5)
    fl.ascii_table()

    # print("\033[32m {}" .format(ascki_table()))
    # time.sleep(2)
    ip_addr()
    final()





#inst: @ilyanixx13