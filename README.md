# sast2023 word game

## 环境配置

目前没有第三方依赖项

## 使用设置

约定以下参数：

```
1. -f 为必选参数，表示输入题库文件。
2. -s 为可选参数，用于显示题库中的所有题目。
3. -a 为可选参数，用于选择题库中的某一篇文章，需要提供对应的文章编号。
例如:
python main.py -f example.json -s 可以显示题库中的所有题目的编号和标题。
python main.py -f example.json -a 1 可以指定第1篇文章。

```

文章使用 JSON 存储，的格式如下：

```json
{
    "language": "zh",
    "articles": [
        {
            "number": ,
            "title": ,
            "article": ,
            "hints": [],
	    "answer": 
        }
    ]
}
```

## 游戏功能

完成了作业要求的基本功能。
