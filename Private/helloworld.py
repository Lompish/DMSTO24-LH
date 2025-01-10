"""
print("Hello, World!")

name = "Linda"
age = 31 
print (f"Jag heter {name} och jag är {age} år gammal!")

x = 10
y = 20
summa = x + y
print (f"Den totala summan av x och y är {summa} och jag definerar den som z = {summa}")


heltal = 10
flyttal = 3.5
text = "Jag är bäst!"
sanningsvärde = 'true'
print(type (heltal))
print(type (flyttal))
print(type (text))
print(type (sanningsvärde))

x = 15
y = str(x)
print (y)
print (type (y))

y = 42.4
x = float(y)
print (x)
print (type (x))

y = 42.5
x = int(y)
print (x)
print (type (x))


x = "123"
y = 2 
print (int (x) * (y))

x = "123"
y = 2 
z = int (x)
summa = z * y 
print (f"Svaret är detta {summa}")

x = "123"
y = 2 
z = int (x)
print (f"Svaret {z * y}")


x = 10 
y = 3 
print (x + y)
print (x - y)
print (x / y)
print (x * y)
print (x // y)
print (x % y)
print (x ** y)

z = 3.14
y = int(z)
print (y)

z = 3.14
print (int(z))

z = 5 
y = float (z)
print (y)

z=5
print (float(z))



tal1 = 0.1
tal2 = 0.2
tal1 = int(tal1 * 10)
tal2 = int(tal2 * 10) 
print (tal1 + tal2)

korrektSvar = (tal1 + tal2) / 10


resultat = round (0.1 + 0.2, 1)	# avrundar till 1 decimal
print(resultat) # output: 0.3 

x = input("Skriv första talet: ")
y = input("Skriv andra talet: ")
summa = int(x) + int(y)
print(f"Summan är: {summa}")   

text = " Python är roligt! "
print(text.upper()) 
print(text.strip())
print(text.replace("roligt", "fantastiskt"))  

namn = "Linda"
age = 31
print(f"Hej! {namn} du är {age} år gammal.") 

x = 18
if x > 5:
 print("x är större än 5") 


# Skapa en dictionary:

produkt = {
    "namn": "Laptop", 
    "pris": "10000", 
    "lager": 50 
}
print(produkt["pris"])

produkt ["kategori"] = "Elektronik"
print(produkt["kategori"])

produkt ["lager"] = 40
print(produkt)

# 1. Skriv ut produktens pris.
# 2. Lägg till en nyckel för "kategori".
# 3. Ändra värdet på "lager" till 40.   

person = {
    "namn": "Linda",
    "ålder": 31, 
    "stad": "Stockholm"
}
print(person)


for attribut, varde in person.items():
    print(f"personens {attribut} är {varde}")   

#spel med loop på olika sätt!
while True: 
    x = int(input("Skriv ett tal:"))
    if x > 0:
        print("Talet är positivt")
    elif x < 0:
        print("Talet är negativt")
    else: 
        print("Talet är noll")
    fortsatt = input("Vill du fortsätta? (j/n):")
    if fortsatt == "n":
        print("Avslutas!")
        break   

#spel med loop på olika sätt!
x = input("Skriv ett tal: ")
while x != "exit" and x !="x": 
    x = int(x)
    if x > 0:
        print("Talet är positivt")
    elif x < 0:
        print("Talet är negativt")
    else: 
        print("Talet är noll")
    x= input("Skriv ett tal: ") 

#övning
password = "x"
while password != "hemligt":
    password = input("Ange lösenord: ")
print("Rätt lösenord!") 

#övning 1
x = int(input("Skriv ett tal:"))
if x % 2 == 0:
    print("Talet är jämnt")
elif x % 2 != 0:
    print("Talet är ojämnt")
else: 
    print("Talet är noll") 

#övning 2
for iterator in range(1, 15):
    print(iterator)
x = 1
while x < 10:
    print(x)
    x = x + 1 

#övning 3
i = 10 
while i > 0:
    print(i)
    i-=1
else:
    print("Starta!")    


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

numbers = [30, 49, 56, 89, 93]
print (numbers)

for x in numbers:
    print(x)

arr = [30, 49, 56, 89, 93]
print(sum(arr))     


text = "DataSceience"
print(text[0]) 
print(text[-1]) 
print(text[0:5])    

try: 
    x=int("Hej")

except ValueError:
    print("Ett fel uppstod")
    print("Försök igen!")   


    reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

for index, number in enumerate(reallyLongList):
    print(index, number)



reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in reallyLongList:
    if number % 2 != 0:
        print(number)  
         
      
mixed_list=["1","Linda","0.5"]
print(mixed_list[:])     

my_list=["Karin","Arvid","Axel","Sara","Alma","Anna","Svea"]
print(my_list)

for names in my_list:
      
      if names != "Svea":     
           print("Jag gillar namnet "+names)
      else:
           print("Jag gillar inte namnet "+names)       
"""
x = 2
if x % 2 == 0:
    print(f'{x} är ett jämnt tal.')
else:
    print(f'{x} är ett udda tal.')