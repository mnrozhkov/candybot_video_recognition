#!/usr/bin/env python3

import speech_recognizer as sr


import random
import logging

logging.basicConfig(filename='Bache.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


#----------------------Bache------------------------

items = 15
max_at_step = 3
taken_items = 0
good_strategy = False
last_human_step = 0

def print_items():
    '''Print string items representation
    '''
    
    global items
    
    obj_str = ''
    obj_str += str(items) + ':'
    for i in range(0,items):
        obj_str += '|'
    print(obj_str)


def find_strategy(m, n):
    k = (m - 1) - (n + 1) * ((m - 1) // (n + 1))
    return k


def computer_step():
    '''Computer does step
    '''
    
    global items
    global max_at_step
    global taken_items
    global good_strategy
    global last_human_step
    
    print('Ходит компьютер...')
    if items > 1:
        if (items + taken_items) / (taken_items + 1) > 2:
            comp_step = random.randint(1,min(max_at_step,items-1))
            items -= comp_step
            taken_items += comp_step
            print_items()
        else:
            if good_strategy:
                comp_step = (max_at_step + 1) - last_human_step
                items -= comp_step
                print_items()
            else:
                k = find_strategy(items, max_at_step)
                if k == 0:
                    k = random.randint(1,min(max_at_step,items-1))
                else:
                    good_strategy = True
                items -= k
                print_items()
    else:
        if items == 1:
            print('Человек победил')
        elif items <= 0:
            print('Компьютер победил')
        return
    
    human_step()


number = {'один': 1, 'два': 2, 'три': 3}


def human_step():
    '''Human does step
    '''
    
    global items
    global max_at_step
    global taken_items
    global last_human_step
    
    print('Ходит человек...')
    if items > 1:
        step = sr.listen()
        if number[step] < 1 or number[step] > max_at_step or not (step in number.keys()):
            human_step()
            return
        items -= number[step]
        if (items + taken_items) / (taken_items + 1) > 2:
            taken_items += number[step]
        last_human_step = number[step]
        print_items()
    else:
        print("Компьютер победил")
        return

    computer_step()
    
#----------------------Bache------------------------


def choose_player():
    '''Chooses first player
    '''
    
    print('Назовите первого игрока (я - человек, компьютер - компьютер): ')
    fst_player = sr.listen()
    if fst_player == 'компьютер':
        computer_step()
    elif fst_player == 'я':
        human_step()
    else:
        choose_player()
    
def main(objs=15):
    global items
    sr.min_rms = 500
    if sr.init('ru-ru', 'Bache.dic', 'Bache.lm.bin'):
        items = objs
        print_items()
        choose_player()

if __name__ == '__main__':
    main()
