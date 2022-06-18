import serial
import time

class movement():
    def __init__(self, g):

        #Feedrate
        self.fdr = 1200

        #Serial communication
        self.g = g

    def move(self, point):

        x = float("{:.3f}".format(point[0]))
        y = float("{:.3f}".format(point[1]))
        z = float("{:.3f}".format(point[2]))

        self.g.flushInput()

        print(f'Command: X{x} Y{y} Z{z}')

        self.g.write(f'$J = G21 X{x} Y{y} Z{z} F{self.fdr}\n'.encode())

        time.sleep(1)

        self.g.flushOutput()

        inp = self.g.readline().decode().strip()
        if inp == 'ok': print('ok')
        else: print('Error' + '\n\n')

    def check_pos(self, point):
        self.g.flushOutput()
        self.g.flushInput()
        self.g.write('?'.encode())
        #time.sleep(1)

        pos = self.g.readline().decode()
        pos = pos[11:27]
        pos = pos.split(',')
        for item in range(len(pos)): pos[item] = float(pos[item])

        x = float("{:.3f}".format(point[0]))
        y = float("{:.3f}".format(point[1]))
        z = float("{:.3f}".format(point[2]))

        if pos[0] == x and pos[1] == y and pos[2] == z: return True
        else: return False

    def home(self):
        self.g.write('$H\n'.encode())
        time.sleep(1)

        inp = self.g.readline().decode().strip()
        pass

def serial_begin():
    print('\nConnecting...')

    try:
        g = serial.Serial('COM5', 115200)

    except:
        print('Connection error\n')
        exit()


    g.write('\r\n\r\n'.encode())          #Wake up GRBL
    time.sleep(1)    

    g.write('$X\n'.encode())              #Unlock
    time.sleep(1)

    g.flushInput()
    print('GRBL connected\n')
    return g