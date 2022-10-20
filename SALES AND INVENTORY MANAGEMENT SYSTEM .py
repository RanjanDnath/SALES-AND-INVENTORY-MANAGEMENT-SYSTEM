import mysql.connector
print("""
                                                          _______________________________________________________________
                                  ********************<---------- WELCOME TO SALES AND INVENTORY MANAGEMENT SYSTEM ---------->********************
                                                          _______________________________________________________________
""")
mydb=mysql.connector.connect(host="localhost",user="root",password="A#@01wrft45")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists sales")
mycursor.execute("use sales")
mycursor.execute("create table if not exists login(username varchar(25)not null, password varchar(25)not null)")
mycursor.execute("create table if not exists purchase(odate date not null, name varchar(25)not null, pcode int not null,amount int not null)")
mycursor.execute("create table if not exists stock(pcode int not null, pname varchar(25)not null, quantity int not null, price int not null)")
mydb.commit()
z=0
mycursor.execute("select*from login")
for i in mycursor:
    z+=1

if(z==0):
    mycursor.execute("insert into login values('username','ng')")
    mydb.commit()
while True:
    print("""
1.Admin
2.Customer
3.Exit
""")
    
###################################################ADMIN SECTION##############################################################
    ch=int(input("Enter your choice:"))
    if(ch==1):
        passs=input("Enter password:")
        mycursor.execute("select*from login")
        for i in mycursor:
            username,password=i
        if(passs==password):
            print("welcome>>>>>")
            loop2='y'
            while(loop2=='y'or loop2=='Y'):
                print("""
                                                                      ________________________________
                                                                >>>>>>>>>> WELCOME TO ADMIN SECTION >>>>>>>>>>
                                                                      ________________________________
    1.Add New Iteam
    2.Updating price
    3.deleting Iteams
    4.Display All Iteams
    5.To change the password
    6.Log Out
    """)
                ch=int(input("Enter your choice:"))
                if(ch==1):
                    loop='y'
                    while(loop=='y'or loop=='Y'):
                        pcode=int(input("Enter product code:"))
                        pname=input("Enter product name:")
                        quantity=int(input("Enter product quantity:"))
                        price=int(input("Enter product price:"))
                        mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit()
                        print("Record inserted successfully...")
                        loop=input("Do you want to enter more iteams(y/n): ")
                    loop2=input("Do you want to continue editing stock(y/n): ")

                elif(ch==2):
                    loop='y'
                    while(loop=='y'or loop=='Y'):
                        pcode=int(input("Enter product code:"))
                        new_price=int(input("Enter product new price:"))
                        mycursor.execute("update stock set price='"+str(new_price)+"' where pcode='"+str(pcode)+"'")
                        mydb.commit()
                        print("Record updated successfully...")
                        loop=input("Do you want to change of any other iteam(y/n): ")
                    loop2=input("Do you want to continue editing stock(y/n):  ")
                               
                elif(ch==3):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        pcode=int(input("Enter product code:"))
                        mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                        mydb.commit()
                        print("Record deleted successfully...")
                        loop=input("Do you want to delete any other data(y/n): ")
                    loop2=input("Do you want to continue editing stock(y/n):  ")

                elif(ch==4):
                    mycursor.execute("select*from stock")
                    print("pcode || pname || quantity || price" )
                    for i in mycursor:
                        t_code,t_name,t_quantity,t_price=i
                        print(f" {t_code} || {t_name} || {t_quantity} || {t_price}")

                elif(ch==5):
                    old_passs=input("Enter old password: ")
                    mycursor.execute("select*from login")
                    for i in mycursor:
                        username,password=i
                    if(old_passs==password):
                        new_passs=input("Enter new password: ")
                        mycursor.execute("update login set password='"+new_passs+"'")
                        mydb.commit()
                        print("password updated successfully...")

                elif(ch==6):
                    print("Log Out successfully...")
                    break
        else:
            print("wrong password")
            
################################################CUSTOMER SECTION##############################################################

    elif(ch==2):
        print("""
                                                                     ____________________________________
                                                                >>>>>>>>>> WELCOME TO CUSTOMER SECTION >>>>>>>>>>
                                                                      ____________________________________
1.Iteam Bucket
2.payment
3.View Available Iteams
4.Go Back
""")
        ch2=int(input("Enter your choice: "))
        if(ch2==1):
            name=input("Enter your product name: ")
            pcode=int(input("Enter your product code: "))
            quantity=int(input("Enter your  purchase product quantity: "))
            mycursor.execute("select*from stock where pcode='"+str(pcode)+"'")
            for i in mycursor:
                t_code,t_name,t_quantity,t_price=i
            amount=t_price*quantity
            net_quantity=t_quantity-quantity
            mycursor.execute("update stock set quantity='"+str(net_quantity)+"'where pcode='"+str(pcode)+"'")
            mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(pcode)+"','"+str(amount)+"')")
            mydb.commit()
            print("Iteam bucket inserted successfully...")

        elif(ch2==2):
            print(f"amount to be paid {amount}")
            mycursor.execute("select*from purchase")
            print("amount paid successfully...")

        elif(ch2==3):
            print("code || name || price")
            mycursor.execute("select*from stock")
            for i in mycursor:
                t_code,t_name,t_quantity,t_price=i
                print(f"{t_code} || {t_name} || {t_quantity} || {t_price}")
                print("View all Available Iteams sucessfully...")

        elif(ch2==4):
            print("Go Back...")
            
###############################################EXIT SECTION####################################################################         
    elif(ch==3):
        print("""
                                                                                     ______________
                                                                            >>>>>>>>>>EXIT SECTION>>>>>>>>>>
                                                                                     ______________
""")
        print("Exit successfully...")
        
    
    
            
            
            
                      
                
                        

