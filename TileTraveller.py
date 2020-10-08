#https://github.com/MrPolarbearNinja/TileTraveller.git

posibleRouts = ""
curentPlace = "11"


def update_place(move, curentPlace):
    if move == "n":
        curentPlace = str(int(curentPlace) + 1)
    elif move == "e":
        curentPlace = str(int(curentPlace) + 10)
    elif move == "s":
        curentPlace = str(int(curentPlace) - 1)
    elif move == "w":
        curentPlace = str(int(curentPlace) - 10)
    return curentPlace


def printPosibleDirections (placement):
    posible = ""
    writeLine = "You can travel: "
    counter = 0
    posibleRouts = ""
    
    if not(placement[1] == "3"):
        if not(placement[0] == "2" and placement[1] == "2"):
            writeLine += "(N)orth"
            posible += "n"
            counter += 1
    if not(placement[0] == "3"):
        if not(placement[0] == "1" and placement[1] == "1"):
            if not(placement[0] == "2" and placement[1] == "2"):
                if not(placement[0] == "2" and placement[1] == "1"):
                    if(counter > 0):
                        writeLine += " or "
                    writeLine += "(E)ast"
                    posible += "e"
                    counter += 1
    if not(placement[1] == "1"):
        if not(placement[0] == "2" and placement[1] == "3"):
            if(counter > 0):
                writeLine += " or "
            writeLine += "(S)outh"
            posible += "s"
            counter += 1
    if not(placement[0] == "1"):
        if not(placement[0] == "2" and placement[1] == "1"):
            if not(placement[0] == "3" and placement[1] == "1"):
                if not(placement[0] == "3" and placement[1] == "2"):
                    if(counter > 0):
                        writeLine += " or "
                    writeLine += "(W)est"
                    posible += "w"
    print(writeLine + ".")
    posibleRouts = updateForbiten(posible, posibleRouts)
    return posibleRouts

def updateForbiten(fb_list, posibleRouts):
    posibleRouts = fb_list
    return posibleRouts
    
def checkPosible(WhatToCheck):
    if(WhatToCheck in posibleRouts):
        return True
    else:
        return False


while (True):
    posibleRouts = printPosibleDirections(curentPlace)
    direction = input("Direction: ")
    direction = direction.lower()

    if not(direction == "n" or direction == "e" or direction == "s" or  direction == "w"):
        print("Not a valid direction!")
    else:
        if(checkPosible(direction)):
            curentPlace = update_place(direction, curentPlace)
        else:
            print("Not a valid direction!")
    if (curentPlace == "31"):
        print("Victory!")
        break
            
                      
