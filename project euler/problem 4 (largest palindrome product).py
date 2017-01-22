def is_palindromic(n):
	s=str(n)
	return s==s[::-1]

print(max([m*n for n in range(100,1000) for m in range(100,1000) if is_palindromic(m*n)]))
