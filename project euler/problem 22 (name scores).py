def name_letter_score(name):
	alphabet='"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	suma=0
	for c in name:
		suma+=alphabet.index(c)
	return suma

with open('p022_names.txt','r') as f:
	names=sorted(f.read().split(','))

scores=[]
for index,name in enumerate(names):
	scores.append((index+1)*name_letter_score(name))
print sum(scores)
	
