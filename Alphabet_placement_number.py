while True:
    word = input("Input a Word : ")
    if word.isalpha():
        num = [str(ord(char)-96)
        for char in word.lower()]
        break
    else:
        print("Invalid Input")
print("\n->->->->->")
print("Alphabetical Placement : {}".format(num),end='')