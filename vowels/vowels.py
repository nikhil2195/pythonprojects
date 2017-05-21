def vowels(string):
	a,e,i,o,u=0,0,0,0,0
	string=string.lower()
	for letter in string:
		if letter=='a':
			a=a+1
		elif letter=='e':
			e=e+1
		elif letter=='o':
			o=o+1
		elif letter=='i':
			i=i+1
		elif letter=='u':
			u=u+1
	print("Number of vowels is",(a+e+i+o+u))
	print("A",a)
	print("E",e)
	print("I",i)
	print("O",o)
	print("U",u)




abc="The cat jumped from the roof in a rush"
vowels(abc)