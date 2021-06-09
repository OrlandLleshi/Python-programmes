mult= int(input("Which number would you like to input?: "))

for i in range(1,mult):
    for j in range(1,mult):
        print(i*j, end='\t')
    print('')

