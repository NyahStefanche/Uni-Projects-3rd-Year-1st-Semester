# Стрингове

name = "Ivan" #И Двете са стрингове
car = 'Volvo' #^^^^^^^^^^^^^^^^^^^^

text = """ This is a text.This is a text.This is a text.This is a text
This is a text.This is a text.This is a text
This is a text.This is a text.""" #Това вече не е коментар а стринг на много редове

#print(text)

# Стринговете като масив(стринговете се разглеждат като масив)

name = "Ivan Petrov"

#print(name[1]) #По същия начин започва от 0, тоест тука връща v

#for letter in name: #for цикъл в python
#	print(letter)

# Проверка за наличие на подстринг в стринг

print("Ivan" in name) #Връща True защото е логическа проверка

if "Ivan" in name: #Начин за проверка дали съществува нещо(not in/in)
	print("Exist")
else:
	print("Does not exist")

# Определяне на отрязъци на части от стринг slicing
# [x:y] x - Началната позиция, а y - крайната позиция, която не участва в този slice

# с подаване на начална и крайна позиция
#print(name[0:4]) #Извежда Ivan
print(name[5:8]) #Извежда pet

# Без подаване на начална стойност (започва от началото до заданения край)

print(name[:4]) #Извежда Ivan

# Без подаване на крайна стойност (Започва от зададената стойност до края)

print(name[5:]) #Извежда Petrov

# Без подаване на начална и крайна позиция (Извежда цялото)

print(name[:]) #Извежда Ivan Petrov

# С подаване на отрицателни стойности (Започва отзад напред - наобратно)

print(name[-6:-2]) #Извежда Petr

#for 
#name[i:i+2]

# Извеждане с главни букви - .upper()

print(name.upper())

# Извеждане с малки букви - .lower()

print(name.lower())

# Премахване на символите за интервал в края и началото на стринга .strip()

name = "      Ivan Petrov       "
print(name.strip())

# Заместване на един стринг с друг стринг .replace,ако няма правилно заместване го игнорира

print(name.replace("Ivan","Emo"))

# Разделяне на стринг - Превръща ги в лист(масив но не е еднотипен)

name = "Ivan,Petrov,Mitkov,3.5,23"
#print(name.split(",")[3:]) #Извежда всичко след 3.5
#print(name.split(",")[2]) #Извежда Mitkov
print(name.split(",")) #Превръща ги в лист и ги отделя

# Конкатенация(Слепване) на стрингове

name = "Ivan "
lastName = "Petrov"

fullName = name + lastName + str(50) #Слепване, трябва да са от тип стринг,ако се зададе с str(50) става
print(fullName)

# Escape символи

#name = "Ivan "Vankata" Petrov"  #Грешен синтаксис
#name = "Ivan \"Vankata\" Petrov" #Правилен запис
#name = "Ivan \\Vankata\\ Petrov" #Извежда Ivan \Vankata\ Petrov
name = "Ivan \\Vankata\\ \tPetrov" # \t - табулация \n - нов ред

print(name)
