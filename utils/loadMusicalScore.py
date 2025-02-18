import re

def loadScore(filename):
    context = ""
    score = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = re.sub(r"/", "", line)
            context += line
    i = 0
    while i < len(context):
        if context[i] == "(":
            temp = ""
            j = 1
            while context[i + j] != ")":
                temp += context[i + j]
                j += 1
            score.append(tuple(temp))
            i += j + 1
        else:
            score.append(tuple(context[i]))
            i += 1
    return score


if __name__ == "__main__":
    filename = "F:\Code Projects\_Local Projects\GenshinMusician\songs\欢乐颂.txt"
    testscore = []

    try:
        testscore = loadScore(filename)
        print(f"乐谱文件 '{filename}' 加载成功")
    except FileNotFoundError:
        print(f"乐谱文件 '{filename}' 路径错误")
    except Exception as e:
        print(f"乐谱文件 '{filename}' 加载失败: {e}")

    print(testscore)
