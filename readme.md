用全排列列词根。不现实。很多组合根本不会出现。全排列总数当然远远超过现存单词数。
python的lambda https://blog.csdn.net/imzoer/article/details/8667176 【lambda作为申明（你要调用它了），冒号前代表要传的参数，冒号后代表结果计算式】
python的reduce runoob.com/python/python-func-reduce.html 【将上一次的结果作为本次的第一个参数】
chr() 将acsii转化为字母
ord() 将字母转化为acsii
list.sort(key = lambda i:len(i),reverse=True)|【按元素的长度进行排序，结果反向输出。key和reverse是sort的参数】
用f.readlines()读取后用f.writelines()时不用加'\n'
f.writelines('{}\n'.format(foo) for foo in foos)