class Person: 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def setDetails(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def getDetails(self): 
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
    
class Student(Person): 
    def __init__(self, name, age, gender, studentID, course):
        super().__init__(name, age, gender)
        self.studentID = studentID
        self.course = course
        self.grades = []

    def setStudentDetails(self, studentID, course):
        self.studentID = studentID
        self.course = course
    
    def addGrade(self, grade): 
        self.grades.append(int(grade))
    
    def calculateAvgGrade(self): 
        if len(self.grades) != 0:
            self.gradeAvg = sum(self.grades) / len(self.grades)
        else: 
            self.gradeAvg = 0

    def getMentor(self, professor): 
        if professor == None:
            print("No mentor assigned") 
        else:
            print(professor.name)

    def getStudentSummary(self): 
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print(f"Student ID: {self.studentID}, Course: {self.course}, Grade Average: {self.gradeAvg}")

class Professor(Person):
    def __init__(self, name, age, gender, staffID, department, salary):
        super().__init__(name, age, gender)
        self.staffID = staffID
        self.department = department
        self.salary = salary
        self.mentoredStudents = []
    
    def setProfessorDetails(self, staffID, department, salary):
        self.staffID = staffID
        self.department = department
        self.salary = salary
        self.mentoredStudents = []
    
    def giveFeedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")

    def increaseSalary(self, percentage): 
        self.salary *= (1 + int(percentage)/100)
        self.salary = round(self.salary)

    def mentorStudent(self, student): 
        print(f"Professor {self.name} is now mentoring Student {student.name} on {student.course}")
        self.mentoredStudents.append(student.name)

    def getMentoredStudents(self): 
        print(self.mentoredStudents)    

    def getProfessorSummary(self): 
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print(f"Professor ID: {self.staffID}, Department: {self.department}, Salary: {self.salary}")

class Admin(Person): 
    def __init__(self, name, age, gender, adminID, office, yearsOfService): 
        super().__init__(name, age, gender)
        self.adminID = adminID
        self.office = office
        self.yearsOfService = yearsOfService

    def setAdminDetails(self, adminID, office, yearsOfService): 
        self.adminID = adminID
        self.office = office
        self.yearsOfService = yearsOfService
    
    def incrementServiceYears(self): 
        self.yearsOfService += 1

    def getAdminSummary(self): 
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print(f"Admin ID: {self.adminID}, Office: {self.office}, Years of Service: {self.yearsOfService}")

daniel = Student("Daniel", 17, "Male", "S238", "Maths")
daniel.setDetails("Daniel", 17, "Male")
daniel.setStudentDetails("S238", "Maths")

professor = Professor("Mr John", 43, "Male", "H896", "Maths", 100000)
professor.setDetails("Mr John", 43, "Male")
professor.setProfessorDetails("H896", "Maths", 100000)

admin = Admin("Bob", 57, "Male", "L780", "Room 17", 5)
admin.setDetails("Bob", 57, "Male")
admin.setAdminDetails("L780", "Room 17", 5)

daniel.addGrade(9)
daniel.addGrade(9)
daniel.addGrade(9)
daniel.addGrade(8)
daniel.addGrade(8)
daniel.calculateAvgGrade()

professor.giveFeedback(daniel, "You have done very well , congratulations")
professor.increaseSalary(20)

admin.incrementServiceYears()

daniel.getStudentSummary()
professor.getProfessorSummary()
admin.getAdminSummary()

professor.mentorStudent(daniel)
professor.mentorStudent(daniel)
professor.mentorStudent(daniel)
professor.mentorStudent(daniel)
professor.mentorStudent(daniel)
professor.getMentoredStudents()