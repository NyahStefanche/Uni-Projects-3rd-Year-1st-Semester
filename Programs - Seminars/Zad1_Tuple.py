"""
Даден е следния tuple pixel = (125,231,48,34,25,34,12)
Да се напише програма, която намира и извежда индекса на
максималния елемент
"""

pixel = (125,231,48,34,25,34,12)
max1 = pixel[0]
ind = -1
for item in range(1,len(pixel)):
	if pixel[item] > max1:
		max1 = pixel[item]
		ind = item
print(ind)