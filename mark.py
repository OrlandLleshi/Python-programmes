inp = input("Please enter your mark: ")

if  int(inp) >= 85:
    print("Congratulations, you achieved a Distinction")
elif int(inp) >= 65 and int(inp) <= 85:
    print("Congrats, you have passed")
else:
    print("You have failed")