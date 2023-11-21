
#csv #comma separated value
#Списък със данни за студенти
# факултетен номер, име, фамилия, специалност, среден успех

studenti = [1111111111, "Иван", "Иванов", "КИТ", 4.50,
			2222222222, "Петър", "Стоянов", "КИТ", 5.60,
			3333333333, "Янка", "Маринова", "КИ", 5.20,
			4444444444, "Митко", "Димов", "КИТ", 3.50,
			5555555555, "Милка", "Димитрова", "КИ", 4.90] #Ако няма кавички не може да ги извеждаме

# Да се изведат имената на студентите

def studentsNames():
	for name in range(1,len(studenti),5):
		print(studenti[name])

#studentsNames()


# Да се изведат името и фамилията на студентите

def StudentsFullNames():
	for name in range(1,len(studenti),5):
		print(studenti[name]," ", studenti[name+1])

#StudentsFullNames()

#Да се изведе средният успех на студентите

def SredenUspeh():
	ocenka = 0
	br = 0
	for item in range(4,len(studenti),5):
		ocenka += studenti[item]
		br += 1
	return ocenka / br

#print(SredenUspeh())

# Да се изведе средния успех на студентите от една специалност

def SredenUspehSpec(specialnost):
	ocenka = 0
	br = 0
	for item in range(4,len(studenti),5):
		if specialnost == studenti[item-1]: #Ако сложа in проверява за целия списък вместо за стойност
			ocenka += studenti[item]
			br += 1
	return ocenka / br
#print(SredenUspehSpec("КИТ"))

#Да се създаде списък с различните специалности на студентите

def SpecList():
	Specs = []
	for item in range(3,len(studenti),5):
		if studenti[item] not in Specs: #Добър начин за проверка на копия в списък
			Specs.append(studenti[item])
	return Specs
#print(SpecList())

#Да се изведе средният успех на студентите от всяка специалност

def SredUspehPerSpecs():
	listSpec = SpecList()
	for Specs in listSpec:
		print("Средният успех на специалност ", Specs, " е: ", "{:.2f}".format(SredenUspehSpec(Specs))) #Начин на форматиране
SredUspehPerSpecs()