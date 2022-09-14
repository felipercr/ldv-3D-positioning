from gcode_sender import *
from points_matrix import *
from menu import menu

def main():
    m = movement()

    while True: menu(m)

if __name__ == "__main__":
    main()
