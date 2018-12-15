import os
import pickle
import sqlite3
import sys

chat_db_file = sys.argv[1]
friend_id = sys.argv[2]
conn = sqlite3.connect(chat_db_file)
cursor = conn.cursor()
cursor.execute('select CreateTime, Message, Status, Type from ' + friend_id)
content = cursor.fetchall()
all_text = []
your_sents = []
other_sents = []

prev_pr_to_sp = {}
prev = None
for line in content:
    createTime = line[0]
    message = line[1]  # 'message content'
    status = line[2]  # 'status=2  or 3 means message from yourself from phone or computer, status=4 or 5  means message from other'
    type_ = line[3]  # 'type = 1 means text message, type = 47 mean emoji (not sure ), type=10000 means  link(not sure)''
    # print(message)
    # print(status)


    if type_ !=1:
        continue
    if status == 2 or status == 3:
        your_sents.append(message)
        all_text.append(message)
        if prev == 'None':
            continue
        if prev == 'pr':
            prev_pr_to_sp[other_sents[-1]] = message
        prev = 'sp'
    elif status == 4 or status == 5:
        other_sents.append(message)
        all_text.append(message)
        prev = 'pr'
    else:
        print(line)
        all_text[-1] += message
        if prev == 'sp':
            your_sents[-1] += message
        elif prev == 'pr':
            other_sents[-1] += message

if not os.path.isdir('res/wechat'):
    if not os.path.isdir('res'):
        os.mkdir('res')
    os.mkdir('res/wechat')


f = open('res/wechat/dilogues.p', 'wb')
pickle.dump(prev_pr_to_sp, f)
f.close()

f = open('res/wechat/all_text.p', 'wb')
pickle.dump(all_text, f)
f.close()

f = open('res/wechat/your_sents.p', 'wb')
pickle.dump(your_sents, f)
f.close()

f = open('res/wechat/other_sents.p', 'wb')
pickle.dump(other_sents, f)
f.close()
