a = input(" Welcome to pyramid builder \n \n Do you want a pyramid \n if yes press 'y', \n Else press any thing. \n your choise : ")
if a=='y' or a=='Y':
    y=input("Do you want costumise pyramid \n \n if yes press 'y', \n Else press anyting : ")
    if y=='y' or y=='Y':
        b=int(input("Enter the number of stars \n You want at its base \n ::: "))
        for i in range (0,b+1):
            print("*"*i)
            
            i+=1
            if i==b+1:
                print("Your Pyramid is completes \n ")
    else:
        for z in range(0,21):
            if 0<z<=5:
                print("$"*z)
            elif 5<z<=10:
                print("$"*z)
            elif 10<z<20:
                print("$"*20)
            else:
                print("~:"*z)
        z+=1
else:
    print("Thanks for Visit")