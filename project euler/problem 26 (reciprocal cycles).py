def rational_to_decimal(n,d): # returns the decimal expression of the rational as a string
	#if n%1!=n or d%1!=d:
		#return 'That is not a rational number!'
	dec_expr='' # it will store n/d = d0.d1 ... dn ( period )
	r=[]
	q=int(n/d)
	dec_expr+=str(q)
	dec_expr+='.'
	r.append(n-d*q)
	n=r[-1]*10
	while True: #This will finish because we know that n/d is always periodic
		q=int(n/d)
		dec_expr+=str(q)
		if r.count(n-d*q)>0:
			i=r.index(n-d*q)
			break
		r.append(n-d*q)
		n=r[-1]*10
	dec_expr=dec_expr[:i+2]+'('+dec_expr[i+2:]
	dec_expr+=')'
	if '(0)' in dec_expr:
		dec_expr=dec_expr[:-3]
	return dec_expr

result=[1,1]
for d in range(2,1000):
	s=rational_to_decimal(1,d)
	if '(' in s:
		index=s.index('(')
		if result[1]<len(s[index:])-2:
			result=[d,len(s[index:])-2]
print(result)
