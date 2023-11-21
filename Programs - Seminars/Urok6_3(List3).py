# Списъци 3

# Сортиране на списък във възходящ ред

mylist = [23,45,78,51,45,28,87,2,44]

mylist.sort()
print(mylist)

# Сортиране на списък в низходящ ред

mylist.sort(reverse=True)
print(mylist)

# Проба със стрингове - главните букви са преди малките
mylist = ["hello","python","opel","audi","world"]

mylist.sort()

print(mylist)


mylist = ["hello","python","Opel","Audi","world"]

mylist.sort(key = str.lower) # Прави буквите малки при сортирането(но ги извежда стандартно)

print(mylist)

# Копиране на един списък в друг
"""
temp = mylist

mylist[0] = "ivan"

print(temp) #Промените се отразяват и на други списъци ако са присвоени с =
"""

temp = mylist.copy() # Прави отделно копие което не е псевдоним и промените не се отразяват

# Обединение на два списъка

list1 = mylist + temp
print(list1)