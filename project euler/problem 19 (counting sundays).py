def is_leap(year):
	leap=False
	if year%100!=0:
		if year%4==0:
			leap=True
		else:
			leap=False
	else:
		if year%400==0:
			leap=True
	return leap
	
count=0
day=0 #Jan 1st 1900 is a Monday
day_offset={0:3, 1:0, 2:3, 3:2, 4:3, 5:2, 6:3, 7:3, 8:2, 9:3, 10:2, 11:3}
for year in range(1900,2000+1):
	leap=is_leap(year)
	for month in range(12):
		if year!=1900 and day==6:
				count+=1
		if month!=1:
			day+=day_offset[month]
			day=day%7
		else:
			day+=day_offset[month]+leap
			day=day%7
		
print(count)
