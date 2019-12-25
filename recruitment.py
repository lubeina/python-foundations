skills = ['Pyton','C++','Javascript','Juggling','Running','Eating']
cv ={}
print('Welcome to the special recruitment program, please answer the following questions:')
cv['name']= input("What's your name? ")
cv['age'] = int(input("What's your age? "))
cv['experience'] = int(input("How many years of experience do you have? "))
cv['skills']=[]

for number,letter in enumerate(skills,1):
	print(number,letter)

num = int(input('Choose a skill from above by entering its number:'))
num2 = int(input('Choose another skill from above by entering its number: '))

cv['skills'].append(skills[num-1])
cv['skills'].append(skills[num2-1])

if (25 < cv['age'] < 40) and (cv['experience'] > 3) and ("Python" in cv['skills']):
	print("You have been accepted,", cv['name'])
else:
	print("Unfortunately", cv['name'], "you do not fit the criteria. We wish you success.")

