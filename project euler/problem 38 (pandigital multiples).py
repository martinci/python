def is_pandigital(s):
	if s.count('0')>0:
		return False
	for i in range(1,10):
		if s.count(str(i))!=1:
			return False
	return True
def mult(n,lst):
	s=''
	for l in lst:
		s+=str(n*l)
	if is_pandigital(s):
		return int(s)
	return 0

lst=[[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
m=[918273645]
for n in range(10**3):
	s='9'+str(n)
	for l in lst[:5-len(s)]:
		m.append(mult(int(s),l))
print(max(m))
	
