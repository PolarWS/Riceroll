from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import os
import time
import urllib.parse
import re
import markdown
import json


app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173'])

def find_comments(root_dir):
    # 加载 pageIdIndex 数据
    with open(os.path.join('E:\\code\\vue\\Riceroll\\server', 'comment.json'), 'r') as f:
        data = json.load(f)

    # 在 pageIdIndex 中查找 UUID
    search_uuid = data['pageIdIndex'][root_dir]

    def find_replies(uuid, comments):
        replies = []
        for comment in comments:
            if comment['uuidLink'] == uuid:
                replies.append(comment)
                replies.extend(find_replies(comment['uuid'], comments))
        return replies

    def find_pageId(pageId, comments):
        pageId_replies = []
        commentData = []
        for comment in comments:
            if comment['pageId'] == pageId:
                pageId_replies.append(comment)
        # 遍历pageId_replies所有uuidLink为空的评论
        for comment in pageId_replies:
            if comment['uuidLink'] == '':
                commentData.append(comment)
                # commentData中的comment添加一项"reply"
                comment['reply'] = find_replies(comment['uuid'], pageId_replies)
        return commentData

    # 使用递归函数找到所有回复
    replies = find_pageId(search_uuid, data['commentData'])

    return replies

def parse_toc(content):
    html = markdown.markdown(content)
    html_lines = html.split('\n')
    toc = {"data":[]}
    href_title_counts = {}
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
        '^': '%5E',
    }
    id_counter = 0
    for line in html_lines:
        if line.startswith('<h') and line[2].isdigit():
            level = str(line[2])  # 获取标题的级别
            title = line[line.find('>')+1:line.rfind('<')]
            if title != "":
                title = re.sub('<.*?>', '', title)
                href_title = re.sub(r'\^(.*?)\^', r'\1', title).strip().replace(' ', '-').replace('&amp;', '&').lower()
                href_title = ''.join([encode_dict.get(c, c) for c in href_title])
                title = re.sub(r'\^(.*?)\^', r'^\1', title)
                title = re.sub(r'(:[^:]*:)', '', title)
                if href_title in href_title_counts:
                    href_title_counts[href_title] += 1
                    href_title = f"{href_title}-{href_title_counts[href_title]}"
                else:
                    href_title_counts[href_title] = 0
            toc["data"].append({
                "class": f"markdownTocClass{level}",
                "href": f"#{href_title}",
                "title": title
            })
            id_counter += 1
    return toc

@app.route('/')
def hello_world():
    return "hellow world"

@app.route('/frindLinkPage')
def hello_world2():
    a2 = [random.randint(1, 510) for _ in range(5)]
    return {"status":200,"ping":a2}

@app.route('/comment',methods=['POST'])
def hello_world6():
    return{"status":200,"data":find_comments(request.get_json()["route"])}

@app.route('/md', methods=['POST'])
def hello_world4():
    with open('test.md', 'r', encoding='utf-8') as file:
        content = file.read()
    md = {
            "status":200,
            "title": {
                "content": "这是一个md",
                "img": "http://127.0.0.1:5173/src/img/4.webp"
            },
            "md": content,
            "date": "2021-01-01",
            "wordCount": "1000",
            "Toc": parse_toc(content),
            "tag": ["tag1", "tag2", "tag3"]
        }
    return jsonify(md)



@app.route('/articlePage')
def hello_world3():
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

@app.route('/filePage')
def hello_world5():
    time.sleep(1)
    return {"status":200,"data":[
                {
                    "label": "2023",
                    "content": [{"title":"标题标题标题标题标题标题","date":"9/10","id":"1"}, 
                                {"title":"标题标题标题标题","date":"7/10","id":"1"}, 
                                {"title":"标题标题","date":"5/23","id":"1"}]
                },
                {
                    "label": "2022",
                    "content": [{"title":"标题标题标题标题标题","date":"9/10","id":"1"}, 
                                {"title":"标题标题标题标题标题","date":"8/10","id":"1"}, 
                                {"title":"标题标题标题标题标题标题","date":"3/10","id":"1"}]
                },
                {
                    "label": "2021",
                    "content": [{"title":"标题标题标题标题标题标题","date":"7/10","id":"1"}, 
                                {"title":"标题标题标题标题标题标题","date":"4/10","id":"1"}, 
                                {"title":"标题标题标题标题","date":"1/10","id":"1"}]
                },
                {
                    "label": "2020",
                    "content": [{"title":"标题题标题标题","date":"9/10","id":"1"}, 
                                {"title":"标标题标题标题","date":"6/10","id":"1"}, 
                                {"title":"标题标题题标题标题","date":"5/10","id":"1"}, 
                                {"title":"标题标题题标题标题","date":"5/10","id":"1"}, 
                                {"title":"标题标题题标题标题","date":"5/10","id":"1"}, 
                                {"title":"标题标题题标题标题","date":"5/10","id":"1"}, 
                                {"title":"标题标题题标题标题","date":"5/10","id":"1"}, 
                                {"title":"标题标题题标题标题","date":"5/10","id":"1"}]
                },
            ]}
    

if __name__ == '__main__':
    app.run()