math= int(input("What is your maths score: "))
physics = int(input("What is your physics score: "))
chem = int(input("What is your chem score: "))

percent = (math + physics + chem) // 3
print(f"Your percentage score is {percent}% ")

if percent > 70:
    print("You scored a grade of A")
elif percent >60 and percent < 70:
    print("You scored a grade of B")
elif percent > 50 and percent < 60:
    print("You scored a grade of C")
elif percent > 40 and percent < 50:
    print("You scored a grade of D")
else:
    print("You failed")
