#rock-paper-scissors
import random

L=['rock','paper','scissors']

mark_p=0
mark_c=0

while(1):
    choice_p=int(input("\nEnter 1 for rock, 2 for paper, 3 for scissors: "))
    if choice_p>=4 or choice_p<1:
        print("Enter 1-3")
        continue
    
    choice_c=random.choice(L)
    print("\nUser's choice:",L[choice_p-1],", Computer's choice: ",choice_c,"\n")
    if L[choice_p-1] == choice_c:
        print("DRAW")
    elif L[choice_p-1] == L[0] and choice_c==L[1]:
        mark_c+=1
    elif L[choice_p-1] == L[1] and choice_c==L[2]:
        mark_c+=1
    elif L[choice_p-1] == L[2] and choice_c==L[0]:
        mark_c+=1
        
    else:
        mark_p+=1
        
    print("Player:",mark_p,"\nComputer:",mark_c)
    ch=int(input("Do you want to continue(1-yes, 2-no)? "))
    if ch==1:
        continue
    else:
        break 
        
if mark_p>mark_c:
    print("Player wins")
elif mark_c>mark_p:
    print("Computer wins")
else:
    print("It's a DRAW!!")
    
    




