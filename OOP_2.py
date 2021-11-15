class Student:
    def __init__(self, name = "Ivan", groupNumber = "10A", age = 18):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber
        pass
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
        return f"{name}, {age}"
    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber
        return groupNumber

ignoramus = Student()

print(ignoramus.getName(), ignoramus.getGroupNumber(), ignoramus.getAge())
ignoramus_2 = Student()
ignoramus_3 = Student()
ignoramus_4 = Student()
ignoramus_5 = Student("Anton", "11B", 17)
print(ignoramus_2.setNameAge("Alex", 16), ignoramus_2.setGroupNumber("10B"))
print(ignoramus_3.setNameAge("Kirill", 15), ignoramus_2.setGroupNumber("9A"))
print(ignoramus_4.setNameAge("Julia", 17), ignoramus_2.setGroupNumber("11C"))
print(ignoramus_5.getName(), ignoramus_5.getGroupNumber(), ignoramus.getAge())

