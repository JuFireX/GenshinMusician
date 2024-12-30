import logging
import tkinter as tk


# 重定义 Handler
class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.configure(state="normal")  # 允许编辑
        self.text_widget.insert(tk.END, msg + "\n")  # 插入日志消息
        self.text_widget.configure(state="disabled")  # 禁止编辑
        self.text_widget.yview(tk.END)  # 自动滚动到底部


# 配置 logging
def setup_logging(log_text):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置日志级别

    # 创建自定义 Handler 并添加到 logging
    text_handler = TextHandler(log_text)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    text_handler.setFormatter(formatter)
    logger.addHandler(text_handler)


# 重定向
def log_info(msg):
    logging.info(msg)


def log_error(msg):
    logging.error(msg)


def log_warning(msg):
    logging.warning(msg)


def log_debug(msg):
    logging.debug(msg)


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import scrolledtext
    import log  # 导入 log.py 文件

    # 创建主窗口
    root = tk.Tk()
    root.title("日志记录示例")

    # 创建一个 ScrolledText 控件用于显示日志
    log_text = scrolledtext.ScrolledText(root, state="disabled", width=80, height=20)
    log_text.pack(padx=10, pady=10)

    # 配置日志记录
    log.setup_logging(log_text)

    # 添加按钮用于测试日志记录
    def test_logging():
        log.log_info("这是一条 INFO 级别的日志")
        log.log_error("这是一条 ERROR 级别的日志")
        log.log_warning("这是一条 WARNING 级别的日志")
        log.log_debug("这是一条 DEBUG 级别的日志")

    test_button = tk.Button(root, text="测试日志记录", command=test_logging)
    test_button.pack(pady=10)

    # 运行主循环
    root.mainloop()
