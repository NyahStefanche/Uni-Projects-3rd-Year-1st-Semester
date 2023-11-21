# Промяна на стойност на елемент в tuple

mytuple= (23,56,43,88,51,343,21)

l = list(mytuple)

l[1] = 547

mytuple = tuple(l)

print(mytuple)


# Добавяне на елемент към tuple

# Първи начин - с превръщане на tuple в list
l1 = list(mytuple)

l1.append(300) # Или с .insert(позиция,число)

mytuple = tuple(l1)

print(mytuple)

# Втори начин - с добавяне на tuple към друг

tup2 = (30,)
mytuple += tup2
print(mytuple)
# print(mytuple+tup2) # Също става

# Премахване на елемент от tuple

l3 = list(mytuple)

l3.remove(30)

mytuple = tuple(l3)

print(mytuple)