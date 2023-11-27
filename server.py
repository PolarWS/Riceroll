from flask import Flask, jsonify
from flask_cors import CORS
import random
import os
import time
import urllib.parse
import re
import markdown


app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173'])

@app.route('/')
def hello_world():
    return "hellow world"

@app.route('/frindLinkPage')
def hello_world2():
    a2 = [random.randint(1, 510) for _ in range(5)]
    return {"status":200,"ping":a2}

import re

def parse_toc(content):
    html = markdown.markdown(content)
    html_lines = html.split('\n')
    toc = []
    encode_dict = {
        '"': '%22',
        '#': '%23',
        '%': '%25',
        '$': '%24',
        '&': '%26',
        '+': '%2B',
        ',': '%2C',
        '/': '%2F',
        ':': '%3A',
        ';': '%3B',
        '=': '%3D',
        '?': '%3F',
        '@': '%40',
        '[': '%5B',
        ']': '%5D',
        '\\': '%5C',
    }
    for line in html_lines:
        if line.startswith('<h'):
            title = line[line.find('>')+1:line.rfind('<')]
            # 移除所有的 HTML 标签
            title = re.sub('<.*?>|\^', '', title)
            print(title)

            # 移除首尾的空格，然后将标题中的空格替换为 -
            href_title = title.strip().replace(' ', '-').replace('&amp;', '&')
            # 使用 encode_dict 来编码 URL
            href_title = ''.join([encode_dict.get(c, c) for c in href_title.lower()]) 
            # 使用正则表达式移除表情符号和特殊字符
            title = re.sub(r'(:[^:]*:)', '', title)
            toc.append(f'<p><a href="#{href_title}">{title}</a></p>')
    return ''.join(toc)

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
            "Toc": parse_toc(content)
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
                "img": "src/img/4.webp",
            },
            {
                "id":2,
                "title": "标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/7.webp",
            },
            {
                "id":3,
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/6.webp",
            },
            {
                "id":4,
                "title": "标题标题标题",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/5.webp",
            },
            {
                "id":5,
                "title": "标题标题2标题23",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/3.webp",
            },
            {
                "id":6,
                "title": "标题4",
                "date": "2020-01-01",
                "wordCount":2333,
                "url": "文章链接",
                "content": "文章内容",
                "img": "src/img/2.webp",
            }]}

if __name__ == '__main__':
    app.run()