count=0
value=200
for n200 in range(value//200+1):
	for n100 in range((value-n200*200)//100+1):
		for n50 in range((value-n200*200-n100*100)//50 +1):
			for n20 in range((value-n200*200-n100*100-n50*50)//20+1):
				for n10 in range((value-n200*200-n100*100-n50*50-n20*20)//10+1):
					for n5 in range((value-n200*200-n100*100-n50*50-n20*20-n10*10)//5+1):
						for n2 in range((value-n200*200-n100*100-n50*50-n20*20-n10*10-n5*5)//2+1):
							for n1 in range((value-n200*200-n100*100-n50*50-n20*20-n10*10-n5*5-n2*2)//1+1):
								count+=1
								break
print(count)
