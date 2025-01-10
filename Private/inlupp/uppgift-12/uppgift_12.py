# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list) -> dict:
    """
    Skapar ett register med studenter där namn är nyckel och ålder är värde.
    
    students: En lista med tupplar (namn, ålder) för varje student.
    return: En dictionary med namn som nyckel och ålder som värde.
    """
    student_register = {}
    for student in students:
        name, age = student  # Dela upp varje tuple i namn och ålder
        student_register[name] = age        # För varje student sätts namnet som nyckel och åldern som värde i dictionaryn.
    return student_register     


students = [("Linda", 31), ("Niklas", 30), ("Bosse", 21), ("Axel", 20), ("Arvid", 22)]
register = create_student_register(students)
print(register)  # Output: {'Linda': 31, 'Niklas': 30, 'Bosse': 21, 'Axel': 20, 'Arvid': 22}
