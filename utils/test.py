from activeTargetWindow import activateWindow
from isPlayMode import isPlayMode
import time

if __name__ == "__main__":
    window_title = "原神"
    activateWindow(window_title)
    time.sleep(1)
    templatePath = "./cache/template.png"
    width = 1854
    height = 632
    print(isPlayMode(templatePath, width, height)[1])