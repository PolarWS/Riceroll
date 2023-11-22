from flask import Flask, jsonify
from flask_cors import CORS
import random
import os
import time

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
            "title": {
                "content": "这是一个md",
                "img": "http://127.0.0.1:5173/src/components/img/7.jpg"
            },
            "md": content,
            "date": "2021-01-01",
            "wordCount": "1000",
        }
    time.sleep(1)
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
                "img": "src/components/img/3.jpg",
            },
            {
                "id":2,
                "title": "标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/4.png",
            },
            {
                "id":3,
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/1.jpg",
            },
            {
                "id":4,
                "title": "标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/4.png",
            },
            {
                "id":5,
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/1.jpg",
            },
            {
                "id":6,
                "title": "标题4",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/components/img/2.png",
            }]}

if __name__ == '__main__':
    app.run()