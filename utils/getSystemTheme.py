import winreg


def getSystemTheme():
    try:
        # 打开注册表项
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
            0,
            winreg.KEY_READ,
        )

        # 查询注册表值
        value = winreg.QueryValueEx(key, "SystemUsesLightTheme")[0]

        # 关闭注册表项
        winreg.CloseKey(key)

        return value
    except FileNotFoundError:
        print("注册表项未找到")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None


if __name__ == "__main__":
    theme = getSystemTheme()

    if theme is not None:
        if theme == 1:
            print("当前主题是亮色模式。")
        elif theme == 0:
            print("当前主题是暗色模式。")
        else:
            print("无法确定当前主题。")
    else:
        print("无法获取主题信息。")
