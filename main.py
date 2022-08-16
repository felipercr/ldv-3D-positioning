from gcode_sender import *
from points_matrix import *

def main():
    m = movement()

    matrix = points_matrix()

    m.home()

    for line in matrix:
        m.move(line)
        while m.check_pos(line) == False: pass

        #################LASER#################
        #################LASER#################

        print('Chegou\n')
        time.sleep(1)

    m.finish()

if __name__ == "__main__":
    main()
