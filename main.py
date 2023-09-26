import sys

def main():
    welcome='''
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝'''
    
    print(welcome,"\n")
    try:
        option=int(input(''' Weclome to Gurung Costumes!
        1: Show the available costumes for renting
        2: Enter 2 to rent  costumes
        3: Enter 3 to return rented costumes
        4: Enter 4 for exiting: \n'''))
    except:
        print("Please check your input(Only integers allowed).")   
    if option==1:
        import display # importing display module
        display.display()
    elif option ==2:
        import rent_costume
        rent_costume.rent_costume() # importinf rent_costume module
    elif option ==3:
        import return_costume # importing return_costume module
        return_costume.return_costume()
    elif option ==4:
        sys.exit()
    else:
        print("Please enter valid numbeers(1,2,3 or 4)")
        main()
    display_input1=input("Do you want to go main menu?(Y/N)")   
    if display_input1=="Y":
        from main import main 
        main()
    else:
        sys.exit()
               
main()
