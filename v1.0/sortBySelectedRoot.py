for i in range(2,8):
	with open('selectRoot{}.txt'.format(i),'r',encoding='utf8') as f:
		roots = f.read().split('\n')

	for root in roots:
		print(root)
		after = []
		before = []
		with open('glossoryJoin.txt','r',encoding='utf8') as f:
			words = f.readlines()
			for word in words:
				if root in word:
					before.append(word)
				else:
					after.append(word)
		before.sort()
		whole = before + after
		print(len(whole))
		print(len(before))
		with open('glossoryJoin.txt','w',encoding='utf8') as f:
			f.writelines(whole)