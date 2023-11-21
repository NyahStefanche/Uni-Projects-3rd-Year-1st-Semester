# Разпакетиране на tuple

pixel = (125,231,48)

red,green,blue = pixel

print(red,green,blue) # Връща ги като 3 различни, тоест разбива ги и ги слага на всяка променлива
# т.е red = 125 , green = 231 , blue = 48

pixel = (125,231,48,34,25,34,12)

red,green,*blue=pixel # Ако има * връща остатъка, т.е blue връща [48,34,25,34,12], цялостнно връща 125 231 [48,34,25,34,12]
# red,*green,blue=pixel # Връща 125 [231,48,34,25,34] 12, тези с * ги връща като списък

print(red,green,blue)

# Обхождане на tuple

for item in pixel:
	print(item,end=' ') # end=' ' завършване с каквото искате

item = 0
while item < len(pixel):
	print(pixel[item],end=' ')
	item+=1

# Мултиплициране на tuple

multy = pixel * 3 # Получава се копия според избрана бройка след *

print(multy)

