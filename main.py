import argparse
import json

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    2. -s 为可选参数，用于显示题库中的所有题目
    3. -a 为可选参数，用于选择题库中的某一篇文章，需要提供对应的文章编号
    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-s", "--show", help="显示题库中的所有题目", action="store_true")
    parser.add_argument("-a", "--article", help="选择题库中的某一篇文章", type=int)

    args = parser.parse_args()
    return args


def read_article(filename):
    """
    读取题库文件
    :param filename: 题库文件名
    :return: 题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def display_article(articles):
    """
    显示题库中的所有题目及其编号
    :param articles: 题库中文章
    """
    for article in articles:
        print(f"{article['number']}.{article['title']}")


def select_article(articles, number):
    """
    选择题库中的某一篇文章
    :param articles: 题库中文章
    :param number: 文章编号
    :return: 选择的文章
    """
    articles = data["articles"]
    if number < 1 or number > len(articles):
        print("文章编号无效！")
        return None
    return articles[number-1]


def get_inputs(hints):
    """
    获取用户输入
    :param hints: 提示信息
    :return: 用户输入的单词
    """
    keys = []
    i=1
    for hint in hints:
        word = input(f"请在{{{{{i}}}}}处填写{hint}:")
        keys.append(word)
    return keys


def replace(article, keys):
    """
    替换文章内容
    :param article: 文章内容
    :param keys: 用户输入的单词
    :return: 替换后的文章内容
    """
    for i in range(len(keys)):
        article = article.replace(f"{{{{{i+1}}}}}", keys[i])
    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_article(args.file)
    articles = data["articles"]
    if args.show:
        display_article(articles)
    elif args.article:
        article = select_article(articles, args.article)
        if article:
            hints = article["hints"]
            content = article["article"]
            print()
            print(content)
            print()
            keys = get_inputs(hints)
            replaced_content = replace(content, keys)
            print()
            print(replaced_content)
            print()
            print("参考答案:")
            print(article["answer"])
    else:
        print("请提供合适的参数！")
