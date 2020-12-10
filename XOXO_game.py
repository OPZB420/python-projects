import random as rand 
import time
l1=[' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '];l2=[];l3=[]
def board():
    
    print(' '+l1[0]+' | '+l1[1]' | '+l1[2]+' '+' 1 | 2 | 3')
    print('------------  -----------------')
    print(' '+l1[3]+' | '+l1[4]' | '+l1[5]+' '+' 4 | 5 | 6')
    print('------------  -----------------')
    print(' '+l1[6]+' | '+l1[7]' | '+l1[8]+' '+' 7 | 8 | 9')
def mp():
    def decision():
        if l1[0]==l1[1]==l1[2]==a or l1[0]==l1[3]==l1[6]==a or l1[0]==l1[4]==l1[8]==a or l1[1]==l1[4]==l1[7]==a or l1[2]==l1[5]==l1[8]==a or l1[3]==l1[4]==l1[5]==a or l1[6]==l1[7]==l1[8]==a or l1[2]==l1[4]==l1[6]==a:
            return True
        if l1[0]==l1[1]==l1[2]==b or l1[0]==l1[3]==l1[6]==b or l1[0]==l1[4]==l1[8]==b or l1[1]==l1[4]==l1[7]==b or l1[2]==l1[5]==l1[8]==b or l1[3]==l1[4]==l1[5]==b or l1[6]==l1[7]==l1[8]==b or l1[2]==l1[4]==l1[6]==b:
            return False
    def player1():
        while True:
            try1=input("\n%s: \nEnter your place : "%(n1))
            if try1 in '123456789' and try1 not in '':
                try1= int(try1)
                if try1 not in l2 and try1 not in l3:
                    l2.append(try1)
                    l1[try1-1]=a;time.sleep(0.25)
                    board();break
                else :
                    print("Place already choosen please try again")
                    continue
            else:
                    print('Invaled place entered ........please try again and enter a correct place')
                    continue
        def player2():
            while True:
                try2=input("\n%s: \nEnter your place : "%(n2))
                if try2 in '123456789' and try2 not in '':
                    try2= int(try2)
                    if try2 not in l2 and try2 not in l3:
                        l3.append(try2)
                        l1[try2-1]=b;time.sleep(0.25)
                        board();break
                    else:
                        print("Place already choosen please try again")
                        continue
                else:
                    print('Invalid place entered.....please try again and enter correct place')
                    continue
        def play():
            for i in range(5):
                player1()
                if decision()==False:
                    print("Game over...", n2,"Wins");break 
                elif decision()==True:
                    print('Game Over.....',n1,'Wins');break
                if i!= 4:
                    player2()
                if decision()==False:
                    print("Game Over...", n2,'Wins');break
                elif decision()==True:
                    print("Game Over...", n2,'Wins');break
            else:
                print("GAME Over.....Match is tied")
    n1= input('\nP1, Enter your name : ')
    n2= input("\nP2, Enter your name : ")
    a = input("\n%s, Enter your symbol : "%(n1))
    b = input("\n%s, Enter your symbol : "%(n2))
    print('''\n #### If value need ) use this 
The no.(s) for position are :-
    |   |       1 | 2 | 3
------------   ------------
    |   |       4 | 5 | 6
-----------    ------------
    |   |       7 | 8 | 9  ''')
    play()
