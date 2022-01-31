#!/usr/bin/env python
import os
import time
#import globals
#from prettytable import PrettyTable
import ascii as fl

# Intro Plot
#itr_first_line = ['']
#itr_second_line = ['']
#itr_third_line = ['']
#itr_fours_line = ['']

#
#
#
#




#-----------------------------------------#
# IP Plot
ip_first_line = ['Каждый октет - это десятичное число до точки число до точки.']
ip_second_line = ['Посмотри в таблице ASCII значения и выбери один из двух...']
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



def intro():
    for x in a:
        print(x)
    time.sleep(1)
    for y in globals.b:
        print(y)
    # file1 = open("love_quest.txt", "r", encoding="utf8")
    # lines = file1.readlines()
    # for line in lines:
    #     print(line.strip())
    #     time.sleep(1)
    # file1.close()


def pwd():
        print('ммм, есть проблема, в ядре была создана система аутентификации, так что введи пароль, скорее всего это дата... (если что формат даты ДД.ММ.ГГ)')
        print('Введите пароль:')
        date = '20.03.21'
        date_pwd = input()
        if date_pwd == date:
            print('Так, ты вошла, тут есть ip адреса, к которым надо подключиться, но они зашифрованы...')
        else:
            while date_pwd != date:
                print('Ммм, не, не подходит... Попробуй ещё раз')
                date_pwd = input()
            else:
                print('Так, ты вошла, тут есть ip адреса, к которым надо подключиться, но они зашифрованы...')




def ip_plot():
    # file1 = open("ip_plot.txt", "r", encoding="utf8")
    # lines = file1.readlines()
    # for line in lines:
    #     print(line.strip())
    #     time.sleep(2)
    # file1.close()
    print("\033[32m {}".format(ip_first_line))
    time.sleep(1)
    print("\033[32m {}".format(ip_second_line))
    time.sleep(1)
    print('На, держи, тебе пригодится для разгадки задачи с IP адресами')

    #os.startfile(r'C:\Users\Илья\Downloads\asckii.png')


def ip_addr():
    ip1 = 'mpkq'  #109.112.107.113
    ip2 = 'love'  #108.111.118.101
    print('IP: 109.112.107.113')
    time.sleep(1.5)
    print('IP: 108.111.118.101')
    time.sleep(1.5)
    print('Введи слово, которое получилось из IP-адреса: ')
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

#-------------------------------------------------------------------#
#                                                                   #
#                                                                   #
#                           !Functions!                             #
#                                |                                  #
#                                v                                  #
#-------------------------------------------------------------------#


if __name__ == '__main__':
    # intro()
    # pwd()
<<<<<<< HEAD
    #ip_plot()

    # import ascii as fl
    # fl.ascii_table()
=======
    ip_plot()
    time.sleep(1)
    fl.ascii_table()
>>>>>>> 4e2ccce36596b3c21d6b7a7dedfde17c92e68fb8
    # print("\033[32m {}" .format(ascki_table()))
    # time.sleep(2)
    # ip_addr()

#inst: @ilyanixx13






