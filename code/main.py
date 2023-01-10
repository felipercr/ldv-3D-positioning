from gcode_sender import *
from points_matrix import *
from menu import menu
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    m = movement()

    while True: menu(m)

if __name__ == "__main__":
    if is_admin(): main()
    else: ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

