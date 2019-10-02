with open('suf.txt','r',encoding='utf8') as f:
	roots = f.read().split('\n')

with open('suffed.txt','a+',encoding='utf8') as f:
	rooted = f.read().split('\n')

for root in roots:
	if root not in rooted:
		after = []
		before = []
		with open('glossoryJoin.txt','r',encoding='utf8') as f:
			words = f.readlines()
			for word in words:
				if root in word:
					before.append(word)
				else:
					after.append(word)
		lenth = len(before)
		if lenth<41 and lenth>3:
			before.sort()
			before.append('-\n')
			# print(root)
			with open('suffed.txt','a+',encoding='utf8') as f:
				f.write('{}\n'.format(root))
			whole = before + after
			with open('glossoryJoin.txt','w',encoding='utf8') as f:
				f.writelines(whole)
