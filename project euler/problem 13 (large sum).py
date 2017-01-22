with open('problem 13.txt', 'r') as f:
	nums=f.read().splitlines()
s=0
for i in range(len(nums)):
	s+=int(nums[i])
print s

