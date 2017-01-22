fibon=[1]*2
while len(str(fibon[-1]))<1000:
	fibon.append(fibon[-1]+fibon[-2])
print len(fibon)
print fibon[-1]
