from os import system
from gcode_sender import *

def menu(m):

    system('cls')

    while True:
        print('Menu:')
        print('  1. Full cycle (Remember to open BSA Flow)')
        print('  2. Home machine')
        print('  3. Set zero')
        print('  4. Set feedrate\n')
        #print('  5. Start from the last location\n')
        opt = input('Select option: ')

        if opt.isnumeric():
            if int(opt) > 4 or int(opt) == 0:
                system('cls')
                print('Invalid option\n')
            else: break

        system('cls')
        print('Invalid option\n')

    system('cls')

    match opt:
        case '1':
            m.full_cycle()
        case '2':
            m.home()
        case '3':
            m.set_zero()
        case '4': 
            m.set_feedrate()
        #case '5':
            #m.last_loc()