def is_palindromic(s):
	return s==s[::-1]
print(sum([n for n in range(10**6) if is_palindromic(str(n)) and is_palindromic('{0:b}'.format(n))]))
