"""    
Author : Ahmet Cemal Sert
Title: CMPE326 HW1
"""

# Creates a printer (list) with a 11*11 dots (21*21 2D list)
# Returns the list
def createPrinter():
    list = [
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."]
    ]
    return list


# Prints the output
# Takes a 2D list as parameter and prints it out  
def printOutput2(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            print(list[i][j],end=" ")
        print("")


# Main function 
def main():

    # Creates printer
    printer = createPrinter()

    # Creates an empty dictionary which will be used to keep logo names(key) and logo shapes(value) later on 
    dictionary = {} 

    loopFlag = True

    while(loopFlag):

        # Takes input from keyboard and assigns it to command
        command = input("Type your command :")

        # Splits it according to space char (" ") 
        commandList = command.split(" ")
        
        # If first argument is LOGO 
        if(commandList[0] == "LOGO"):

            # Assigns first first command after LOGO to logoName and second command to logoShape 
            logoName = commandList[1]
            logoShape = commandList[2]
            
            # Key : Logoname , Value: logoShape
            dictionary[logoName] = logoShape 

            print(logoName+ " defined")

        # If first argument is ENGRAVE
        elif(commandList[0] == "ENGRAVE"):

            logoName = commandList[1]
            x_coordinate = int(commandList[2])
            y_coordinate = int(commandList[3])

            # loops through the dictionary 
            for key in dictionary.keys(): 
                # if logo name is one of the keys
                if(key == logoName): 
                    # the value will be shape of that key
                    # convert the key to string  
                    value = str(dictionary[key])
                
                    for char in value:
                        if(char == 'D'): 
                            printer[(2*x_coordinate-1)][(2*y_coordinate-1)-1] = "|"
                            x_coordinate += 1
                        elif(char == 'U'):  
                            printer[(2*x_coordinate-1)-2][(2*y_coordinate-1)-1] = "|"
                            x_coordinate-=1
                        elif(char == 'R'): 
                            printer[(2*x_coordinate-1)-1][(2*y_coordinate-1)] = "_"
                            y_coordinate+=1
                        elif(char == 'L'):
                            printer[(2*x_coordinate-1)-1][(2*y_coordinate-1)-2] = "_"
                            y_coordinate-=1
                        else:
                            print("Invalid direction. The directions can be only 'R' , 'L' , 'U' , 'D' ")

            # Prints the list 
            printOutput2(printer)
            
            # Resets the printer after engrave operation in order to engrave again 
            printer = createPrinter()           
                    
        elif(commandList[0] == "SAME"):

            cmd1 = commandList[1] # logo name
            cmd2 = commandList[2] # logo name 

            # Checks if logoShapes are same since in my dictionary logo names are key and logoShapes are values 
            if(str(dictionary[cmd1]) == str(dictionary[cmd2])): 
                print("They are same")

            # Checks if the reverse of string is same since the shapes will be the same anyways     
            elif(str(dictionary[cmd1]) == str(dictionary[cmd2])[::-1]): 
                print("They are same")

            # Any other case they won't be the same 
            else : 
                print("They are not same") 

        # Press q to exit 
        elif (commandList[0] == "Q" or commandList[0]=="q"):
            loopFlag = False

        else:
            print("Invalid Command")    

    
#Main function call 
main()
