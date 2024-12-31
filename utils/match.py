import numpy as np
import pyautogui
import cv2


template_path = "data\\matchpicture.png"
target_size = (1854, 632)


# 截取屏幕并匹配模板
def capture_and_match_template():
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
        print(f"定位模板 '{template_path}' 路径错误")

    resized_template = cv2.resize(template, target_size)
    result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"窗口定位 '{min_loc}' 已加载")

    return min_loc
