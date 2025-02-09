from win32 import win32gui
from win32.lib import win32con


def activateWindow(window_title):
    # 查找窗口句柄
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        # 激活窗口
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        win32gui.SetForegroundWindow(hwnd)
        print(f"窗口 {window_title} 已激活")
    else:
        print(f"窗口 {window_title} 未找到")


if __name__ == "__main__":
    window_title = "原神"
    activateWindow(window_title)
