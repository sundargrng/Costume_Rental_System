import sys
from display import text_to_array

def rent_costume():
    rent_='''
██████╗░███████╗███╗░░██╗████████╗
██╔══██╗██╔════╝████╗░██║╚══██╔══╝
██████╔╝█████╗░░██╔██╗██║░░░██║░░░
██╔══██╗██╔══╝░░██║╚████║░░░██║░░░
██║░░██║███████╗██║░╚███║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░'''

    print(rent_,"\n")
    name=input("Enter your name: ")
    address=input("Enter your address: ")
    contact=input("Enter your contact number: ")
    file=open("%s %s.txt" % ("Rented by", name),"w")# creates the file 
    file.write("%s %s" % ("Customer Name: ", name)) # writes the name of customer 
    file.write("%s %s" % ("\nCustomer Address: ", address)) # writes the address of customer
    file.write("%s %s" % ("\nCustomer contact: ", contact))# writes the contact of customer

    from datetime import datetime
    now=datetime.now()
    dateandtime=now.strftime("%d/%m/%Y %H:%m:%S")
    file.write("%s %s" % ("\n\nBorrowed: ", dateandtime))# writes the current date and time in the file
    file.write("\n\nBorrow Details: ")
    file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                  
    rent_array=text_to_array()
    grandTotal=0
    rent=True
    while rent==True:
        try:
            rent_display= int(input(''' Enter the number of costume for renting
              1: Cop Costume Set
              2: Formal Suite (Black Premium)
              3: Fairy Costume Full Set
              4: Full Metal Alchemist Set
              5: Black-Buttler (Sebastian)
              6: Jotaro Kujo (Exclusive)\n
              Enter : '''))
        except:
            print("Please check your input(Only integers allowed).")      
            rent_costume()

        if rent_display==1:
            try: 
                no_of_costumes1=int(input("How many costumes do you want to rent?"))
            except:
                print("Please check your input(Only integers allowed).")
            if no_of_costumes1>int(rent_array[0][3]):
                print("Sorry, only ",rent_array[0][3], " costumes are available")
                input1=input("Enter Y for renting again and any keys for exiting:")
                if input1=="Y":
                   rent_costume()
                else: 
                   sys.exit()
                

            elif no_of_costumes1<int(rent_array[0][3]):
                amount1=no_of_costumes1*15
                grandTotal= grandTotal+ amount1
                remaining1=int(rent_array[0][3])-no_of_costumes1
                rent_array[0][3]=str(remaining1)

                print("Thank you for renting!!")
                file.write("%s %s" %("\nName of the costume : ",rent_array[0][0]))
                file.write("%s %s" %("\nName of the brand : ",rent_array[0][1]))
                file.write("%s %s" %("\nPrice for 5 days: ",rent_array[0][2]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes1))
                file.write("%s %d" %("\n\nTotalAmount : $",amount1))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input1=input("Enter Y for renting again and any keys for exiting:")
                if input1=="Y" :
                    rent=True
                else:
                    rent=False        


        elif rent_display==2:
            try: 
                no_of_costumes2=int(input("How many costumes do you want to rent?"))
            except:
                print("Please check your input(Only integers allowed).")
            if no_of_costumes2>int(rent_array[1][3]):
                print("Sorry, only ",rent_array[1][3], " costumes are available")
                input2=input("Enter Y for renting again and any keys for exiting:")
                if input2=="Y":
                   rent_costume()
                else: 
                   sys.exit()
                

            elif no_of_costumes2<int(rent_array[1][3]):
                amount2=no_of_costumes2*14.5
                grandTotal= grandTotal+ amount2  
                remaining2=int(rent_array[1][3])-no_of_costumes2
                rent_array[1][3]=str(remaining2)

                print("Thank you for renting!!")
                file.write("%s %s" %("\nName of the costume : ",rent_array[1][0]))
                file.write("%s %s" %("\nName of the brand : ",rent_array[1][1]))
                file.write("%s %s" %("\nPrice for 5 days: ",rent_array[1][2]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes2))
                file.write("%s %d" %("\n\nTotalAmount : $",amount2))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input2=input("Enter Y for renting again and any keys for exiting:")
                if input2=="Y" :
                    rent=True
                else:
                    rent=False


        elif rent_display==3:
            try: 
                no_of_costumes3=int(input("How many costumes do you want to rent?"))
            except:
                print("Please check your input(Only integers allowed).")
            if no_of_costumes3>int(rent_array[2][3]):
                print("Sorry, only ",rent_array[2][3], " costumes are available")
                input3=input("Enter Y for renting again and any keys for exiting:")
                if input3=="Y":
                   rent_costume()
                else: 
                   sys.exit()
                

            elif no_of_costumes3<int(rent_array[2][3]):
                amount3=no_of_costumes3*20
                grandTotal= grandTotal+ amount3  
                remaining3=int(rent_array[1][3])-no_of_costumes3
                rent_array[2][3]=str(remaining3)

                print("Thank you for renting!!")
                file.write("%s %s" %("\nName of the costume : ",rent_array[2][0]))
                file.write("%s %s" %("\nName of the brand : ",rent_array[2][1]))
                file.write("%s %s" %("\nPrice for 5 days: ",rent_array[2][2]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes3))
                file.write("%s %d" %("\n\nTotalAmount : $",amount3))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input3=input("Enter Y for renting again and any keys for exiting:")
                if input3=="Y" :
                    rent=True
                else:
                    rent=False    

        elif rent_display==4:
            try: 
                no_of_costumes4=int(input("How many costumes do you want to rent?"))
            except:
                print("Please check your input(Only integers allowed).")
            if no_of_costumes4>int(rent_array[3][3]):
                print("Sorry, only ",rent_array[3][3], " costumes are available")
                input4=input("Enter Y for renting again and any keys for exiting:")
                if input4=="Y":
                   rent_costume()
                else: 
                   sys.exit()
                

            elif no_of_costumes4<int(rent_array[3][3]):
                amount4=no_of_costumes4*37
                grandTotal= grandTotal+ amount4  
                remaining4=int(rent_array[1][3])-no_of_costumes4
                rent_array[3][3]=str(remaining4)

                print("Thank you for renting!!")
                file.write("%s %s" %("\nName of the costume : ",rent_array[3][0]))
                file.write("%s %s" %("\nName of the brand : ",rent_array[3][1]))
                file.write("%s %s" %("\nPrice for 5 days: ",rent_array[3][2]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes4))
                file.write("%s %d" %("\n\nTotalAmount : $",amount4))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input4=input("Enter Y for renting again and any keys for exiting:")
                if input4=="Y" :
                    rent=True
                else:
                    rent=False  

        elif rent_display==5:
            try: 
                no_of_costumes5=int(input("How many costumes do you want to rent?"))
            except:
                print("Please check your input(Only integers allowed).")
            if no_of_costumes5>int(rent_array[4][3]):
                print("Sorry, only ",rent_array[4][3], " costumes are available")
                input5=input("Enter Y for renting again and any keys for exiting:")
                if input5=="Y":
                   rent_costume()
                else: 
                   sys.exit()
                

            elif no_of_costumes5<int(rent_array[4][3]):
                amount5=no_of_costumes5*50
                grandTotal= grandTotal+ amount5  
                remaining5=int(rent_array[1][3])-no_of_costumes5
                rent_array[4][3]=str(remaining5)

                print("Thank you for renting!!")
                file.write("%s %s" %("\nName of the costume : ",rent_array[4][0]))
                file.write("%s %s" %("\nName of the brand : ",rent_array[4][1]))
                file.write("%s %s" %("\nPrice for 5 days: ",rent_array[4][2]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes5))
                file.write("%s %d" %("\n\nTotalAmount : $",amount5))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input5=input("Enter Y for renting again and any keys for exiting:")
                if input5=="Y" :
                    rent=True
                else:
                    rent=False  

        elif rent_display==6:
            try: 
                no_of_costumes6=int(input("How many costumes do you want to rent?"))
            except:
                print("Please check your input(Only integers allowed).")
            if no_of_costumes6>int(rent_array[5][3]):
                print("Sorry, only ",rent_array[5][3], " costumes are available")
                input6=input("Enter Y for renting again and any keys for exiting:")
                if input6=="Y":
                   rent_costume()
                else: 
                   sys.exit()
                

            elif no_of_costumes6<int(rent_array[5][3]):
                amount6=no_of_costumes6*30
                grandTotal= grandTotal+ amount6  
                remaining6=int(rent_array[1][3])-no_of_costumes1
                rent_array[5][3]=str(remaining6)

                print("Thank you for renting!!")
                file.write("%s %s" %("\nName of the costume : ",rent_array[5][0]))
                file.write("%s %s" %("\nName of the brand : ",rent_array[5][1]))
                file.write("%s %s" %("\nPrice for 5 days: ",rent_array[5][2]))
                file.write("%s %d" %("\nQuantity: ",no_of_costumes6))
                file.write("%s %d" %("\n\nTotalAmount : $",amount6))
                file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                input6=input("Enter Y for renting again and any keys for exiting:")
                if input6=="Y" :
                    rent=True
                else:
                    rent=False    
            
        else:
            print("Please enter valid serial number")
    file.write("%s %5.1f %s\n"%("\n\nGrand Total :",grandTotal,"dollars"))
    file.close()
    fileNAME=f"Rented by {name}.txt"
    with open(fileNAME,"r")as x:
        a=x.read()
        print(a)
    



    
    file=open("data.txt","w") # here "w" reperesnts the write function
    for x in rent_array:
         line=','.join(x)
         file.write(line)
         file.write("\n")      


rent_costume()


            
              
            


            
