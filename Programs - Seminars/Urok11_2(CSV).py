
#csv #comma separated value
#Списък със данни за студенти
# факултетен номер, име, фамилия, специалност, среден успех

import csv

try:
	f_csv =  open("students.csv")
	reader = csv.reader(f_csv, skipinitialspace = True)
	stud = list(reader)
	f_csv.close()
except FileNotFoundError:
	print("CSV file not exist")
	quit()

def CopyList():
	studenti2 = []
	for row in range(len(stud)):
		for item in range(len(stud[row])):
			studenti2.append(stud[row][item])
	return studenti2

numberOfItems = len(stud[0])
studenti = CopyList()

# Да се изведат имената на студентите

def studentsNames():
	for name in range(1,len(studenti),numberOfItems):
		print(studenti[name])

#studentsNames()


# Да се изведат името и фамилията на студентите

def StudentsFullNames():
	for name in range(1,len(studenti),numberOfItems):
		print(studenti[name]," ", studenti[name+1])

#StudentsFullNames()

#Да се изведе средният успех на студентите

def SredenUspeh():
	ocenka = 0
	br = 0
	for item in range(4,len(studenti),numberOfItems):
		ocenka += studenti[item]
		br += 1
	return ocenka / br

#print(SredenUspeh())

# Да се изведе средния успех на студентите от една специалност

def SredenUspehSpec(specialnost):
	ocenka = 0
	br = 0
	for item in range(4,len(studenti),numberOfItems):
		if specialnost == studenti[item-1]: #Ако сложа in проверява за целия списък вместо за стойност
			ocenka += float(studenti[item])
			br += 1
	return ocenka / br
#print(SredenUspehSpec("КИТ"))

#Да се създаде списък с различните специалности на студентите

def SpecList():
	Specs = []
	for item in range(3,len(studenti),numberOfItems):
		if studenti[item] not in Specs: #Добър начин за проверка на копия в списък
			Specs.append(studenti[item])
	return Specs
#print(SpecList())

#Да се изведе средният успех на студентите от всяка специалност

def SredUspehPerSpecs():
	listSpec = SpecList()
	for Specs in listSpec:
		print("Средният успех на специалност ", Specs, " е: ", "{:.2f}".format(SredenUspehSpec(Specs))) #Начин на форматиране
#SredUspehPerSpecs()

def namecity():
	for name in range(1,len(studenti),numberOfItems):
		print(studenti[name]," ", studenti[name+1], " ", studenti[name+4])
namecity()