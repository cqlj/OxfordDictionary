with open('suf.txt','r',encoding='utf8') as f:
	roots = f.read().split('\n')


for root in roots:
	after = []
	before = []
	# count = 0
	with open('glossoryReferred.txt','r',encoding='utf8') as f:
		words = f.readlines()
		for word in words:
			if root in word:
				before.append(word)
				# count += 1
			else:
				after.append(word)
	lenth = len(before)
	if lenth<15 and lenth>2:
		before.sort()
		before.append('-\n')
		# print(root)
		whole = before + after
		with open('glossoryReferred.txt','w',encoding='utf8') as f:
			f.writelines(whole)
		# with open('countRootReferred.txt','a+',encoding='utf8') as f:
		# 	f.write('{} {}\n'.format(root,count))