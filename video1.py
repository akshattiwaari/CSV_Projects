Stack=[]

def PUSH():
    ch=int(input('Enter a number to be inserted :'))
    Stack.append(ch)

def POP():
    if Stack==[]:
        print('Underflow')
    else:
        Stack.pop(-1)

def PEEK():
    if Stack==[]:
        print('Underflow')
    else:
        print(Stack[-1])

def DISPLAY():
    for i in range(len(Stack)):
        print(Stack[i])

while True:
    ln=int(input('Enter 1 for PUSH\nEnter 2 for POP\nEnter 3 for PEEK\nEnter 4 for DISPLAY :'))
    if ln==1:
        PUSH()
    elif ln==2:
        POP()
    elif ln==3:
        PEEK()
    elif ln==4:
        DISPLAY()
    else:
        print('Thanks you')
        break
