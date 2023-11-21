# Списъци 2

# Обхождане на списък

mylist = [23,45,78,51,48,45,28,87,2,44]

#for item in mylist:
#	print(item)
temp = []

for item in mylist:
	if item > 50:
		temp.append(item)
#		print(item)
print(temp)

del temp

# Дължина на списък

print(len(mylist))

# Обхождане на списък 2-ри начин

for item in range(0, len(mylist)): # Може без да задаваме 0-лата също, range(0,Len(mylist),2) е като for(int i=0;i<10;i+2))
#	print(item) # Дава индекса
	print(mylist[item]) # Търсим по индекса в mylist
print("----------------------")
# Обхождане с разпечатване на елементите - трети начин

[print(item) for item in mylist]
