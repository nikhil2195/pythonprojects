def palindrome(string):
	temp=''.join(reversed(string))
	if temp==string:
		print(string," is palindrome")
	else:
		print(string," is not palindrome")




palindrome('lol')
palindrome('Nikhil')