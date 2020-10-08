#https://github.com/MrPolarbearNinja/TileTraveller.git

x = 1
y = 1

while True:
    #hér kemur "You can travel"
    if x==1:
        if y == 1:
            valid = "(N)orth."
            val_input= 'n', 'N'
        elif y==2:
            valid = "(N)orth or (E)ast or (S)outh."
            val_input= 'n', 'N', 'e', 'E', 's', 'S'
        elif y==3:
            valid = "(E)ast or (S)outh."
            val_input= 'e', 'E', 's', 'S'
    elif x==2:
        if y == 1:
            valid = "(N)orth."
            val_input= 'n', 'N'
        elif y==2:
            valid = "(S)outh or (W)est."
            val_input= 'w', 'W', 's', 'S'
        elif y==3:
            valid = "(E)ast or (W)est."
            val_input=  'e', 'E', 'w', 'W'
    elif x==3:
        if y == 1:
            print("Victory!")
            break
        elif y==2:
            valid ="(N)orth or (S)outh."
            val_input= 'n','N','s','S'
        elif y==3:
            valid ="(S)outh or (W)est."
            val_input= 'w', 'W', 's', 'S'
    print("You can travel:", valid)

    direction = str(input("Direction: "))
    if direction in val_input:
        if (direction == 'n') or (direction == 'N'):
            y += 1
        elif (direction == 'w') or (direction == 'W'):
            x -= 1
        elif (direction == 'e') or (direction == 'E'):
            x += 1
        elif (direction == 's') or (direction == 'S'):
            y -= 1
    else:
        print("Not a valid direction!")
    #directions búið
    
    #(S)outh
    #(E)ast
    #(N)orth
    #(W)est
    #1,1 valid = n
#1,2 valid = n,s,e
#1,3 valid = s,e
#2,1 valid = n
#2,2 valid = w,s
#2,3 valid = w,e
#3,3 valid = w,s
#3,2 valid = n,s
  
