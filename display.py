
import sys

def text_to_array():
    text_array=[]

    # opening the text file for reading using open() function
    with open('data.txt') as file:   
        for line in file:  
            line=line.rstrip()
            line=line.split(",")  
            text_array.append(line)
    return(text_array)


def display():
    costumes='''
░█████╗░░█████╗░░██████╗████████╗██╗░░░██╗███╗░░░███╗███████╗░██████╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║░░░██║████╗░████║██╔════╝██╔════╝
██║░░╚═╝██║░░██║╚█████╗░░░░██║░░░██║░░░██║██╔████╔██║█████╗░░╚█████╗░
██║░░██╗██║░░██║░╚═══██╗░░░██║░░░██║░░░██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░╚██████╔╝██║░╚═╝░██║███████╗██████╔╝
░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═════╝░'''

    print(costumes,"\n")
    a=1
    array1=text_to_array()
    print("We have the following costumes available for rent:\n ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
           
    print("S/N  Costumes                      Brand                        Charge                 Available quantity")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

    # displaying the elements of array1
    for i in array1:
        print(a,".",i[0]," "*(28-len(i[0])),i[1]," "*(28-len(i[1])),i[2]," "*(28-len(i[2]))
        ,i[3])
        a=a+1
    
    display_input1=input("Do you want to go main menu?(Y/N)")   
    if display_input1=="Y":
        from main import main 
        main()
    else:
        sys.exit()



