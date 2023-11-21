
studenti = [[1111111111, "Иван", "Иванов", "КИТ", 4.50],
			[2222222222, "Петър", "Стоянов", "КИТ", 5.60],
			[3333333333, "Янка", "Маринова", "КИ", 5.20],
			[4444444444, "Митко", "Димов", "КИТ", 3.50],
			[5555555555, "Милка", "Димитрова", "КИ", 4.90]]

#print(studenti[1][1]) #Извеждане, Петър

def studentNames():
	for item in range(0,len(studenti),1): #1 е Стъпка (да не забравям)
		print(studenti[item][1])

#studentNames()

def All():
	for row in range(len(studenti)):
		for item in range(len(studenti[row])):
			print(studenti[row][item])

# All()

def CopyList():
	studenti2 = []
	for row in range(len(studenti)):
		for item in range(len(studenti[row])):
			studenti2.append(studenti[row][item])
	return studenti2
print(CopyList())