import random
import time
print("...................... Welcome ....................")
print()
print()
print("It's just MIND Reading Game ")
print()
a = input("Enter you'r name : ")
time.sleep(0.1)
print()
b = input("Enter your'r Age : ")
time.sleep(0.2)
print()
print("Select the number between 1 to 10 \nin you'r mind dont't tell me  ")
print()
j = input("Type 'y Or Y Or Yes Or yes' when done : ")
for i in range(1,4):
    print("  .")
    time.sleep(1.0)
print()
print("Now multiply the number from --> 9 ")
print()
l = input("Type 'y Or Y Or Yes Or yes' when done : ")
for i in range(1,4):
    print("  .")
    time.sleep(1.0)
print()
print("Now you should get two digits plus both the digits")
print("e.g. If you got 55 then 5+5 10 ")
print("e.g. If you got One digit then No need to anything !!! ")
print()
x = input("Type 'y Or Y Or Yes Or yes' when done : ")
print()
z = random.randint(1,8)
b = z + 9
print(f"Now add {z} in your answer")
print()
v = input("Type 'y Or Y Or Yes Or yes' when done : ")
for i in range(1,6):
    print("  .")
print()
print(f"You'r ans is !!!--------> {b} <---------!!!")
time.sleep(1)
print()
print()
print(f"            Thanks for Participation {a}      ")
print()