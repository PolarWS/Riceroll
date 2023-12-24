from flask import Flask, jsonify, request,escape
from flask_cors import CORS
import random ,os ,html ,time ,urllib.parse ,re ,markdown ,json,uuid,hashlib,urllib

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173'])

def find_comments(root_dir):
    def find_replies(uuid, comments):
        replies = []
        for comment in comments:
            if comment['uuidLink'] == uuid:
                comment.pop('email')
                comment.pop('pageId')
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
                comment.pop('email')
                comment.pop('pageId')
                commentData.append(comment)
                # commentData中的comment添加一项"reply"
                comment['reply'] = find_replies(comment['uuid'], pageId_replies)
        return commentData
    
    # 加载 pageIdIndex 数据
    with open(os.path.join('E:\\code\\vue\\Riceroll\\server', 'comment.json'), 'r') as f:
        data = json.load(f)

    # 在 pageIdIndex 中查找 UUID
    if root_dir not in data['pageIdIndex']:
        return []
    search_uuid = data['pageIdIndex'][root_dir]
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
def frindLinkPage():
    a2 = [random.randint(1, 510) for _ in range(5)]
    return {"status":200,"ping":a2}

@app.route('/comment',methods=['POST'])
def comment():
    if "route" not in request.get_json():
        return{"status":400,"news":"非法操作"}
    return{"status":200,"data":find_comments(request.get_json()["route"])}

@app.route('/commentadd',methods=['POST'])
def commentadd():
    commentData = request.get_json()
    keys = ["name", "email", "uuidLink", "pageId"]
    for key in keys:
        if key not in commentData:
            return {"status": 400, "news": "非法操作"}
        elif len(commentData[key]) > 100:
            return {"status": 400, "news": "信息过长"}

    if commentData["name"] == "" or commentData["msg"] == "":
        return {"status": 400, "news": "请填写完信息"}
    
    if "msg" not in commentData or len(commentData["msg"]) > 2500:
        return {"status": 400, "news": "内容过长"}
    
    if "msg" not in commentData or len(commentData["url"]) > 500:
        return {"status": 400, "news": "网址过长"}
    
    if commentData["url"] != "":
        urlPattern = r'^(https?:\/\/)?(www\.)?[\w-]+(\.[\w-]+)+(\.[a-z]{2,})((\/[\w-]+)*\/?(\?[\w=&-]*)?)?$'
        if re.match(urlPattern, commentData["url"]) is not None:
            return {"status":400,"news":"url不合法"}
        if not commentData["url"].startswith("https://") and not commentData["url"].startswith("http://"):
            commentData["url"] = "https://" + commentData["url"] + "/"
        head, sep, tail = commentData["url"].partition('://')
        tail = urllib.parse.quote(tail)
        commentData["url"] = head + sep + tail
    if commentData["email"] != "":
        # 检测email是否合法
        emailPattern = r'^([A-Za-z0-9_\-\.])+@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$'
        if re.match(emailPattern, commentData["email"]) is None: 
            return {"status":400,"news":"email不合法"}
        default = "https://www.example.com/default.jpg"
        cravatar_url = "https://cravatar.cn/avatar/" + hashlib.md5(commentData["email"].lower().encode()).hexdigest() + "?"
        cravatar_url += urllib.parse.urlencode({'d':default, 's':"100"})
        commentData["avatarImg"] = cravatar_url
    else:
        commentData["avatarImg"] = ""
    
    with open(os.path.join('E:\\code\\vue\\Riceroll\\server', 'comment.json'), 'r') as f:
        commentJson = json.load(f)
    if commentData["pageId"] not in commentJson['pageIdIndex']:
        return {"status":400,"news":"评论区锁定"}
    pageId = commentJson['pageIdIndex'][commentData["pageId"]]

    commentData["pageId"] = pageId
    commentData["msg"] = html.escape(commentData["msg"])
    commentData["uuid"] = str(uuid.uuid4()).replace("-", "")
    commentData["date"] = time.strftime("%Y-%m-%d %H:%M", time.localtime())

    # 先将 commentData 添加到 commentJson['commentData'] 列表中
    commentJson['commentData'].append(commentData)
    # 然后将 commentJson 写回到 comment.json 文件中
    with open(os.path.join('E:\\code\\vue\\Riceroll\\server', 'comment.json'), 'w') as f:
        json.dump(commentJson, f)
    return{"status":200,"news":"评论成功","uuid":commentData["uuid"],"avatarImg":commentData["avatarImg"],"date":commentData["date"]}

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
def articlePage():
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
def filePage():
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