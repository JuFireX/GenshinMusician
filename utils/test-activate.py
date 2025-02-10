from activeTargetWindow import activateWindow
from isPlayMode import isPlayMode
import time

if __name__ == "__main__":
    window_title = "任务管理器"
    activateWindow(window_title)
    time.sleep(1)
    templatePath = "./cache/template0.png"
    width = 1906
    height = 1258
    print(isPlayMode(templatePath, width, height)[1])