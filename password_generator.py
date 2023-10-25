import random
import string

alphabets = list(string.ascii_lowercase)

digits = list(string.digits)

special=['@','#','$','%','&','^','(',')','_','+','!'] 
'''use of special characters is dependent on the guidelines of the platform 
where the password is being used. For the sake of generating 
passwords some of the special characters have been used here.'''

print("Greetings of the Day!\nThis is to help you generate a strong password.")
n=int(input("Enter the length of the password required to be generated: "))

while(1):
    a=int(input("Enter the number of alphabets required in the password: "))
    d=int(input("Enter the number of digits required in the password: "))
    s=int(input("Enter the number of special characters required in the password: "))
    
    if (a+s+d)!=n:
        print("The sum of number of alphabets/digits/special characters does not match the password length")
        print()
    else:
        break


password=[]
for i in range(a):
    password.append(random.choice(alphabets))
for i in range(d):
    password.append(random.choice(digits))
for i in range(s):
    password.append(random.choice(special))

final_psswrd=[]
for i in range(n):
    rm=random.choice(password)
    final_psswrd.append(rm)
    password.remove(rm)

final_psswrd="".join(final_psswrd)

print("The password generated for you is:",final_psswrd)




