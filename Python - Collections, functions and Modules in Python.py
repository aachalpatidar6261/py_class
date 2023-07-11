import datetime
d = {}

print("\n",25*" ","WELCOME TO FRUITS MARKET\n")

print(26*" ","1) Manager.")
print(26*" ","2) Customer.")

def stock():
    print("\n",25*" ","FRUITS MARKET MANAGER\n")
    print(25*" ","1) ADD FRUIT STOCK.")
    print(25*" ","2) VIEW FRUIT STOCK.")
    print(25*" ","3) UPDATE FRUIT STOCK.")

choice = int(input("\nSelect Your Role : "))
   
if choice==1:
    stock()
    
while True:
        
        ch = int(input("\nEnter Your Choice : "))
        if ch == 1:
            print("\nADD FRUIT STOCK")
            
            
            def log_transaction(add, qty, price):  # add is fruits
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp}: {add}: {qty, price}\n"

                with open('transaction_log.txt', 'a') as file:
                    file.write(log_entry)

            # Function to view all transaction logs
            def view_transaction_logs():
                try:
                    with open('transaction_log.txt') as file:
                        print("Transaction Logs:")
                        print(file.read())
                except FileNotFoundError:
                    print("No transaction logs found.")
                    
            add = input("Enter Fruits Name : ")
            qty = int(input("Enter qty (in kg) : "))
            price = int(input("Enter Price : "))
            log_transaction(add,qty,price)
            view_transaction_logs()
            
            
            d[add]={"qty":qty,"price":price}
            dicti=d
            
            do = input("\nDo you want to perform more operation : Press y for YES or Press n for NO : ")

            if do == "y":
                 stock()
            
            
            elif do == "n":
                 print("\n",25*" ","THANK YOU !, HAVE A NICE DAY..\n")
                 break
            elif do!=y or do!=n:
                        print("sorry !, not accepted.")

                    
        
        elif ch ==2 :
                    print(dicti)
                    do = input("\nDo you want to perform more operation : Press y for YES or Press n for NO : ")

                    if do == "y":
                         stock()
                
                    elif do == "n":
                         print("\n",25*" ","THANK YOU !, HAVE A NICE DAY..\n")
                         break
                    elif do!=y or do!=n:
                        print("sorry !, not accepted.")
            
                    
            
        elif ch ==3 :
               up_fr= input("Enter Fruits Name : ")

               if up_fr in dicti:
                     qty = int(input("Enter qty (in kg) : "))
                     price = int(input("Enter Price : "))
                     d[up_fr]={"qty":qty,"price":price}
                     print(d)
               else : 
                     print("Sorry,Fruit is not present in stock. ")

               do = input("\nDo you want to perform more operation : Press y for YES or Press n for NO : ")

               if do == "y":
                    stock()
            
               elif do == "n":
                     print("\n",25*" ","THANK YOU !, HAVE A NICE DAY..\n")
                     break





    
        

