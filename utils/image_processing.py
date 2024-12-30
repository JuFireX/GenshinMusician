import cv2
import pyautogui
import numpy as np
import time
from typing import List, Tuple


def find_template_location(template_path: str) -> Tuple[int, int]:
    """
    在屏幕中查找模板图片的位置。

    :param template_path: 模板图片的路径
    :return: 模板图片在屏幕中的位置 (x, y)
    """
    screenshot = np.array(pyautogui.screenshot())
    template = cv2.imread(template_path)
    if template is None:
        raise FileNotFoundError(f"模板图片未找到: {template_path}")

    # 调整模板图片大小
    new_template = cv2.resize(template, (1854, 632))
    result = cv2.matchTemplate(screenshot, new_template, cv2.TM_SQDIFF_NORMED)
    _, _, min_loc, _ = cv2.minMaxLoc(result)
    return min_loc


def play_musical_score(min_loc: Tuple[int, int], tik: float, filename: str) -> None:
    """
    根据音符文件播放音乐。

    :param min_loc: 模板图片在屏幕中的位置 (x, y)
    :param tik: 每个音符的间隔时间
    :param filename: 音符文件的路径
    """
    pyautogui.click(min_loc)
    try:
        with open(filename, "r", encoding="utf-8") as file:
            musical_score: List[Tuple[str, ...]] = [
                tuple(line.strip()) for line in file
            ]
    except FileNotFoundError:
        print(f"音符文件未找到: {filename}")
        return

    pyautogui.click(min_loc)
    for keys in musical_score:
        pyautogui.hotkey(*keys)
        time.sleep(tik)
