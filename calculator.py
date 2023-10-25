#codsoft task- simple calculator

def calculator(op,n1,n2):
    if(op=='%'):
        return n1%n2
    elif(op=='/'):
        return n1/n2
    elif(op=='*'):
        return n1*n2
    elif(op=='+'):
        return n1+n2
    elif op=='-':
        return n1-n2
    
    
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
op=input("Enter the operation you need to perform(among %,/,*,+,-): ")
res=calculator(op,n1,n2)
    
print(n1,op,n2,"=",res)