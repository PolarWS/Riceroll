from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173'])

@app.route('/')
def hello_world():
    return "hellow world"

@app.route('/frindLinkPage')
def hello_world2():
    a2 = [random.randint(1, 510) for _ in range(5)]
    return {"status":200,"ping":a2}

@app.route('/articlePage')
def hello_world3():
    return {"status":200,"data":[{
                "title": "标题标题标题标题标题标题标题标题标题标题标题标题标题2标题2标题2标题2",
                "date": "2020-01-01",
                "label": ["日常"],
                "url": "文章链接",
                "content": "文章内容文章内容文章内容文章内容文章内容文章内容文章内容文章内容",
                "img": "src/components/img/3.jpg",
            },
            {
                "title": "标题标题标题",
                "date": "2020-01-01",
                "label": ["代码", "计算机"],
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/4.png",
            },
            {
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "label": ["相机", "数码"],
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/1.jpg",
            },
            {
                "title": "标题标题标题",
                "date": "2020-01-01",
                "label": ["代码", "计算机"],
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/4.png",
            },
            {
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "label": ["相机", "数码"],
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/1.jpg",
            },
            {
                "title": "标题4",
                "date": "2020-01-01",
                "label": ["日常"],
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/2.png",
            }]}

if __name__ == '__main__':
    app.run()