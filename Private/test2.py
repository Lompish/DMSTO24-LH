""" 
my_list=["Äpple","Banan","Kiwi","Citron","Melon","Körsbär","Ananas","Guava","Granatäpple"]
for fruit in my_list:
    if fruit != "Banan":
        print("Jag gillar "+fruit)
    else:
        print("Jag gillar inte "+ fruit)   

my_list = ["stockholm","budapest", "london", "tokyo", "oslo"]
print(my_list)

for city in my_list:
    firstLetter = city[0]
    capitalized = firstLetter.upper()
    city = capitalized

    print(my_list)

my_list.append("helsingfors")
print (my_list)

my_list.pop(1)
print (my_list)

for x in my_list:
    print(x)      
"""
numbers = [30, 49, 56, 89, 93]
print (numbers)

for x in numbers:
    print(x)

arr = [30, 49, 56, 89, 93]
print(sum(arr)) 