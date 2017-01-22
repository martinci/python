import numpy as np
m=np.zeros(10**3+1)
for a in range(1,10**3):
	for b in range(1,a+1):
		h=(a**2+b**2)**0.5
		if h%1==0 and a+b+h<=10**3:
			p=a+b+int(h)
			m[p]+=1
print(np.argmax(m))
