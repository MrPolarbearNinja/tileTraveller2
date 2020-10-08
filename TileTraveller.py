x = 1
y = 1
coins = 0

def lever_option(coins):
    pullAns = input("Pull a lever (y/n): ")
    if (pullAns == "y"):
        coins += 1
        print("You received 1 coin, your total is now {}.".format(coins))
        

def canTravel(x,y):
    #hér kemur "You can travel"
    
    if x==1:
        if y == 1:
            valid = "(N)orth."
            val_input= 'n', 'N'
        elif y==2:
            lever_option(coins)
            valid = "(N)orth or (E)ast or (S)outh."
            val_input= 'n', 'N', 'e', 'E', 's', 'S'
            lever = True
        elif y==3:
            valid = "(E)ast or (S)outh."
            val_input= 'e', 'E', 's', 'S'
    elif x==2:
        if y == 1:
            valid = "(N)orth."
            val_input= 'n', 'N'
        elif y==2:
            lever_option(coins)
            valid = "(S)outh or (W)est."
            val_input= 'w', 'W', 's', 'S'
            lever = True
        elif y==3:
            lever_option(coins)
            valid = "(E)ast or (W)est."
            val_input=  'e', 'E', 'w', 'W'
            lever = True
    elif x==3:
        if y == 1:
            print("Victory! Total coins {}."format(coins))
            break
        elif y==2:
            lever_option(coins)
            valid ="(N)orth or (S)outh."
            val_input= 'n','N','s','S'
            lever = True
        elif y==3:
            valid ="(S)outh or (W)est."
            val_input= 'w', 'W', 's', 'S'
    print("You can travel:", valid)
    return val_input
def move(val_input)
    direction = str(input("Direction: "))
    if direction in val_input:
        if (direction == 'n') or (direction == 'N'):
            #y += 1
            return 'Yadd'
        elif (direction == 'w') or (direction == 'W'):
            #x -= 1
            return 'Xsub'
        elif (direction == 'e') or (direction == 'E'):
            #x += 1
            return 'Xadd'
        elif (direction == 's') or (direction == 'S'):
            #y -= 1
            return 'Ysub'

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
def main():
    x=1
    y=1
    while True:
        valid = canTravel(x,y)
        move = move(valid)
