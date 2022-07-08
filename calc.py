print ("#"*10,"Hello, it's simple calculator","#"*10)
result=0

def Plus (num1,num2):
    result = num1 + num2
    return result
def Mines (num1,num2):
    result = num1 - num2
    return result
def Multipl (num1,num2):
    result = num1 * num2
    return result
def Div (num1,num2):
    if num2 == 0:
        result ="Error!!!Cant / on \"0\""
        
    else:
        result = num1/num2
    return result
while True:
    
    num1 = float(input ("Enter first number : "))
    num2 = float(input ("Enter second number : "))
    choise = input('Choise "+" "-" "/ " "*" :')
    if choise == '+':
        print(Plus (num1,num2))
        
    elif choise == '-':
        print(Mines (num1,num2))
    
    elif choise == '*':
        print(Multipl (num1,num2))
    elif choise == '/':
        print(Div (num1,num2))
    else : print("Error, bad choise, try again!!!") ; continue
    end=(input('Are you want to continue? Any key for continue and "Q,q" for exit :'))
    if end == 'q' or end =='Q':
        break
    
    
     
        