import pyautogui
import time


def simulate_key_presses(events):
    start_time = time.time()

    for event in events:
        # 计算当前事件的目标执行时间
        target_time = start_time + event[0]
        # 计算需要等待的时间
        delay = target_time - time.time()

        if delay > 0:
            time.sleep(delay)

        # 使用pyautogui按下并释放按键
        pyautogui.hotkey(*event[1])


# 示例用法
events = [
    (0.0, ("E",)),
    (0.5, ("E",)),
    (1.0, ("G",)),
    (1.5, ("E",)),
    (2.0, ("W",)),
    (2.166666666666668, ("A", "D", "G")),
    (2.333333333333336, ("T",)),
    (2.5, ("W",)),
    (3.0, ("E",)),
]


simulate_key_presses(events)
