"""
Даден е списък mylist = ["hello","python","opel","audi","world"]
да се състави програма, която създава нов списък,
в който се съдържат елементи на mylist, с изключение на "оpel".
"""
mylist = ["hello","python","opel","audi","world"]
temp = [item for item in mylist if "opel" not in item] # Филтъра може да е if item !="opel"

print(temp)