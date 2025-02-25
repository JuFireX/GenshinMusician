import cv2
import numpy as np
import pyautogui


def match(path):
    screenshot = pyautogui.screenshot()
    img = np.array(screenshot)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 进行中值滤波，去除噪声
    gray = cv2.medianBlur(gray, 5)
    # 边缘检测
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    # 霍夫圆变换
    circles = cv2.HoughCircles(
        edges,
        cv2.HOUGH_GRADIENT,
        1,
        20,
        param1=50,
        param2=30,
        minRadius=60,
        maxRadius=75,
    )
    circles_roi = []
    # 确保检测到了圆形
    if circles is not None:
        # 转换为整数类型
        circles = np.uint16(np.around(circles))
        # 绘制圆形
        for i in circles[0, :]:
            x, y, r = i[0], i[1], i[2]
            # 提取圆形图像
            circle_roi = gray[y - r : y + r, x - r : x + r]
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)
            # 设定匹配阈值
            circles_roi.append(circle_roi)
    else:
        return (False, f"匹配失败1")
    # cv2.imshow('Detected Circles', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    template = cv2.imread(path)
    template = cv2.resize(template, (1464, 160))
    img_template = np.array(template)
    # 转换为灰度图
    gray_template = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
    # 进行中值滤波，去除噪声
    gray_template = cv2.medianBlur(gray_template, 5)
    # 边缘检测
    edges_template = cv2.Canny(gray_template, 50, 150, apertureSize=3)
    # 霍夫圆变换
    circles_template = cv2.HoughCircles(
        edges_template,
        cv2.HOUGH_GRADIENT,
        1,
        20,
        param1=50,
        param2=30,
        minRadius=60,
        maxRadius=75,
    )
    circles_roi_template = []
    if circles_template is not None:
        # 转换为整数类型
        circles_template = np.uint16(np.around(circles_template))
        # 绘制圆形
        for i in circles_template[0, :]:
            x, y, r = i[0], i[1], i[2]
            # 提取圆形图像
            circle_roi = gray_template[y - r : y + r, x - r : x + r]
            cv2.circle(img_template, (x, y), r, (0, 255, 0), 2)
            # 设定匹配阈值
            circles_roi_template.append(circle_roi)
    else:
        return (False, f"匹配失败2")
    # cv2.imshow('Detected Circles', img_template)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    for i in circles_roi:
        for j in circles_roi_template:
            result = cv2.matchTemplate(i, j, cv2.TM_CCOEFF_NORMED)
            max_val, min_val, max_loc, min_loc = cv2.minMaxLoc(result)
            threshold = 0.7
            if max_val >= threshold:
                return (True, f"匹配成功，匹配值{max_val}")
    return (False, f"匹配失败，匹配值{max_val}")
if __name__ == "__main__":
    print(match(f"cache\\piano.png")[1])

