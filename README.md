# Me_Bot
A simple tool to make a bot that speaks like you, simply learning from your WhatsApp Chats.

Instructions:-

1. From WhatsApp on your phone, go to any chat and export it by going into the settings. Move the txt file that you receive inside the Me_Bot folder.

2. Run the clean_whatsapp_chats.py script using the command. Before running, change the names of the people by changing YOUR_NAME and OTHER_NAME in the scripts according to the txt file you have for your chats.

`python clean_whatsapp_chats.py whatsapp_chat.txt`

3. Run the prepare_files.ipynb ipython notebook.

4. Run the Me_Bot.ipynb file and you can play with the bot at the bottom!

NOTE - Actively seeking collaborators for fun side projects like this. If you're itnerested, please drop me a mail at smadan@mit.edu

## For wechat user:
Wechat chat history is save in SQLite Database, therefore you need to export from you Phone.
Basically, if you have a iPhone, there are the steps to get the database file:
1. Use iTunes to backup your phone (unselect encrypt backup)
2. Use iTools to open the backup file and get a copy of your database file named MM.sqlite
3. run `python clean_wechat_chats.py YOUR_DATABASE_PATH YOUR_FRIEND_ID`

find more detail information about this [here](https://www.cnblogs.com/cxun/p/5677606.html)
