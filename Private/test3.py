"""
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
    x = x + 1 """

#övning 3
i = 10 
while i > 0:
    print(i)
    i-=1
else:
    print("Starta!")


