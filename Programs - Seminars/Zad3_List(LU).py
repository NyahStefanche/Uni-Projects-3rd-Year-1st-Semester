"""
3. Даден е следния списък
mylist = [2,33,46,12,56,38,23,49,28,74]
Да се намери и изведе индекса на първата стойност
в списъка,която е по-голяма от 30
"""

mylist = [2,33,46,12,56,38,23,49,28,74]

#Първи начин - Оправен
b = False
for item in range(0,len(mylist)):
	if b==False and mylist[item]>30:
		print(item)
		b = True

# Първи начин - на лектора
"""
b = False
ind = -1
for item in range(0,len(mylist)):
	if not b and mylist[item]>30:
		ind = item
		b = True

print(ind)
"""

"""
Втори начин - на лектора
index=[]
for item in range(0,len(mylist)):
	if mylist[item]>30:
		index.append(item)

print(index[0])

"""

"""
Трети начин - на лектора
for item in range(0,len(mylist)):
	if mylist[item]>30:
		print(item)
		break # Спира for цикъла (Спира вътрешния ако има вложени for цикли)
			  #continue - Пропусни тази стъпка

"""