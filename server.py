from flask import Flask, jsonify
import markdown_code_blocks
from flask_cors import CORS
import random
import markdown
import os
import time
from markdown_code_blocks import highlight

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173'])

@app.route('/')
def hello_world():
    return "hellow world"

@app.route('/frindLinkPage')
def hello_world2():
    a2 = [random.randint(1, 510) for _ in range(5)]
    return {"status":200,"ping":a2}

@app.route('/md')
def hello_world4():
    with open('test.md', 'r', encoding='utf-8') as file:
        content = file.read()
    md = {
            "status":200,
            "title": {
                "content": "这是一个md",
                "img": "http://127.0.0.1:5173/src/img/4.webp"
            },
            # "md": highlight(content),
            "md": content,
            "date": "2021-01-01",
            "wordCount": "1000",
        }
    return jsonify(md)
    

@app.route('/articlePage')
def hello_world3():
    # 延迟1S
    time.sleep(1)
    return {"status":200,"data":[{
                "id":1,
                "title": "标题标题标题标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容文章内容文章内容文章内容文章内容文章内容文章内容文章内容",
                "img": "src/img/2.webp",
            },
            {
                "id":2,
                "title": "标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/3.webp",
            },
            {
                "id":3,
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/5.webp",
            },
            {
                "id":4,
                "title": "标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/6.webp",
            },
            {
                "id":5,
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/7.webp",
            },
            {
                "id":6,
                "title": "标题4",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/4.webp",
            }]}

if __name__ == '__main__':
    app.run()