import json
import os

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

# 测试函数
print(find_comments('/articlePage/1'))