def comp():
    print('''\n
The no.(s) for position are :-
    |   |       1 | 2 | 3
----------     ----------
    |   |       4 | 5 | 6
----------     ----------
    |   |       7 | 8 | 9  ''')
    def player1():
        while True:
            try1=input("\n%s:\nEnter your place : "%(n))
            if try1 in '123456789' and try1 not in '':
                try1 =int(try1)
                if try1 not in l2 and try1 not in l3:
                    l2.append(try1)
                    l1[try1-1]='0';time.sleep(0.3)
                    board();break
                else:
                    print("Please already choosen please try again")
                    continue
            else:
                print('Invalid place entered.....please try again and enter a correct place')
    def decision():
        if l1[0]==l1[1]==l1[2]=='X' or l1[0]==l1[3]==l1[6]=='X' or l1[0]==l1[4]==l1[8]=='X' or l1[1]==l1[4]==l1[7]=='X' or l1[2]==l1[5]==l1[8]=='X' or l1[3]==l1[4]==l1[5]=='X' or l1[6]==l1[7]==l1[8]=='X' or l1[2]==l1[4]==l1[6]=='X':
            return False
        if l1[0]==l1[1]==l1[2]=='O' or l1[0]==l1[3]==l1[6]=='O' or l1[0]==l1[4]==l1[8]=='O' or l1[1]==l1[4]==l1[7]=='O' or l1[2]==l1[5]==l1[8]=='O' or l1[3]==l1[4]==l1[5]=='O' or l1[6]==l1[7]==l1[8]=='O' or l1[2]==l1[4]==l1[6]=='O':
            return True
    def easy():
        if (l1[0]==l1[3]=='X' or l1[4]==l1[2]=='X' or l1[8]==l1[7]=='X') and l1[6]==' ':
            X = 7;l3.append(X)
            l1[6]='X'
        elif (l1[4]==l1[0]=='X' or l1[7]==l1[6]=='X' or l1[2]==l1[5]=='X') and l1[8]==' ':
            X = 9;l3.append(X)
            l1[8]='X'
        elif (l1[6]==l1[4]=='X' or l1[0]==l1[1]=='X' or l1[8]==l1[5]=='X') and l1[2]==' ':
            X = 3;l3.append(X)
            l1[2]='X'
        elif (l1[1]==l1[2]=='X' or l1[3]==l1[6]=='X' or l1[8]==l1[4]=='X') and l1[0]==' ':
            X = 1;l3.append(X)
            l1[0]='X'
        elif (l1[0]==l1[8]=='X' or l1[2]==l1[6]=='X' or l1[1]==l1[7]=='X' or l1[3]==l1[5]=='X') and l1[4]==' ':
            X = 5;l3.append(X)
            l1[4]='X'
        elif (l1[0]==l1[2]=='X' or l1[4]==l1[7]=='X') and l1[1]==' ':
            X = 2;l3.append(X)
            l1[1]='X'
        elif (l1[0]==l1[6]=='X' or l1[4]==l1[5]=='X') and l1[3]==' ':
            X =4;l3.append(X)
            l1[3]='X'
        elif (l1[2]==l1[8]=='X' or l1[3]==l1[5]=='X') and l1[5]==' ':
            X = 6;l3.append(X)
            l1[5]='X'
        elif (l1[1]==l1[4]=='X' or l1[6]==l1[8]=='X') and l1[7]==' ':
            X=8;l3.append(X)
            l1[7]='X'
        else:
            if (l1[0]==l1[3]=='O' or l1[4]==l1[2]=='O' or l1[8]==l1[7]=='O') and l1[6]==' ':
                X=7;l3.append(X)
                l1[6]='X'
            elif (l1[4]==l1[0]=='O' or l1[7]==l1[6]=='O' or l1[2]==l1[2]==l1[5]=='O') and l1[8]==' ':
                X =9;l3.append(X)
                l1[8]='X'
            elif (l1[6]==l1[4]=='O' or l1[0]==l1[1]=='O' or l1[8]==l1[5]=='O') and l1[2]==' ':
                X=3;l3.append(X)
                l1[2]='X'
            elif (l1[1]==l1[2]=='O' or l1[3]==l1[6]=='O' or l1[8]==l1[4]=='O') and l1[0]==' ':
                X=1;l3.append(X)
                l1[0]='X'
            elif (l1[0]==l1[8]=='O' or l1[2]==l1[6]=='O' or l1[1]==l1[7]=='O' or l1[3]==l1[5]=='O') and l1[4]==' ':
                X=5;l3.append(X)
                l1[4]='X'
            elif (l1[0]==l1[2]=='O' or l1[4]==l1[7]=='O') and l1[1]==' ':
                X=2;l3.append(X)
                l1[1]='X'
            elif (l1[0]==l1[6]=='O' or l1[4]==l1[5]=='O') and l1[3]==' ':
                X=4;l3.append(X)
                l1[3]='X'
            elif(l1[2]==l1[8]=='O' or l1[3]==l1[4]=='O') and l1[5]==' ':
                X=6;l3.append(X)
                l1[5]='X'
            elif(l1[1]==l1[4]=='O' or l1[6]==l1[8]=='O') and l1[7]==' ':
                X=8;l3.append(X)
                l1[7]='X'
            else:
                while True:
                    X=rand.randint(1,9)
                    if X not in 12 and X not in l3:
                        l3.append(X)
                        l1[X-1]='X'
                        break
    step()
