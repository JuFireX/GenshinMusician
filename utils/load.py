# 加载乐谱文件
def load_musical_score(filename):
    musical_score = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                musical_score.append(tuple(line))
            print(f"乐谱文件 '{filename}' 加载成功")
    except FileNotFoundError:
        print(f"乐谱文件 '{filename}' 路径错误")
    except Exception as e:
        print(f"乐谱文件 '{filename}' 加载失败: {e}")

    return musical_score