Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='i love you do you love me?'
>>> b=a.split()
>>> c={}
>>> for d in b:
	count=0
	for e in c:
		if e==d:
			count+=1
	if count>0:
		continue
	else:
		c[d]=b.count(d)

		
>>> c
{'i': 1, 'love': 2, 'you': 2, 'do': 1, 'me?': 1}
>>> 
