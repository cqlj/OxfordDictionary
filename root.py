root = 'cular'

with open('glossory.txt','r',encoding='utf8') as f:
	roots = []
	words = f.readlines()
	for word in words:
		if root in word:
			roots.append(word)

with open('./roots/{}.txt'.format(root),'a+',encoding='utf8') as f:
	f.writelines(roots)