with open ('count.txt','r',encoding='utf8') as f:
	words = f.read().split('\n')
	
for root in words:
	bef = []
	aft = []
	with open('glossoryJoin.txt','r',encoding='utf8') as f:
		words = f.readlines()
		for word in words:
			if root in word:
				aft.append(word)
			else:
				bef.append(word)

	whole = aft + bef
	print(len(whole))
	print(len(aft))
	with open('glossoryJoin.txt','w',encoding='utf8') as f:
		f.writelines(whole)