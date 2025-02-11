import sys
import os
import win32api
import ctypes


def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        return e


def getAdmin():
    if isAdmin()!= 0 or 1:
        print(isAdmin())
        os.system("pause")
        return
    if not isAdmin():
        win32api.ShellExecute(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        os.system("exit")
    else:
        os.system("pause")
        while True:
            print(isAdmin())


if __name__ == "__main__":
    getAdmin()
    