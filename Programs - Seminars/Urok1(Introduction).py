print("Hello World!")
# едноредов Коментар

""" 
Това е многоредов коментар - първи ред
това е втори
това е трети
"""
number = 10 # number е променлива (деклариране на променливи)
number = number + 2
number += 2 #ако искаме да натрупваме стойности в променлива
number = str(number)
# number +=2 грешен вход защото променливата е вече от тип string
number += "2"
number = "Hello" # Променливата се променя(ако не е зададен видът му като str(number)) тъй като няма зададен тип(Както в c++) и както е int може да стане string без да му задаваме
logic = False # Python е case sensitive (Главни/малки букви имат разлика)

print(number) #ако искаме да изведем на екрана дадена променлива

if (logic == True) and : #с : условието завършва тук
	print("True") #Вместо {} се вкарва навътре в реда и така се определя
	if #if в if
		
else:
	pass # Премини го (още не съм готов)