from datetime import date

def checkbirthdate(year,month,day):
	if date.today() < date(int(year),int(month),int(day)):
		return False
	else:
		return True

def calculate_age(year,month,day):
	today = date.today()
	age = today.year - int(year) - ((today.month,today.day) < (int(month), int(day)))
	print (f'You are {age} years old')

year = input('Enter year of birth:')
month = input('Enter month of birth:')
day = input('Enter day of birth:')

if checkbirthdate(year,month,day) == True:
	calculate_age(year,month,day)
else:
	print('The Birthdate is Invalid')

