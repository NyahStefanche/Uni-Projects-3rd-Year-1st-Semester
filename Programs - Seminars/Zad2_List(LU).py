"""
2. Даден е следният списък
mylist = [2,33,46,12,56,38,23,49,28,74]
Да се създадат два допълнителни списъка със четните и нечените стойности от даденият масив.
"""

mylist = [2,33,46,12,56,38,23,49,28,74]
chetni = []
nechetni = []
for item in mylist:
	if item%2==0:
		chetni.append(item)
print(chetni)

for item in mylist:
	if item%2!=0:
		nechetni.append(item)
print(nechetni)
"""
# Кратък вариант
chetni1 = [item for item in mylist if item%2==0]
print(chetni1)
nechetni1 = [item for item in mylist if item%2!=0]
print(nechetni1)
"""