def step():
    print('\nComputer is thinking')
    for i in range(4):
        time.sleep(0.3)
        print('.')
    print()
    board()
def play():
    for i in range(5):
        player1()
        if decision()==False:
            print("Game Over .... Computer wins wins");break
        elif decision()==True:
            print("Game Over.....You win");break
        if i==0 and l1[4]=='O':
            c=rand.choice([0,2,6,8])
            l1[c]='X';step()
        elif i==1 and l1[4]=='O':
            if (l1[0]==l1[3]=='O' or l1[4]==l1[2]=='O' or l1[8]==l1[7]=='O') and l1[6]==' ':
                X=7;l3.append(X)
                l1[6]='X';step()
            elif (l1[4]==l1[0]=='O' or l1[7]==l1[6]=='O' or l1[2]==l1[5]=='O') and l1[8]==' ':
                X=9;l3.append(X)
                l1[8]='X';step()
            elif(l1[6]==l1[4]=='O' or l1[0]==l1[1]=='O' or l1[8]==l1[5]=='O') and l1[2]==' ':
                X=3;l3.append(X)
                l1[2]='X';step()
            elif(l1[1]==l1[2]=='O' or l1[3]==l1[6]=='O' or l1[8]==l1[4]=='O') and l1[0]==' ':
                X=1;l3.append(X)
                l1[0]='X';step()
            elif(l1[0]==l1[8]=='O' or l1[2]==l1[6]=='O' or l1[1]==l1[7]=='O' or l1[3]==l1[5]=='O') and l1[4]==' ':
                X=5;l3.append(X)
                l1[4]='X';step()
            elif(l1[0]==l1[2]=='O' or l1[4]==l1[7]=='O') and l1[1]==' ':
                X=2;l3.append(X)
                l1[1]='X';step()
            elif(l1[0]==l1[6]=='O' or l1[4]==l1[5]=='O') and l1[3]==' ':
                X=4;l3.append(X)
                l1[3]='X';step()
            elif(l1[2]==l1[8]=='O' or l1[3]==l1[5]=='O') and l1[5]==' ':
                X=6;l3.append(X)
                l1[5]='X';step()
            elif(l1[1]==l1[4]=='O' or l1[6]==l1[8]=='O') and l1[7]==' ':
                x=8;l3.apend(X)
                l1[7]='X';step()
            else:
                while True:
                    c=rand.choice([0,2,6,8])
                    if l1[c]==' ':
                        l1[c]='X';step();break
        else:
            if i!= 4:
                easy()
        if decision()==False:
            print("Game over ... Compute wins");break
        elif decision()==True:
            print('Game over... You win');break
    else:
        print('Game over...match is tied')
n= input('Enter your name : ')
play()
while True:
    print('''
Which mode do you want to play ?
1. Multiplayer
2. v/s computer ''')
    ch=input('Enter you choise : ')
    if ch in '12' and ch not in '':
        if ch=='1':
            mp()
            z=input('\nPress any key (+enter) to play again , else press enter key : ')
            if z=="":
                quit()
            else:
                continue
        elif ch=='2':
            comp()
            z=input('\nPress any key (+enter) to paly again, else press enter : ')
            if z=="":
                quit()
            else:
                continue
    else:
        print("\n Invalid choise ")
        X =input("press any key(+enter) to try again, else press enter : ")
        if x=='':
            quit()
        else:
            continue
                    
                    
                
            