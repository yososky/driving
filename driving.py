coutry = input ('What is your coutry:')
age = input ('type your age:')
age = int(age)
if coutry == "USA":
	if age >= 18:
		print ('Yes')
	else:
		print('No')
elif coutry == 'China':
	if age >= 16:
		print('Yes')
	else:
		print('No')