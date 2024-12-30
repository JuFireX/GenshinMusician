import tkinter as tk
from tkinter import scrolledtext
import log

path = "res\\test.txt"
bpm = 120


# 运行 GUI 界面
def run_gui():
    # 创建窗口
    root = tk.Tk()
    root.geometry("600x800+100+100")
    root.resizable(False, False)
    root.title("Genshin Musician")

    # 获取路径
    label_path = tk.Label(root, text="请输入乐谱路径")
    label_path.pack(padx=(0, 300), pady=(30, 10))

    entry_path = tk.Entry(root, width=25, font=("Arial", 12))
    path = tk.Entry.get(entry_path)
    entry_path.pack(padx=(0, 10), pady=(10, 15))

    # 获取速度
    label_bpm = tk.Label(root, text="请输入歌曲速度")
    label_bpm.pack(padx=(0, 300), pady=(10, 10))

    entry_bpm = tk.Entry(root, width=25, font=("Arial", 12))
    bpm = tk.Entry.get(entry_bpm)
    entry_bpm.pack(padx=(0, 10), pady=(10, 15))

    # 日志框
    label_path = tk.Label(root, text="启动日志")
    label_path.pack(padx=(0, 360), pady=(10, 10))

    log_text = scrolledtext.ScrolledText(root, width=30, height=10, state="disabled")
    log_text.pack(side=tk.TOP, padx=(10, 10), pady=(10, 10))

    # 配置日志记录
    log.setup_logging(log_text)

    button_run = tk.Button(root, text="  Run ")
    button_run.pack(side=tk.RIGHT, padx=(30, 70))

    button_stop = tk.Button(root, text=" Stop ")
    button_stop.pack(side=tk.RIGHT, padx=(30, 30))

    root.mainloop()


if __name__ == "__main__":
    run_gui()

