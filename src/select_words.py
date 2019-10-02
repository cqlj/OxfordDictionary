import re

words = []

for i in range(1,214):
	with open('牛津高阶词典第7版_{}.txt'.format(i),'r',encoding='utf8') as f:
		contents = f.readlines()
		print(len(contents))
		for content in contents:
			if content.startswith('★') or content.startswith('☆'):
				words.append(content)
words.sort()
with open('index.txt','a+',encoding='utf8') as f:
	f.writelines(words)
