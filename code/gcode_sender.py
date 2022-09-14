from os import system, path
import serial
import serial.tools.list_ports
import time
from points_matrix import points_matrix

class movement():
    def __init__(self):

        self.log_path = '../log.txt'

        system('cls')

        #Serial communication
        while True:
            print('Connecting...\n')

            ports = serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                print(f"{port}")

            self.com_number = input('Select a serial port: ')
            if self.com_number.isnumeric() == False:
                system('cls')
                print('Invalid port, insert a numeric value\n')
            else: break

        
        self.g = serial_begin(self.com_number)
        print('\nGRBL connected\n')

        time.sleep(1)

        system('cls')

        if path.exists(self.log_path) == False:
            with open(self.log_path, 'w') as log:
                log.write(f'Zero (x,y,z): 0 0 0\n')
                log.write(f'Feedrate (mm/s): 1000\n')
                log.write(f'Last Position (x,y,z): 0 0 0\n')
                log.write('\n--------------------------------------\n\n')
                log.write('Given of commands: \n\n')

        with open(self.log_path, 'r') as log:
            lines = log.readlines()
            lines = lines[1]
            lines = lines.split()
            self.fdr = lines[2]


    def move(self, point):

        x = float("{:.3f}".format(float(point[0])))
        y = float("{:.3f}".format(float(point[1])))
        z = float("{:.3f}".format(float(point[2])))

        self.g.flushInput()
        self.g.flushOutput()
        #time.sleep(1)

        print(f'Command: X{x} Y{y} Z{z}')

        with open(self.log_path, 'r') as log:
            lines = log.readlines()
        
        feedrate = lines[1]
        feedrate = feedrate.split()
        feedrate = feedrate[2]
        self.fdr = feedrate

        lines.append(f'X{x} Y{y} Z{z}\n')

        with open(self.log_path, 'w') as log:
            for line in lines:
                log.write(line)

        self.g.write(f'$J = G21 X{x} Y{y} Z{z} F{self.fdr}\n'.encode())

        #time.sleep(1)

        self.g.flushOutput()

        inp = self.g.readline().decode().strip()
        if inp == 'ok': print('ok')
        else: print(f'Error: {inp}' + '\n\n' )

        while self.check_pos(point) == False: pass

    def check_pos(self, point):
        self.g.flushOutput()
        self.g.flushInput()
        self.g.write('?'.encode())

        pos = self.g.readline().decode()

        #If a hard limit stop occurs, GRBL will send
        #a message -> [MSG:Reset to continue]
        if pos == '[MSG:Reset to continue]' or pos == 'ALARM 1':
            print('\nHard limits\n')
            print('Re-homing is highly recommended!\n')
            while True: pass

        pos = pos.split('|')
        try:
            pos = pos[1]
        except:
            print('\nError, probably due to hard limits')
            print('Re-homing is highly recommended!\n')
            while True: pass
        pos = pos.split(':')
        pos = pos[1]
        pos = pos.split(',')

        for item in range(len(pos)): pos[item] = float(pos[item])

        x = float("{:.3f}".format(float(point[0])))
        y = float("{:.3f}".format(float(point[1])))
        z = float("{:.3f}".format(float(point[2])))

        with open(self.log_path, 'r') as log:
            lines = log.readlines()

        with open(self.log_path, 'w') as log:
            for n, line in enumerate(lines):
                if n == 2:
                    log.write(f'Last Position (x,y,z): {pos[0]} {pos[1]} {pos[2]}\n')
                else:
                    log.write(line)

        if pos[0] == x and pos[1] == y and pos[2] == z: return True
        else: return False

    def home(self):
        print('Homing cycle enabled...')
        self.g.write('$H\n'.encode())
        #time.sleep(1)

        self.g.flushOutput()

        while self.g.readline().decode().strip() != 'ok': pass 

        #Close and reopen communication to reset MPos
        self.g.close()
        #time.sleep(1)
        self.g = serial_begin(self.com_number)

        with open(self.log_path, 'r') as log:
            lines = log.readlines()
        
        lines.append('Homing cycle\n')
        lines.append('Reset MPos\n')

        with open(self.log_path, 'w') as log:
            for line in lines:
                log.write(line)

        print('Homing cycle completed\n')

    def full_cycle(self):
        with open(self.log_path, 'r') as log:
            lines = log.readlines()

        with open(self.log_path, 'w') as log:
            lines = lines[0:8]
            for line in lines:
                log.write(line)

        self.home()
        self.move_to_zero()

        #time.sleep(1)

        matrix = points_matrix()

        n_points = len(matrix)
        completed = 0

        for line in matrix:
            self.move(line)
            while self.check_pos(line) == False: pass

        #################LASER#################
        #################LASER#################

            completed = completed + 1

            print(f'Done - {completed} / {n_points}\n')
            time.sleep(0.2)

        print('Full cycle completed!')

        with open(self.log_path, 'r') as log:
            lines = log.readlines()
        
        lines.append('Full cycle completed!\n')

        with open(self.log_path, 'w') as log:
            for line in lines:
                log.write(line)

        time.sleep(2)

    def set_zero(self):

        system('cls')
        while True:
            x = input('Select x: ')

            try: 
                if float(x) < 0:
                    system('cls')
                    print('Select a valid number\n')
                else: break

            except:
                system('cls')
                print('Select a valid number\n')

        system('cls')
        while True:
            y = input('Select y: ')
            
            try: 
                if float(y) < 0:
                    system('cls')
                    print('Select a valid number\n')
                else: break

            except:
                system('cls')
                print('Select a valid number\n')

        system('cls')
        while True:
            z = input('Select z: ')
            
            try: 
                if float(z) < 0:
                    system('cls')
                    print('Select a valid number\n')
                else: break

            except:
                system('cls')
                print('Select a valid number\n')

        with open(self.log_path, 'r') as log:
            lines = log.readlines()

        with open(self.log_path, 'w') as log:
            for n, line in enumerate(lines):
                if n == 0:
                    log.write(f'Zero (x,y,z): {x} {y} {z}\n')
                
                else: 
                    log.write(line)

    def set_feedrate(self):
        
        system('cls')
        while True:
            f = input('Select a Feedrate (mm/s): ')
            try: 
                if float(f) < 0:
                    system('cls')
                    print('Select a valid number\n')
                else: break

            except:
                system('cls')
                print('Select a valid number\n')

        with open(self.log_path, 'r') as log:
            lines = log.readlines()

        with open(self.log_path, 'w') as log:
            for n, line in enumerate(lines):
                if n == 1:
                    log.write(f'Feedrate (mm/s): {f}\n')
                
                else: 
                    log.write(line)

    def last_loc(self):
        pass

    def move_to_zero(self):
        with open(self.log_path, 'r') as log:
            lines = log.readlines()
            lines = lines[0]
            lines = lines.split()
            x = lines[2]
            y = lines[3]
            z = lines[4]

            point = (x, y, z)

        self.move(point)

        #Close and reopen communication to reset MPos
        self.g.close()
        #time.sleep(1)
        self.g = serial_begin(self.com_number)

        with open(self.log_path, 'r') as log:
            lines = log.readlines()
        
        lines.append('Reset MPos\n')

        with open(self.log_path, 'w') as log:
            for line in lines:
                log.write(line)

        print('Done - Move to zero and reset MPos\n')

    #Close serial communication
    def finish(self):
        self.g.close()

def serial_begin(com_number):

    try:
        g = serial.Serial(f'COM{com_number}', 115200, timeout = 2)

    except:
        print(f'\nConnection error, please check COM{com_number} and restart the program!\n')
        while True: pass


    g.write('\r\n\r\n'.encode())          #Wake up GRBL
    time.sleep(1)    

    g.write('$X\n'.encode())              #Unlock
    time.sleep(1)

    g.flushInput()

    return g