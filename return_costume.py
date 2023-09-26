from ast import While
import sys
from display import text_to_array

def return_costume():
    display_return='''
██████╗░███████╗████████╗██╗░░░██╗██████╗░███╗░░██╗
██╔══██╗██╔════╝╚══██╔══╝██║░░░██║██╔══██╗████╗░██║
██████╔╝█████╗░░░░░██║░░░██║░░░██║██████╔╝██╔██╗██║
██╔══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔══██╗██║╚████║
██║░░██║███████╗░░░██║░░░╚██████╔╝██║░░██║██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝'''

    print(display_return,"\n")
    name=input("Enter your name: ")
    address=input("Enter your address: ")
    contact=input("Enter your contact number: ")
    file=open("%s %s.txt" % ("Returned by", name),"w")# creates the file 
    file.write("%s %s" % ("Customer Name: ", name)) # writes the name of customer 
    file.write("%s %s" % ("\nCustomer Address: ", address)) # writes the address of customer
    file.write("%s %s" % ("\nCustomer contact: ", contact))# writes the contact of customer

    from datetime import datetime
    now=datetime.now()
    dateandtime=now.strftime("%d/%m/%Y %H:%m:%S")
    file.write("%s %s" % ("\n\nReturned: ", dateandtime))# writes the current date and time in the file
    file.write("\n\nBorrow Details: ")
    file.write("\n____________________________________________")

    return_array=text_to_array()
    total_fine=0
    return_=True
    while return_==True:
        try:
            return_display= int(input(''' Enter the number of costume which you are returning
              1: Cop Costume Set
              2: Formal Suite (Black Premium)
              3: Fairy Costume Full Set
              4: Full Metal Alchemist Set
              5: Black-Buttler (Sebastian)
              6: Jotaro Kujo (Exclusive)\n
              Enter : '''))
        except:
            print("Please check your input(Only integers allowed).")      
            return_costume()
        
        if return_display==1:
            try: 
                days1=int(input("How many days did you rent the costume?"))
                no_of_costumes1=int(input("How many costumes are you returning?"))
              
            except:
                print("Please check your input(Only integers allowed).")
            if days1<=5:
                return_array[0][3]=str(int(return_array[0][3])+no_of_costumes1)
                print("Thank you for returning!!")
                file.write("%s %s" %("\nName of the costume : ",return_array[0][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[0][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes1))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input1=input("Enter Y for returning again and any keys for exiting:")
                if input1=="Y" :
                    return_=True
                else:
                    return_=False 
            else:
                return_array[0][3]=str(int(return_array[0][3])+no_of_costumes1)
                fine1=5*(days1-5)*no_of_costumes1
                total_fine=total_fine+fine1

                print("You have rented the costume for more than 5 days. So you will be fined")
                file.write("%s %s" %("\nName of the costume : ",return_array[0][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[0][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes1))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input1=input("Enter Y for returning again and any keys for exiting:")
                if input1=="Y" :
                    return_=True
                else:
                    return_=False 

        elif return_display==2:
            try: 
                days2=int(input("How many days did you rent the costume?"))
                no_of_costumes2=int(input("How many costumes are you returning?"))
              
            except:
                print("Please check your input(Only integers allowed).")
            if days2<=5:
                return_array[1][3]=str(int(return_array[1][3])+no_of_costumes2)
                print("Thank you for returning!!")
                file.write("%s %s" %("\nName of the costume : ",return_array[1][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[1][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes2))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input2=input("Enter Y for returning again and any keys for exiting:")
                if input2=="Y" :
                    return_=True
                else:
                    return_=False 
            else:
                return_array[1][3]=str(int(return_array[1][3])+no_of_costumes2)
                fine2=5*(days2-5)*no_of_costumes2
                total_fine=total_fine+fine2

                print("You have rented the costume for more than 5 days. So you will be fined")
                file.write("%s %s" %("\nName of the costume : ",return_array[1][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[1][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes2))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input2=input("Enter Y for returning again and any keys for exiting:")
                if input2=="Y" :
                    return_=True
                else:
                    return_=False  


        elif return_display==3:
            try: 
                days3=int(input("How many days did you rent the costume?"))
                no_of_costumes3=int(input("How many costumes are you returning?"))
              
            except:
                print("Please check your input(Only integers allowed).")
            if days3<=5:
                return_array[2][3]=str(int(return_array[2][3])+no_of_costumes3)
                print("Thank you for returning!!")
                file.write("%s %s" %("\nName of the costume : ",return_array[2][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[2][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes3))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input3=input("Enter Y for returning again and any keys for exiting:")
                if input3=="Y" :
                    return_=True
                else:
                    return_=False 
            else:
                return_array[2][3]=str(int(return_array[2][3])+no_of_costumes3)
                fine3=5*(days3-5)*no_of_costumes3
                total_fine=total_fine+fine3

                print("You have rented the costume for more than 5 days. So you will be fined")
                file.write("%s %s" %("\nName of the costume : ",return_array[2][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[2][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes3))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input3=input("Enter Y for returning again and any keys for exiting:")
                if input3=="Y" :
                    return_=True
                else:
                    return_=False    

        elif return_display==4:
            try: 
                days4=int(input("How many days did you rent the costume?"))
                no_of_costumes4=int(input("How many costumes are you returning?"))
              
            except:
                print("Please check your input(Only integers allowed).")
            if days4<=5:
                return_array[3][3]=str(int(return_array[3][3])+no_of_costumes4)
                print("Thank you for returning!!")
                file.write("%s %s" %("\nName of the costume : ",return_array[3][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[3][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes4))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input4=input("Enter Y for returning again and any keys for exiting:")
                if input4=="Y" :
                    return_=True
                else:
                    return_=False 
            else:
                return_array[3][3]=str(int(return_array[3][3])+no_of_costumes4)
                fine4=5*(days4-5)*no_of_costumes4
                total_fine=total_fine+fine4

                print("You have rented the costume for more than 5 days. So you will be fined")
                file.write("%s %s" %("\nName of the costume : ",return_array[3][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[3][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes4))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input4=input("Enter Y for returning again and any keys for exiting:")
                if input4=="Y" :
                    return_=True
                else:
                    return_=False

        elif return_display==5:
            try: 
                days5=int(input("How many days did you rent the costume?"))
                no_of_costumes5=int(input("How many costumes are you returning?"))
              
            except:
                print("Please check your input(Only integers allowed).")
            if days5<=5:
                return_array[4][3]=str(int(return_array[4][3])+no_of_costumes5)
                print("Thank you for returning!!")
                file.write("%s %s" %("\nName of the costume : ",return_array[4][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[4][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes5))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input5=input("Enter Y for returning again and any keys for exiting:")
                if input5=="Y" :
                    return_=True
                else:
                    return_=False 
            else:
                return_array[4][3]=str(int(return_array[4][3])+no_of_costumes5)
                fine5=5*(days5-5)*no_of_costumes5
                total_fine=total_fine+fine5

                print("You have rented the costume for more than 5 days. So you will be fined")
                file.write("%s %s" %("\nName of the costume : ",return_array[4][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[4][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes5))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input5=input("Enter Y for returning again and any keys for exiting:")
                if input5=="Y" :
                    return_=True
                else:
                    return_=False 

        elif return_display==6:
            try: 
                days6=int(input("How many days did you rent the costume?"))
                no_of_costumes6=int(input("How many costumes are you returning?"))
              
            except:
                print("Please check your input(Only integers allowed).")
            if days6<=5:
                return_array[5][3]=str(int(return_array[5][3])+no_of_costumes6)
                print("Thank you for returning!!")
                file.write("%s %s" %("\nName of the costume : ",return_array[5][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[5][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes6))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input6=input("Enter Y for returning again and any keys for exiting:")
                if input6=="Y" :
                    return_=True
                else:
                    return_=False 
            else:
                return_array[5][3]=str(int(return_array[5][3])+no_of_costumes6)
                fine6=5*(days6-5)*no_of_costumes6
                total_fine=total_fine+fine6

                print("You have rented the costume for more than 5 days. So you will be fined")
                file.write("%s %s" %("\nName of the costume : ",return_array[5][0]))
                file.write("%s %s" %("\nName of the brand : ",return_array[5][1]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes6))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input6=input("Enter Y for returning again and any keys for exiting:")
                if input6=="Y" :
                    return_=True
                else:
                    return_=False                                                           
        else:
            print("Please enter valid serial numbers")

    if total_fine==0:
        file.write("%s %s\n"%("\n\nTotal fine : $",0,))
    else:
        file.write("%s %s\n"%("\n\nTotal fine : $",total_fine))


    file.close()
    fileNAME=f"Returned by {name}.txt"
    with open(fileNAME,"r")as x:
        a=x.read()
        print(a)    
          
    
    file=open("data.txt","w") # here "w" reperesnts the write function
    for x in return_array:
         line=','.join(x)
         file.write(line)
         file.write("\n")  

return_costume()
                    
    
      
    


