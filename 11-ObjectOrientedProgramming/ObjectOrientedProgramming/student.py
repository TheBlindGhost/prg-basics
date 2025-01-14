class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.garde = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.garde = 3
    student2.name = "Olivia"
    student2.age = 21
    student2.garde = 1
    student3.name = "Marta"
    student3.age = 20
    student3.garde = 2
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old and is in {student1.garde} grade')
    print(f'{student2.name}, {student2.age} years old and is in {student2.garde} grade')
    print(f'{student3.name}, {student3.age} years old and is in {student3.garde} grade')

if __name__ == "__main__":
    main()