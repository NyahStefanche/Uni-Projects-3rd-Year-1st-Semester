"""
Sets - множества
Харастеристики:
- НЕ е подредена структура
- НЕ позволява дублиране на стойности
- НЕ позволява промяна на стойностите на елементите
- Позволява елементи с различен тип данни

"""

myset = {1,2,3,4,5,6,"second",7,8,9,10,"first"} # При разпечатването не са подредени винаги така 

print(myset)


# Дължина на множеството

print(len(myset))

# Достъп до елементите

for item in myset:
	print(item)

# Промяна на елемент на множество

# Първи начин
l = list(myset)
print(l)
for item in range(0,len(l)):
	if l[item] == 10:
		l[item] = 100

myset= set(l)

print(myset)


#Втори начин
"""
myset.remove("second")
myset.add("last")
print(myset)
"""