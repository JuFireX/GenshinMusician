def loadScore(filename):
    score = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            score.append(tuple(line))
    return score


if __name__ == "__main__":
    filename = "./songs/test.txt"
    testscore = []

    try:
        testscore = loadScore(filename)
        print(f"乐谱文件 '{filename}' 加载成功")
    except FileNotFoundError:
        print(f"乐谱文件 '{filename}' 路径错误")
    except Exception as e:
        print(f"乐谱文件 '{filename}' 加载失败: {e}")

    print(testscore)
