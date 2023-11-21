"""
4. Даден е следния списък
mylist = [2,33,46,12,56,38,23,49,28,74]
Да се намери и изведе индекса на последната стойност
в списъка,която е по-голяма от 30
"""
mylist = [2,33,46,12,56,38,23,49,28,74]

index=[]
for item in range(0,len(mylist)):
	if mylist[item]>30:
		index.append(item)

print(index[-1])
"""
for item in range(-1,len(mylist)):
	if mylist[item]>30:
		print(item)
		break
"""

"""
b = False
for item in range(-1,len(mylist)):
	if b==False and mylist[item]>30:
		print(item)
		b=True
"""

"""
ind = 0
for item in range(0,len(mylist)):
	if mylist[item] > 30:
		ind = item
print(ind)
"""

"""
10
0 --> 9
1 --> 8
2 --> 7
....
9 --> 0
т.е index = дължината на списъка - 1 - индекса от for
#с използване на reverse()
mylist.reverse()
for item in range(0,len(mylist)):
	if mylist[item]>30:
		ind=item
		break
index = len(mylist) - 1 - ind
print(index)
"""