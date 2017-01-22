spiral={}
spiral[(0,0)]=1
turn=1
n=2
while n<1001**2:	
	for k in range(2*turn): #going down the turn
		spiral[(turn,turn-1-k)]=n
		n+=1
	for k in range(1,2*turn+1): #going left the turn
		spiral[(turn-k,-turn)]=n
		n+=1
	for k in range(1,2*turn+1): #going up the turn
		spiral[(-turn,-turn+k)]=n
		n+=1
	for k in range(1,2*turn+1): #going right the turn
		spiral[(-turn+k,turn)]=n
		n+=1
	turn+=1

print sum([spiral[(x,y)] for (x,y) in spiral.keys() if x==y or x==-y])

c=3
for y in range(c-1,-c,-1):
	print [spiral[(x,y)] for x in range(-c+1,c)]
