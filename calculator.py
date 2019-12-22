firstnum = input("Enter the first number: ")
if firstnum.isalpha() is True:
  print('The first number is invalid')
secondnum= input("Enter the second number: ")
if secondnum.isalpha() is True:
  print('The second number is invalid')
operation = input("Choose the operation (+,-,/,*):")
if operation == '+':
  result = int(firstnum)+int(secondnum)
elif operation == '-':
  result = int(firstnum)-int(secondnum)
elif operation == '*':
  result = int(firstnum)*int(secondnum)
elif operation == '/':
  result = int(firstnum)/int(secondnum)
else:
  print('Operator is not Valid')

print ('The answer is ',result)