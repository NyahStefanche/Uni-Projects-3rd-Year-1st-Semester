#Използване на множества

set1 = {1,2,3,4,5,7,9}
set2 = {2,3,6,8}

# Обединяване на множества

set3 = set1.union(set2)
print(set3)

#set1.update(set2)
#print(set1)

set1.intersection_update(set2) # Остава само с повтарящите стойности
print(set1)
