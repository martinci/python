def number_name(n): #gives the names of numbers between 1 and 999 included.
	if n>1000:
		return 'Too big!'
	if n==1000:
		return 'one thousand'
	
	s=str(n)
	
	if len(s)==1:
		if s[0]=='0':
			return 'zero'
		if s[0]=='1':
			return 'one'
		if s[0]=='2':
			return 'two'
		if s[0]=='3':
			return 'three'
		if s[0]=='4':
			return 'four'
		if s[0]=='5':
			return 'five'
		if s[0]=='6':
			return 'six'
		if s[0]=='7':
			return 'seven'
		if s[0]=='8':
			return 'eight'
		if s[0]=='9':
			return 'nine'
	
	elif len(s)==2:
		if s[0]=='0':
			return number_name(int(s[0]))
		if s[0]=='1':
			if s[1]=='0':
				return 'ten'
			if s[1]=='1':
				return 'eleven'
			if s[1]=='2':
				return 'twelve'
			if s[1]=='3':
				return 'thirteen'
			if s[1]=='4':
				return 'fourteen'
			if s[1]=='5':
				return 'fifteen'
			if s[1]=='6':
				return 'sixteen'
			if s[1]=='7':
				return 'seventeen'
			if s[1]=='8':
				return 'eighteen'
			if s[1]=='9':
				return 'nineteen'
		if s[0]=='2':
			if s[1]=='0':
				return 'twenty'
			else:
				return 'twenty-{0}'.format(number_name(int(s[1])))
		if s[0]=='3':
			if s[1]=='0':
				return 'thirty'
			else:
				return 'thirty-{0}'.format(number_name(int(s[1])))
		if s[0]=='4':
			if s[1]=='0':
				return 'forty'
			else:
				return 'forty-{0}'.format(number_name(int(s[1])))
		if s[0]=='5':
			if s[1]=='0':
				return 'fifty'
			else:
				return 'fifty-{0}'.format(number_name(int(s[1])))
		if s[0]=='6':
			if s[1]=='0':
				return 'sixty'
			else:
				return 'sixty-{0}'.format(number_name(int(s[1])))
		if s[0]=='7':
			if s[1]=='0':
				return 'seventy'
			else:
				return 'seventy-{0}'.format(number_name(int(s[1])))
		if s[0]=='8':
			if s[1]=='0':
				return 'eighty'
			else:
				return 'eighty-{0}'.format(number_name(int(s[1])))
		if s[0]=='9':
			if s[1]=='0':
				return 'ninety'
			else:
				return 'ninety-{0}'.format(number_name(int(s[1])))

	elif len(s)==3:
		if s[1:]=='00':
			return '{0} hundred'.format(number_name(int(s[0])))
		else:
			return '{0} hundred and {1}'.format(number_name(int(s[0])),number_name(int(s[1:])))

string=''
for i in range(1,1001):
	string+=number_name(i)

print(len([s for s in string if s!=' 'and s!='-']))
