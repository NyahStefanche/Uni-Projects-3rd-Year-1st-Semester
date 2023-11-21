#Dictionaries - речници

mydict = {
	"ime":"Ivan",
	"spec":"KIT",
	"kurs":3
}

print(mydict)
print(mydict["ime"]) #Извеждане само на стойност от даден ключ
mydict["ime"] = "Petyr" #Директна смяна
print(mydict)

print(len(mydict))


name = mydict["ime"]

key = mydict.keys()

print(type(key))

#print(mydict[0]) #Този начин не може, няма достъп до ключовете

#for k in key: #Обхожда целия речник
#	print(mydict[k]) #Извежда всички стойности

mydict["nomer"] = 101232110 #Добавяне на ключ и стойност
print(mydict)

mydict.pop("spec") #Изтриване на ключ и стойност
print(mydict)

mydict.popitem() #Изтрива последния ключ и стойност, под 3.6(включително) версия на python се маха на случаен принцип вместо последния
print(mydict)

#del mydict #Изтриване на целия речник
#mydict.clear() #Изчиства целия речник

for item in mydict.values(): #Другия вариант да работим само със стойностите
	print(item)

for x,y in mydict.items(): #Извежда ключа и стойността
	print(x,y)

#Копирането работи както при останалите с .copy
#mydict2 = mydict.copy() <-- Пример

students = {
	student01: {
		"name":"Ivan",
		"spec":"KIT",
		"nomer":01232156
	},
	student02: {
		"name":"Petyr",
		"spec":"KIT",
		"nomer":01232175	
	},
	student03: {
		"name":"Maria",
		"spec":"KIT",
		"nomer":01232145	
	}
}
