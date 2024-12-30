from gui import run_gui
from gui import bpm, path
import log
import numpy as np
import time
import ctypes
import sys
import pyautogui
import cv2


# 检查管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# 以管理员身份运行
def run_as_admin():
    if is_admin():
        log.log_info("已经是管理员权限运行")
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


# 截取屏幕并匹配模板
def capture_and_match_template(template_path, target_size):
    """
    截取屏幕、加载并调整模板图片，然后匹配模板位置。用以定位原神窗口。

    参数:
        template_path (str): 模板图片的路径。
        target_size (tuple): 模板图片的目标大小 (width, height)。

    返回:
        min_loc (tuple): 模板在截图中的左上角位置 (x, y)。

    """
    screenshot = np.array(pyautogui.screenshot())
    template = cv2.imread(template_path)
    if template is None:
        log.log_error(f"定位模板 '{template_path}' 路径错误")

    resized_template = cv2.resize(template, target_size)
    result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    log.log_info(f"原神窗口定位 '{min_loc}' 加载成功")

    return min_loc


# 加载乐谱文件
def load_musical_score(filename):
    musical_score = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                musical_score.append(tuple(line))
            log.log_info(f"乐谱文件 '{filename}' 加载成功")
    except FileNotFoundError:
        log.log_error(f"乐谱文件 '{filename}' 路径错误")
    except Exception as e:
        log.log_error(f"乐谱文件 '{filename}' 加载失败: {e}")

    return musical_score


# 播放乐谱
def play_musical_score(musical_score, tik, click_location):
    pyautogui.click(click_location)
    for chord in musical_score:
        pyautogui.hotkey(*chord)
        time.sleep(tik)


# 主函数
def main():
    try:
        # 加载乐谱文件 需要path和tik两个参数
        tik = bpm / 6000
        musical_score_path = path
        musical_score = load_musical_score(musical_score_path)

        # 定位原神窗口
        template_path = "res\\matchpicture.png"
        target_size = (1854, 632)
        click_location = capture_and_match_template(template_path, target_size)

        # 播放乐谱
        log.log_info("开始播放乐谱···")
        play_musical_score(musical_score, tik, click_location)

    except FileNotFoundError as e:
        log.log_error(f"存在文件路径错误: {e}")
    except Exception as e:
        log.log_error(f"发生未知错误: {e}")


# 程序入口
if __name__ == "__main__":
    run_as_admin()
    run_gui()
    main()
