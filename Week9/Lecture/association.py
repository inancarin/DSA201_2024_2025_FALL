class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return "A person whose name is " + self.name \
            + " and age is " + str(self.age)

class Course:
    def __init__(self, code, capacity, credit):
        self.code = code
        self.capacity = capacity
        self.credit = credit
        self.enrolledStudents = 0

    def __str__(self):
        return self.code + ", capacity: " + str(self.capacity) \
              + ", enrolled: " + str(self.enrolledStudents)
    

class Student(Person):
    def __init__(self, name, age, id, school):
        super().__init__(name, age)
        self.id = id
        self.school = school
        self.registeredCourses = [] # a list of courses
    
    def __str__(self):
        return "A student with ID " + str(self.id) + " at " + self.school
    
    def enrollCourse(self, course):
        if course.capacity > course.enrolledStudents:
            self.registeredCourses.append(course)
            course.enrolledStudents += 1
            print("Enrollment for", self.name, "is successful for", course.code)

        else:
            print("Enrollment for", self.name, "is NOT successful for", course.code, "due to capacity")

    def printEnrolledCourses(self):
        print(self.__str__())
        print("Registered courses are as follows:")
        for c in self.registeredCourses:
            print(c)

class FacultyMember(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.teachingCourses = []
    
    def teachCourse(self, course):
        self.teachingCourses.append(course)
    
    def printTeachingCourses(self):
        print()
        if len(self.teachingCourses) > 0:
            print("Here is the courses given by", self.name)
            for c in self.teachingCourses:
                print(c)
        else:
            print("No courses given by", self.name)

p1 = Person("Jack", 20)

c1 = Course("DSA201", 1, 3)
c2 = Course("IF100", 2, 3)
c3 = Course("HIST191", 3, 2)

s1 = Student("Ahmet", 20, 1, "Sabanci University")
s2 = Student("Ayse", 20, 2, "Sabanci University")
s3 = Student("Damla", 20, 3, "Sabanci University")

s1.enrollCourse(c1)
s2.enrollCourse(c1)

s1.enrollCourse(c2)
s2.enrollCourse(c2)
s3.enrollCourse(c2)

s1.printEnrolledCourses()

f1 = FacultyMember("Duygu", 35)
f1.teachCourse(c2)
f1.teachCourse(c1)
f1.printTeachingCourses()

f2 = FacultyMember("Emre", 36)
f2.printTeachingCourses()