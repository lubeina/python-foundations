from datetime import date
Employee_data=[]
Manager_data=[]
class Employee:
	def __init__ (self,name = "",age = 0,salary = 0,employment_year = 0):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year
		
	def get_working_years(self):
		today = date.today()
		return(today.year - self.employment_year)

	def __str__(self):
		return "Name: %s , Age: %s , Salary: %s , Working Years: %s" % (self.name, self.age,self.salary,self.get_working_years())

class Manager(Employee):
	def __init__ (self,name = "",age = 0,salary = 0,employment_year = 0,bonus_percentage = 0.0):
		Employee.__init__(self, name, age,salary,employment_year)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return(self.bonus_percentage * self.salary)

	def __str__(self):
		return "Name: %s , Age: %s , Salary: %s , Working Years: %s , Bonus: %s " % (self.name, self.age,self.salary,self.get_working_years(),self.get_bonus())



print("Welcome to HR Pro 2019\nOptions:\n"
    "1. Show Employees\n"
    "2. Show Managers\n"
    "3. Add An Employee\n"
    "4. Add A Manager\n"
    "5. Exit\n")
option = int(input("What would you like to do? "))
print("-----------------")

while option !=5:
	if option == 1:
		print("Employees\n")
		for i in range(len(Employee_data)):
			print (Employee_data[i])
		print ("\n-----------------\n")

	if option == 2:
		print("Managers\n")
		for i in range(len(Manager_data)):
			print (Manager_data[i])
		print ("\n-----------------\n")

	if option == 3:
		name=input("Name: ")
		age=int(input("Age: "))
		salary = float(input("Salary: "))
		employment_year = int(input("Employment year: "))
		empobj = Employee(name,age,salary,employment_year)
		Employee_data.append(empobj)
		print("Employee added succesfully!\n")

	if option == 4:
		name=input("Name: ")
		age=int(input("Age: "))
		salary = float(input("Salary: "))
		employment_year = int(input("Employment year: "))
		bonus_percentage = float(input("Bonus: "))
		manobj = Manager(name,age,salary,employment_year,bonus_percentage)
		Manager_data.append(manobj)
		print("Manager added succesfully!\n")

	print("Welcome to HR Pro 2019\nOptions:\n"
    "1. Show Employees\n"
    "2. Show Managers\n"
    "3. Add An Employee\n"
    "4. Add A Manager\n"
    "5. Exit\n")
	option = int(input("What would you like to do? "))
	print("-----------------")









