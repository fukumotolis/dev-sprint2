
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	n = len(word) // 2								# only check half the letters
	for i in range(0, n):	
		if first(word) == last(word):				# if first = last, check middle
			is_palindrome(middle(word))	
			i + 1
			if i == n:								# sub-conditional to tell me if it is a palindrome
					print 'This is a palindrome'
			
		else:										# otherwise no way
			print 'This is not a palindrome.'

is_palindrome('redivider')
is_palindrome('noon')