class Student:
    class_="student"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
       

    def average(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

        avg = (self.mark1 + self.mark2 + self.mark3) // 3
        print(f"{self.name} achieved {avg} overall")



Orland = Student("Orland", "26",)
Orland.average(100, 65, 65)

