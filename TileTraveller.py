import random

def lever_option(coins):
    pullAns = random.choice(['y', 'n'])
    print("Pull a lever (y/n):", pullAns)
    if (pullAns == "y"):
        coins += 1
        print("You received 1 coin, your total is now {}.".format(coins))
        return coins
    return coins
        
def playagain():
    again = input("Play again (y/n): ")
    if again.lower() == 'y':
        main()
def canTravel(x,y,coins,moved):
    #hér kemur "You can travel"
    
    if x==1:
        if y == 1:
            valid = "(N)orth."
            val_input= 'n', 'N'
        elif y==2:
            if (moved):
                coins = lever_option(coins)
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
            if (moved):
                coins = lever_option(coins)
            valid = "(S)outh or (W)est."
            val_input= 'w', 'W', 's', 'S'
        elif y==3:
            if (moved):
                coins = lever_option(coins)
            valid = "(E)ast or (W)est."
            val_input=  'e', 'E', 'w', 'W'           
    elif x==3:
        if y == 1:
            
            val_input = 'victory'
        elif y==2:
            if (moved):
                coins = lever_option(coins)
            valid ="(N)orth or (S)outh."
            val_input= 'n','N','s','S'
        elif y==3:
            valid ="(S)outh or (W)est."
            val_input= 'w', 'W', 's', 'S'
    if val_input != 'victory':
        print("You can travel:", valid)
    return val_input, coins
def move(val_input):
    direction = random.choice(['n', 'e', 's', 'w'])
    print("Direction:", direction)
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
        return 'inval'
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
    x = 1
    y = 1
    coins = 0
    moved = True
    moves = 0

    seed = int(input("Input seed: "))
    random.seed(seed)
    
    while True:
        valid = canTravel(x,y,coins,moved)
        coins = valid[1]
        if valid[0] == 'victory':
            print("Victory! Total coins {}. Moves {}.".format(coins,moves))
            break
        movement = move(valid[0])
        moves += 1
        
        if (movement == 'inval'):
            moved = False
        else:
            moved = True    
        if movement == 'Xadd':
            x+=1
        elif movement == 'Xsub':
            x-=1
        elif movement == 'Yadd':
            y+=1
        elif movement == 'Ysub':
            y-=1
    playagain()
main()
