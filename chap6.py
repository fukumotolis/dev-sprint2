# Enter your answrs for chapter 6 here
# Name: Lisa


# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

middle('jamboree')
# returns 'ambore'

middle('to')
middle('a')
middle('')
# returns ''


""" Write a function that checks if a given word is a palindrome.
	Check first and last letters, then go on to middle.
	If not a match or middle returns '', it's time to stop.
"""

def is_palindrome(word):
		if len(word) > 2:							# need at least 3 letters
			first(word) == last(word)				# then check the letters
			is_palindrome(middle(word))	
			if i == n:								# sub-conditional to tell me if we're done
					print 'This is a palindrome'
			i + 1
		else:										# otherwise no way
			print 'This is not a palindrome.'

# Ex 6.8

def gcd(a,b):
	r = a % b
	gcd(b, r)
	print a, b, r
