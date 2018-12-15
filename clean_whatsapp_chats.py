import pickle
import random
import sys
import os
chat_file = sys.argv[1]

f = open(chat_file,'r', encoding="utf8")
content = f.readlines()
all_text = []
your_sents = []
other_sents = []

YOUR_NAME = 'YOUR NAME HERE'
OTHER_NAME = 'OTHER NAME HERE'

prev_pr_to_sp = {}
prev = None
for line in content[1:]:
	if 'Missed Voice Call' in line:
		continue
	if 'image omitted' in line:
		continue
	if ' %s: '%YOUR_NAME in line:
		text = line.split(' %s: '%YOUR_NAME)[-1]
		your_sents.append(text)
		all_text.append(text)
		if prev == 'None':
			continue
		if prev == 'pr':
			prev_pr_to_sp[other_sents[-1]] = text
		prev = 'sp'
	elif ' %s: '%OTHER_NAME in line:
		text = line.split(' %s: '%OTHER_NAME)[-1]
		other_sents.append(text)
		all_text.append(text)
		prev = 'pr'
	else:
		print(line)        
		all_text[-1] += line

		if prev == 'sp':
			your_sents[-1] += line
		elif prev == 'pr':
			other_sents[-1] += line

if not os.path.isdir('res/whatsapp'):
	if not os.path.isdir('res'):
		os.mkdir('res')
	os.mkdir('res/whatsapp')


f = open('res/whatsapp/dilogues.p', 'wb')
pickle.dump(prev_pr_to_sp, f)
f.close()

f = open('res/whatsapp/all_text.p', 'wb')
pickle.dump(all_text, f)
f.close()

f = open('res/whatsapp/your_sents.p', 'wb')
pickle.dump(your_sents, f)
f.close()

f = open('res/whatsapp/other_sents.p', 'wb')
pickle.dump(other_sents, f)
f.close()
