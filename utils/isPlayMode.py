import cv2
import pyautogui
import numpy as np


def isPlayMode(templatePath, width, height):
    templateSize = (width, height)

    screenshot = np.array(pyautogui.screenshot())
    template = cv2.imread(templatePath)
    if template is None:
        return (False, f"定位模板 '{templatePath}' 路径错误")

    resized_template = cv2.resize(template, templateSize)
    result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if min_val > 0.2:
        return (False, f"当前未处于演奏界面")

    return (True, f"定位模板匹配成功")


if __name__ == "__main__":
    templatePath ="./cache/template.png"
    width = 1854
    height = 632
    print(isPlayMode(templatePath, width, height)[1])
