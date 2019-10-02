roots1 = []
roots2 = []
roots3 = []
roots4 = []
roots5 = []
roots6 = []
roots7 = []
roots8 = []
with open('glossoryJoin.txt','r',encoding='utf8') as f:
	words = f.readlines()
	for word in words:
		if len(word)==1:
			roots1.append(word)
		if len(word)==2:
			roots2.append(word)
		if len(word)==3:
			roots3.append(word)
		if len(word)==4:
			roots4.append(word)
		if len(word)==5:
			roots5.append(word)
		if len(word)==6:
			roots6.append(word)
		if len(word)==7:
			roots7.append(word)
		if len(word)==8:
			roots8.append(word)
root = []
root.append(roots1)
root.append(roots2)
root.append(roots3)
root.append(roots4)
root.append(roots5)
root.append(roots6)
root.append(roots7)
root.append(roots8)

for i in range(1,9):
	try:
		with open('selectRoot{}.txt'.format(i),'a+',encoding='utf8') as f:
			f.writelines(root[i])
	except:
		pass
