class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex= sex

people_1 = People("jason", 20, "male")
# print(people_1.name) #people 클래스  테스트용

class Colleague(People):
    position = "대리"
    
colleague_1 = Colleague("Tom", 40, "male")
colleague_2 = Colleague("Amy", 30, "female")
colleague_3 = Colleague("sindy", 24, "female")

print(colleague_1.age)
print(colleague_2.sex)
print(colleague_3.name)
