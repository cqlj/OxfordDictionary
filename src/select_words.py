import re

for i in range(1,214):
	with open('牛津高阶词典第7版_{}.txt'.format(i),'r',encoding='utf8') as f:
		content = f.read()
		words = re.findall(r'\n(.*?)/',content)
		print(words)

	with open('glossory.txt','a+',encoding='utf8') as f:
		for word in words:
			f.write(word)
			f.write('\n')