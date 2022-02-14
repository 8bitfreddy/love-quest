#!/usr/bin/env python
import os
import time
#import globals
from prettytable import PrettyTable
#import ascii as fl

# Intro Plot
#intro_first_line = ['']
#intro_second_line = ['']
#intro_third_line = ['']
#intro_fours_line = ['']

#
#
#
#
#




#-----------------------------------------#
# IP Plot
ip_first_line = ['Каждый октет - это десятичное число до точки число до точки.']
ip_second_line = ['Посмотри в таблице ASCII значения и выбери IP один из двух...']
#
#
#
#
#a = ["q"]
#
def ascii_table():
    asc_header = ['DEC', 'HEX', 'OCT', 'Char']
    asc_data = ['97', '61',  '141', 'a',
                '98', '62',  '142', 'b',
                '99', '63',  '143', 'c',
                '100', '64', '144', 'd',
                '101', '65', '145', 'e',
                '102', '66', '146', 'f',
                '103', '67', '147', 'g',
                '104', '68', '150', 'h',
                '105', '69', '151', 'i',
                '106', '6A', '152', 'j',
                '107', '6B', '153', 'k',
                '108', '6C', '154', 'l',
                '109', '6D', '155', 'm',
                '110', '6E', '156', 'n',
                '111', '6F', '157', 'o',
                '112', '70', '160', 'p',
                '113', '71', '161', 'q',
                '114', '72', '162', 'r',
                '115', '73', '163', 's',
                '116', '74', '164', 't',
                '117', '75', '165', 'u',
                '118', '76', '166', 'v',
                '119', '77', '167', 'w',
                '120', '78', '170', 'x',
                '121', '79', '171', 'y',
                '122', '7A', '172', 'z',
                ]

    columns = len(asc_header)

    asc_table = PrettyTable(asc_header)

    data = asc_data[:]
    while data:
        asc_table.add_row(data[:columns])
        data = data[columns:]
    #print(asc_table)
    print("\033[32m {}".format(asc_table))





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



def close_prog():
    print("\033[32m {}".format('Чтобы выйти, нажми Q'))
    cls = input()
    while cls != 'q':
        cls = input()
    print("\033[32m {}".format('Пока'))

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

    #ip_plot()

    # import ascii as fl
    # fl.ascii_table()

    #ip_plot()
    time.sleep(1)
    ascii_table()
    #fl.ascii_table()

    # print("\033[32m {}" .format(ascki_table()))
    # time.sleep(2)
    # ip_addr()
    close_prog()

#inst: @ilyanixx13






