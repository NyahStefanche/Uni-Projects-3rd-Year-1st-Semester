"""
6. Да се създаде списък с нечетните числа в интервала
от 0 до 100
"""

nechetni = []
"""
for item in range(101):
	if item%2!=0:
		nechetni.append(item)
print(nechetni)
"""

nechetni=[item for item in range(101) if item%2!=0]
print(nechetni)
