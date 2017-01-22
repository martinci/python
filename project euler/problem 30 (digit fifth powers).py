powers=[n**5 for n in range(10)]
print sum([n for n in range(2, 10**6) if n==sum([powers[int(c)] for c in str(n)])])
