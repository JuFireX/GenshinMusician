from activateTargetWindow import activate
from isPlayMode import isPlayMode
import time


if __name__ == "__main__":
    window_title = "原神"
    templatePath = "./cache/template.png"
    isActive, msg = activate(window_title)
    if isActive:
        print(msg)
        isPlay, msg = isPlayMode(templatePath)
        if isPlay:
            print(msg)
            print(True)
        else:
            print(msg)
            print(False)
    else:
        print(msg)
        print(False)
