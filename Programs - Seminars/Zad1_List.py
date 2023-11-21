"""
Даден е списък mylist = ["hello","python","opel","audi","world"]
да се състави програма, която създава нов списък,
в който се съдържат елементите, в които има използвана буква 'l'
"""

mylist = ["hello","python","opel","audi","world"]

"""
for item in range(len(mylist)):
	if mylist[item][:] == "l":
		result.append(item)
print(result) 
""" # Пробен вариант (грешен)

"""
result=[]
for item in mylist:
	if "l" in item:
		result.append(item)
print(result) 1-ви начин(стандартно)
"""

temp = [item for item in mylist if "l" in item] # if "l" in item е филтъра
print(temp)

