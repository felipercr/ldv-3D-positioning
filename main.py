from gcode_sender import *
from points_matrix import *

def main():
    g = serial_begin()

    m = movement(g)

    matrix = points_matrix()

    for line in matrix:
        m.move(line)
        while m.check_pos(line) == False: pass
        print('Chegou\n')
        time.sleep(1)

    g.close()

if __name__ == "__main__":
    main()
