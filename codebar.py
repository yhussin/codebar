class Member: 
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi, my name is {self.full_name}")


class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason
        print(f"{self.full_name}: My reason for attending is: {self.reason}")

class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)


class Workshop: 
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, member):
        if type(member) == Instructor:
            self.instructors.append(member)
        else:
            self.students.append(member)
        

    def print_details(self):
        print(f"Workshop was on {self.date}, the subject was {self.subject}")
        
        for i in self.students:
            print(f"{i.full_name}")

        for i in self.instructors:
            print(f"{i.full_name} - {i.skills}")

    


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()

# =>
# Workshop - 12/03/2014 - Shutl
#
# Students
# 1. Jane Doe - I am trying to learn programming and need some help
# 2. Lena Smith - I am really excited about learning to program!
#
# Instructors
# 1. Vicky Ruby - HTML, JavaScript
#    I want to help people learn coding.
# 2. Nicole McMillan - Ruby
#    I have been programming for 5 years in Ruby and want to spread the love
#