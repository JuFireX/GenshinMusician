from utils.admin import check_admin_permission
from utils.image_processing import find_template_location, play_musical_score


def main():
    check_admin_permission()

    # 获取模板匹配位置
    template_path = "data/matchpicture.png"
    min_loc = find_template_location(template_path)

    # 播放音符
    tik = float(input("请输入每个音符的时长："))
    filename = input("请输入音符文件名：")
    play_musical_score(min_loc, tik, filename)


if __name__ == "__main__":
    main()
