__author__ = "Prajesh Ananthan"


class LotteryPlayer:
    def __init__(self):
        self.name = "Prajesh"
        self.numbers = (5, 9, 12, 3, 1, 21)


player_one = LotteryPlayer()
player_two = LotteryPlayer()

print(player_one.name)
print(player_one.numbers)
print(player_one == player_two)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to MIT")


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())

Student.go_to_school()
