import ctypes
import sys


def is_admin() -> bool:
    """
    检查当前是否以管理员权限运行。

    :return: 如果是管理员权限返回 True，否则返回 False
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def check_admin_permission() -> None:
    """
    确保脚本以管理员权限运行。如果不是，则尝试以管理员身份重新启动脚本。
    """
    if not is_admin():
        # 以管理员身份重新运行脚本
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()
    print("已经是管理员权限运行")
