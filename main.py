import utils.admin as admin
import utils.match as match
import utils.load as load

import pyautogui
import threading
import time


# 主循环
def mainloop(stop, click_location, musical_score, tik):
    try:
        pyautogui.click(click_location)
    except pyautogui.FailSafeException:
        print("激活窗口失败")
        stop.set()
        return
    except Exception as e:
        print(f"激活窗口失败 {e}")
        stop.set()
        return
    
    print("开始演奏···")
    for chord in musical_score:
        if stop.is_set():
            break
        pyautogui.hotkey(*chord)
        time.sleep(tik)
    stop.set()


# 程序入口
if __name__ == "__main__":
    # admin.run_as_admin()
    tik = 0.1
    path = "songs\\test.txt"
    stop = threading.Event()

    scores = load.load_musical_score(path)
    click = match.capture_and_match_template()

    if click is not None and scores:
        # 创建并启动线程
        mainloop_thread = threading.Thread(target=mainloop, args=(stop, click, scores, tik))
        mainloop_thread.start()

        time.sleep(60)  # 等待加载完毕
        stop.set()  # 设置事件，通知线程停止
        mainloop_thread.join()  # 等待线程结束
        print("演奏结束")
    else:
        print("未找到原神窗口或歌曲文件为空")

    print("程序结束")

"""





"""
