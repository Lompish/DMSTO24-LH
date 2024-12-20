"""
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
print(mixed_list[:])     """

my_list=["Karin","Arvid","Axel","Sara","Alma","Anna","Svea"]
print(my_list)

for names in my_list:
      
      if names != "Svea":     
           print("Jag gillar namnet "+names)
      else:
           print("Jag gillar inte namnet "+names)

