with open('index.txt','r',encoding='utf8') as f:
	words = f.readlines()
	print(len(words))
	for i in range(0,len(words)-1):
		if len(words[i])>4 and len(words[i+1])>4:
			if words[i][0:4] == words[i+1][0:4]:
				words[i] = words[i] + '、'
				

with open('index.txt','w',encoding='utf8') as f:
	f.writelines(words)