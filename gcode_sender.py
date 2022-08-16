import serial
import time

class movement():
    def __init__(self):

        #Feedrate
        self.fdr = 1200

        #Serial communication
        print('\nConnecting...')
        self.g = serial_begin()
        print('GRBL connected\n')

    def move(self, point):

        x = float("{:.3f}".format(point[0]))
        y = float("{:.3f}".format(point[1]))
        z = float("{:.3f}".format(point[2]))

        self.g.flushInput()
        self.g.flushOutput()
        time.sleep(1)

        print(f'Command: X{x} Y{y} Z{z}')

        self.g.write(f'$J = G21 X{x} Y{y} Z{z} F{self.fdr}\n'.encode())

        time.sleep(1)

        self.g.flushOutput()

        inp = self.g.readline().decode().strip()
        if inp == 'ok': print('ok')
        else: print(f'Error: {inp}' + '\n\n' )

    def check_pos(self, point):
        self.g.flushOutput()
        self.g.flushInput()
        self.g.write('?'.encode())
        #time.sleep(1)

        pos = self.g.readline().decode()

        #If a hard limit stop occurs, GRBL will send
        #a message -> [MSG:Reset to continue]
        if pos == '[MSG:Reset to continue]' or pos == 'ALARM 1':
            print('\nHard limits\n')
            exit()

        pos = pos.split('|')
        pos = pos[1]
        pos = pos.split(':')
        pos = pos[1]
        pos = pos.split(',')

        for item in range(len(pos)): pos[item] = float(pos[item])

        x = float("{:.3f}".format(point[0]))
        y = float("{:.3f}".format(point[1]))
        z = float("{:.3f}".format(point[2]))

        if pos[0] == x and pos[1] == y and pos[2] == z: return True
        else: return False

    def home(self):
        print('Homing cycle enabled...')
        self.g.write('$H\n'.encode())
        time.sleep(1)

        self.g.flushOutput()

        while self.g.readline().decode().strip() != 'ok': pass 
        print('Homing cycle completed\n')

        #Close and reopen communication to reset MPos
        self.g.close()
        time.sleep(1)
        self.g = serial_begin()

        pass

    #Close serial communication
    def finish(self):
        self.g.close()

def serial_begin():

    try:
        g = serial.Serial('COM3', 115200)

    except:
        print('Connection error\n')
        exit()


    g.write('\r\n\r\n'.encode())          #Wake up GRBL
    time.sleep(1)    

    g.write('$X\n'.encode())              #Unlock
    time.sleep(1)

    g.flushInput()

    return g