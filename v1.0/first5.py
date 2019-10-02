with open('glossory.txt','r',encoding='utf8') as f:
	words = f.readlines()
	print(len(words))
	for i in range(0,32770):
		if len(words[i])>4 and len(words[i+1])>4:
			if words[i][0:4] == words[i+1][0:4]:
				words[i+1] = words[i] + '、' + words[i+1]
				words[i] = ''

with open('glossoryJoin.txt','a+',encoding='utf8') as f:
	for word in words:
		if word:
			f.write(word)
