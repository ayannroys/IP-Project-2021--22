import os
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.indexes.base import Index
from datetime import date, timedelta 

def clear(): 
    os.system('cls')

CountrieShipping = pd.read_csv(r"C:\Users\ayann\Desktop\Assingment\Countriesandshipping.csv" )
Packages = pd.read_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv")
Deals = pd.read_csv(r"C:\Users\ayann\Desktop\Assingment\Deals.csv")

#Extreme beta probably will not be included in the final product
Date_Data = pd.read_csv(r"C:\Users\ayann\Desktop\Assingment\Date.csv")

ans  = 1 
while ans  == True :
    print("""
    ----------------------------------------------------------------------------------------
    ██████████████████████████████████████████████               ESTB. - 1969
    █░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░█████████           (NOT FOR PUBLIC EYES)
    █░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████     Where there’s a will, DHL is the way
    █░░▄▀░░░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████           
    █░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████                  
    █░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████                  Alert:
    █░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████  
    █░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████     Due to COVID-19 Shipping to some 
    █░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████       countries has been temporarly 
    █░░▄▀░░░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█                suspended.   
    █░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
    █░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░░░░░░░░░█      !help - For help with commands
    ██████████████████████████████████████████████
    ----------------------------------------------------------------------------------------

    -----------------  ---------------   --------------  -------------  ------------ 
    |   Customer    |  |   Staff     |   |  Analyst   |  |   Cancel  |  |  About   |
    |    Portal     |  |   Portal    |   |   Portal   |  |   Package |  |    us    |
    |   (Press 1)   |  |  (Press 2)  |   |( Press 3 ) |  | (Press 4) |  | (Press 5)|
    -----------------  ---------------   --------------  -------------  ------------          """)

    portal_selection = int(input("Please Chose the Portal you want to log into ===> "))
    clear()


    #CUSTOMER PORTAL CODE
    customer  = 1
    while customer == True:
        if portal_selection == 1:
            print("""
            ----------------------------------------------------------------------------------------
            ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
            ░█ ░█ ░█▀▀█ ░█                      CLOSER
            ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
            ----------------------------------------------------------------------------------------
            
             --------------------  -----------------  -------------  ---------------  ---------------  
             |     SHIP NOW     |  |     TRACK     |  |   DEALS   |  |  COUNTRIES  |  |    BACK     |
             |     (PRESS 1)    |  |   (PRESS 2)   |  | (PRESS 3) |  | WE DELIEVER |  |   <-----    |
             |                  |  |               |  |           |  |  (PRESS 4)  |  |  (PRESS 5)  |
             --------------------  -----------------  -------------  ---------------  ---------------""")
            customer_portal1 = int(input("Please Chose the Services you require --> "))
            clear()
            if customer_portal1 == 1:
                print("""
                -------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█                     
                ░█ ░█ ░█▀▀█ ░█ 
                ░█▄▄▀ ░█ ░█ ░█▄▄█
                -------------------------------------------------------------------------------------
                PLEASE ENTER THE ITEM YOU WILL BE SHIPPING
                --> Documents                          
                --> Heavy Good 
                --> Container 
                --> Others """)
                cargo = input("Write here and press enter --> ")

                print("PLEASE ENTER THE FOLLOWING DETAILS : ")
                Weight = int(input("Please Enter the Weight (Kg) of the cargo : "))
                Length = int(input("Please Enter the Length of the cargo : "))
                Height = int(input("Please Enter the Height of the cargo : "))

                clear()

                print("Thank you. Please Press Enter: ")
                input()

                clear()                

                print("""
                -------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█ 
                ░█ ░█ ░█▀▀█ ░█ 
                ░█▄▄▀ ░█ ░█ ░█▄▄█
                -------------------------------------------------------------------------------------""")

                Sender_Country = input("Enter the senders Country: ")
                Sender_Name = input("Enter sender name: ")
                Sender_Adress = input("Please enter sender's adress : ")
                Phone_No = input("Please enter your phone number : ")
                Reciever_Name = input("Enter Reciever Name: ")
                Reciever_Country = input("Please Enter the reciever's Country: ")
                Reciever_Adress = input("Please neter reciever adress : ")
                Item = input("Please enter what is inside the package : ")
                Quantity = input("Please enter the quantity of the item : ")
                package_id = random.randint(0,900)
                a = int(input("WHAT SERVICE TYPE DO YOU REQUIRE : 1) EXPRESS 2) REGULAR"))
                if a == 1:
                    transport = "Flight"
                elif a == 2:
                    transport = "Ship"


                print("""
                -------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█ 
                ░█ ░█ ░█▀▀█ ░█ 
                ░█▄▄▀ ░█ ░█ ░█▄▄█
                -------------------------------------------------------------------------------------
                YOUR PACKAGE WILL BE DELEVERED SUCESFULLY !! YOUR ORDER ID IS : """ , package_id)

                Extra_Detail = {"ID":[package_id],"Package":[Item],"Weight":[Weight],"Length":[Length],"Height":[Height],"Cargo":[cargo],"Sender_Adress":[Sender_Adress],"Reciever_Adress":[Reciever_Adress],"Reciever Name":[Reciever_Name]}
                df = pd.DataFrame(Extra_Detail)
                df.to_csv(r"C:\Users\ayann\Desktop\Assingment\Manifest.csv" , header= False , mode = 'a')

                
                item = {"ID":[package_id],"Package":[Item],"Sender_Name":[Sender_Name],"Destination":[Reciever_Country],"Status":["On time"],"Shipping":[transport]}
                df = pd.DataFrame(item)
                df.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv" , header= False , mode = 'a')

                #BETA
                Refund = {"ID":[package_id],"Package_Type":[cargo],"Sended_Date":[date.today()],"Expected_Date":[date.today()+timedelta(days = 7)]}
                a = pd.DataFrame(Refund)
                a.to_csv(r"C:\Users\ayann\Desktop\Assingment\Date.csv",header = False, mode = 'a')
        
            elif customer_portal1 == 2:
                print("""
                ----------------------------------------------------------------------------------------
                ░█▀▀▄ ░█░ █ ░█
                ░█ ░█ ░█▀▀█ ░█                         TRACKING AND KEEPING YOUR PARCEL
                ░█▄▄▀ ░█ ░█ ░█▄▄█                                SAFE 24/7
                ----------------------------------------------------------------------------------------
                 """)

                id = int(input("Enter your delivery code : "))
                print(Packages.loc[Packages['ID']==id])
                input()
                clear()

            elif customer_portal1 == 3:
                print("""
                ----------------------------------------------------------------------------------------
                ░█▀▀▄ ░█░ █ ░█
                ░█ ░█ ░█▀▀█ ░█ 
                ░█▄▄▀ ░█ ░█ ░█▄▄█
                ----------------------------------------------------------------------------------------
                 """)
                print("THSESE ARE THE CURRENT OFFERS AVAILABLE")
                print(Deals)
                a = input() 
                clear()

            elif customer_portal1 == 4:
                print("""
                ----------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█                EVER EXPANDING                                         
                ░█ ░█ ░█▀▀█ ░█                      AND            
                ░█▄▄▀ ░█ ░█ ░█▄▄█                 GROWING           
                ----------------------------------------------------------------------------------------
                
                THE FOLLOWING ARE THE LSIT OF COUNTRIES WE ARE CURRENTLY OPERATING IN - """)

                print(CountrieShipping)

                print("NOTE : DEAR CUSTOMER, IF THE SERVICE TO COUNTRY WHICH YOU HAVE CHOSEN IS DISABLED THEN THE ITEM MAYBE PUT ON HOLD UNTIL THE SERVICE IS RESUMED OR MAY BE RETURNED BACK TO YOU")
                A = input("PRESS ENTER")
                clear()

            elif customer_portal1 == 5:
                print("""
                ----------------------------------------------------------------------------------------
                ░█▀▀▄ ░█░ █ ░█
                ░█ ░█ ░█▀▀█ ░█ 
                ░█▄▄▀ ░█ ░█ ░█▄▄█
                ----------------------------------------------------------------------------------------
                 """)
                print("LOADING.....")
                clear()
                customer = 0
                 
        elif portal_selection == 2:
            print("""
            ----------------------------------------------------------------------------------------
            ░█▀▀▄ ░█ ░█ ░█                                                             
            ░█ ░█ ░█▀▀█ ░█                      CHANGING THE WORLD AS A WHOLE 
            ░█▄▄▀ ░█ ░█ ░█▄▄█                   
            ----------------------------------------------------------------------------------------""")
            
            a = int(input("PLEASE ENTER YOUR EMPLOYEE ACESS CODE : "))
            if a == 0000 :
                print("Acess Granted")
                input("PRESS ENTER")

                clear()
                
                print("""
                ----------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█                                                       
                ░█ ░█ ░█▀▀█ ░█                  CHANGING THE WORLD AS A WHOLE    
                ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                ----------------------------------------------------------------------------------------
                1) SHOW ALL PACKAGES 
                2) CHANGE ORDERS
                3) ADD PACKAGE MANUALLY
                4) MODIFY DEALS 
                5) CHANGE COUNTRY STATUS""")

                employee_ans = int(input("ENTER YOUR OPTION : "))

                if employee_ans == 1:
                    print(Packages)
                    input()

                elif employee_ans == 2: 
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                                                       
                    ░█ ░█ ░█▀▀█ ░█                  CHANGING THE WORLD AS A WHOLE    
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                    ----------------------------------------------------------------------------------------
                    1) CHANGE ORDER ID
                    2) PACKAGE
                    3) SENDER NAME
                    4) DESTINATION
                    5) STATUS
                    6) CHANGE TRANSPORT""")


                    a = int(input("PLEASE ENTER YOUR OPTION : "))
                

                    clear()

                    if a == 1:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        print(Packages)
                        old_id = int(input("PLEASE ENTER THE INDEX OF THE PACKAGE YOU WANT TO CHANGE : "))
                        new_id = int(input("PLEASE ENTER THE NEW ORDER ID : "))
                        Packages.loc[old_id,'ID'] = new_id
                        Packages.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv" , )
                        input()


                    elif a == 2:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        print(Packages)
                        old_Package = int(input("PLEASE ENTER THE INDEX OF THE PACKAGE YOU WANT TO CHANGE : "))
                        new_Package = input("PLEASE ENTER THE NEW PACKAGE : ")
                        Packages.loc[old_Package,'Package'] = new_Package
                        Packages.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv" )
                        input()

                    elif a == 3:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        print(Packages)
                        old_Name = int(input("PLEASE ENTER THE INDEX OF THE PACKAGE YOU WANT TO CHANGE : "))
                        new_Package = input("PLEASE ENTER THE NEW NAME : ")
                        Packages.loc[old_Name,'Sender_Name'] = new_Package
                        Packages.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv" )
                        input()

                    elif a == 4:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        print(Packages)
                        old_Destination = int(input("PLEASE ENTER THE INDEX OF THE PACKAGE YOU WANT TO CHANGE : "))
                        new_Destination = input("PLEASE ENTER THE NEW DESTINATION : ")
                        Packages.loc[old_Destination,'Destination'] = new_Destination
                        Packages.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv")
                        input()

                    elif a == 5:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        print(Packages)
                        old_Status = int(input("PLEASE ENTER THE INDEX OF THE PACKAGE YOU WANT TO CHANGE : "))
                        new_Status = input("PLEASE ENTER THE NEW STATUS : ")
                        Packages.loc[old_Status,'Status'] = new_Status
                        Packages.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv" )
                        input()
                    
                    elif a == 6:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        print(Packages)
                        old_Transport = int(input("PLEASE ENTER THE INDEX OF THE PACKAGE YOU WANT TO CHANGE : "))
                        new_Transport = input("PLEASE ENTER THE NEW DESTINATION : ")
                        Packages.loc[old_Transport,'Shipping'] = new_Transport
                        Packages.to_csv(r"C:\Users\ayann\Desktop\Assingment\Packages.csv" )
                        input()
                    
                    elif a == 7:
                        customer = 0


                elif employee_ans == 3: 
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                                                          
                    ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                    ----------------------------------------------------------------------------------------""")

                    clear()

                elif employee_ans == 4:
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                                                          
                    ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                    ----------------------------------------------------------------------------------------
                    1) ADD A DEAL
                    2) REMOVE A DEAL """)

                    A = int(input("SELECT AN OPTION: "))

                    clear() 

                    if A == 1:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        b = input("PLEASE ENTER DEAL : ")
                        c = input("ENTER THE DISCOUNT : ")
                        deal = {"DEAL": [b] , "DISCOUNT": [c]}
                        df = pd.DataFrame(deal)
                        df.to_csv(r"C:\Users\ayann\Desktop\Assingment\Deals.csv"  , mode = 'a' , header= False )
                
                    elif A == 2:
                        print("""
                        ----------------------------------------------------------------------------------------
                        ░█▀▀▄ ░█ ░█ ░█                                                          
                        ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                        ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                        ----------------------------------------------------------------------------------------""")
                        b = input("PLEASE ENTER DEAL : ")
                        TIME = int(input("ENTER THE DEAL YOU WANT TO REMOVE: "))
                        df = pd.DataFrame(Deals.drop(index = TIME))
                        df.to_csv(r"C:\Users\ayann\Desktop\Assingment\Deals.csv")

                    
                
                elif employee_ans == 5:
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                                                          
                    ░█ ░█ ░█▀▀█ ░█                   CHANGING THE WORLD AS A WHOLE    
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   
                    ----------------------------------------------------------------------------------------""")
                    print(CountrieShipping)
                    country = int(input("Please select the country index you want to change the status of : "))
                    status = input("Enter the new status of the country: ")
                    CountrieShipping.loc[country,"Service"] = status

                    CountrieShipping.to_csv(r"C:\Users\ayann\Desktop\Assingment\Countriesandshipping.csv")
                clear()
            else :
                print("Try again")
                customer = 0
            clear()
            customer = 0
        
        elif portal_selection == 3:
            print("""
            ----------------------------------------------------------------------------------------
            ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
            ░█ ░█ ░█▀▀█ ░█                      CLOSER
            ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
            ----------------------------------------------------------------------------------------""")
            analysis_code = int(input("Enter the Imperial Code: "))
            if analysis_code == 6666:
                print("Acesss Granted")
                clear()
                print("""
                ----------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
                ░█ ░█ ░█▀▀█ ░█                      CLOSER
                ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
                ----------------------------------------------------------------------------------------
                
                PLEASE SELECT THE ITEM YOU WANT TO COMPARE: 
                
                1) TRANSPORT
                2) COUNTRIES
                3) DELAY AND ON TIME PACKAGES
                4) COUNTRY STATUS""")

                analysis_option = int(input("PLEASE ENTER THE OPTION: "))

                if analysis_option == 1:
                    Transport_Data = [Packages.Shipping.value_counts().Flight,Packages.Shipping.value_counts().Ship]
                    TransportName_Data = ["Flight","Ship"]
                    plt.bar(TransportName_Data,Transport_Data)
                    plt.xlabel("TransportNmae_Data")
                    plt.ylabel("Transport_Data")
                    plt.show()
                    input()
                
                elif analysis_option == 2:
                    clear()
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
                    ░█ ░█ ░█▀▀█ ░█                      CLOSER
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
                    ----------------------------------------------------------------------------------------""")
                    countries_no = int(input("PLEASE ENTER THE NO. OF COUNTRIES YOU WANT TO COMPARE (RECOMMENED 3) : "))
                    list = []
                    data = []
                    
                    for i in range(0,countries_no): 
                        a = input("ENTER THE COUNTRY: ")
                        b = Packages.Destination.value_counts()[a]
                        list.append(a)
                        data.append(b)
                        
                    clear()
                    
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
                    ░█ ░█ ░█▀▀█ ░█                      CLOSER
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
                    ----------------------------------------------------------------------------------------
                    1) BAR GRAPH
                    2) PIE CHART""")

                    graph_type = int(input("SELECT GRAPH TYPE: "))

                    if graph_type == 1:
                        
                        plt.bar(list,data)
                        plt.xlabel("COUNTRY")
                        plt.ylabel("PARCELS")
                        plt.show()

                    elif graph_type == 2: 
                        plt.title("COMAPRISON")
                        plt.pie(data,labels = list)
                        plt.show()

                    input()
                
                elif analysis_option == 3:
                    clear()
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
                    ░█ ░█ ░█▀▀█ ░█                      CLOSER
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
                    ----------------------------------------------------------------------------------------
                    1) BAR GRAPH
                    2) PIE CHART""")
                    
                    GRAPH_TYPE = int(input("PLEASE SELECT THE GRAPH TYPE YOU NEED: "))
                    Status = []
                    Status_Data = []
                    no = int(input("HOW MANY STATUS DO YOU WANT TO COMPARE ? (MAX 4)"))
                    for i in range (0,no):
                        a = input("ENTER THE STATUS: ")
                        b = Packages.Status.value_counts()[a]
                        Status.append(a)
                        Status_Data.append(b)
                        

                    if GRAPH_TYPE == 1:
                        plt.bar(Status,Status_Data)
                        plt.xlabel("Status")
                        plt.ylabel("Packages")
                        plt.show()

                    elif GRAPH_TYPE == 2:
                        plt.title("DATA")
                        plt.pie(Status_Data,labels = Status)
                        plt.show()

                elif analysis_option == 4: 
                    print("""
                    ----------------------------------------------------------------------------------------
                    ░█▀▀▄ ░█ ░█ ░█                BRINGING THE WORLD                                        
                    ░█ ░█ ░█▀▀█ ░█                      CLOSER
                    ░█▄▄▀ ░█ ░█ ░█▄▄█                   TO YOU
                    ----------------------------------------------------------------------------------------""")

                    clear()

            customer = 0

        elif portal_selection == 4:
            print("""
            ----------------------------------------------------------------------------------------
            ░█▀▀▄ ░█ ░█ ░█                                                      
            ░█ ░█ ░█▀▀█ ░█                   (PLEASE DO NOT SELECT ANY OF THE BELOW OPTIONS)      
            ░█▄▄▀ ░█ ░█ ░█▄▄█                     THIS PORTAL IS USED TO ERASE ALL DATA
            ----------------------------------------------------------------------------------------
            1) PACKAGES
            2) DATE
            3) MANIFEST""")

            #PLEASE IGNORE THE SLOPPY CODING. WE HAD TIME CONSTRAINS

            developer = int(input("PLEASE ENTER YOUR OPTION : "))

            if developer == 1: 
                Packages.pop("ID")
                Packages.pop("Package")
                Packages.pop("Sender_Name")
                Packages.pop("Destination")
                Packages.pop("Status")
                Packages.pop("Shipping")
                Packages.to_csv(r'C:\Users\ayann\Desktop\Assingment\Packages.csv')

            elif developer == 2:
                Packages.pop("ID")
                Packages.pop("Package_Type")
                Packages.pop("Sender_Date")
                Packages.pop("Expected_Date")
                Packages.to_csv(r'C:\Users\ayann\Desktop\Assingment\Packages.csv')

            elif developer == 3: 
                Packages.pop("ID")
                Packages.pop("Weight")
                Packages.pop("Length")
                Packages.pop("Height")
                Packages.pop("Cargo")
                Packages.pop("Sender_Adress")
                Packages.pop("Reciever_Adress")
                Packages.pop("Reciever Name")
                Packages.to_csv(r'C:\Users\ayann\Desktop\Assingment\Packages.csv')



            input()
            clear()
            customer = 0

        elif portal_selection == 5:
            print("""
                ----------------------------------------------------------------------------------------------------------
                ░█▀▀▄ ░█ ░█ ░█                            DEVELOPED BY       -            WE BELIVE IN QUALITY                                  
                ░█ ░█ ░█▀▀█ ░█                            ARD STUDIOS                             NOT
                ░█▄▄▀ ░█ ░█ ░█▄▄█                                                              QUANTITIY
                ----------------------------------------------------------------------------------------------------------
                __745___ 595656__ 56758___                                A - AYAN ROY
                _42_47__ 32___84_ 46__78__                                R - ROHIT SHETTI
                94___84_ 25___76_ 65___88_                                D - DEV ATHA
                2894655_ 383256__ 37___65_                  (WE WOULD LIKE TO THANK EVERYONE WHO SUPPORTED US)
                92___28_ 79___62_ 56__29__
                93___74_ 83___86_ 87895___    THIS SOFTWARE WAS DEVELOPED BY AND IS A INTELECTUAL PROPERTY OF ARD STUDIOS""")
             
            input("PRESS ENTER")
            customer  = 0 
            clear()
                
        
        else :
            exit() 
