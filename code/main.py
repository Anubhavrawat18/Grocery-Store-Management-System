
import mysql.connector as sql
cart = []
l1 = []
#TO SETUP CONNECTION
conn=sql.connect(host="localhost", user="root", passwd="your_password-Comes_here", database="GROCERY_STORE")
if conn.is_connected():
    print("Successfully Connected to mySQL Database")
cursor=conn.cursor()
print('')
print('-------------------------------WELCOME-------------------------------')
print('')
print("----------------------GROCERY MANAGEMENT SYSTEM----------------------")
print('\n*2')
#FUNCTION TO UPDATE THE QUANTITY OF PRODUCTS AVAILABLE AFTER EACH PURCHASE

def update(table, quantity, name):
    cursor.execute("UPDATE {} SET qty=qty-{} where Iname = '{}'".format(table, quantity, name))
    conn.commit()
again = "y"

while True:
    print('1.FRUITS')
    print('')
    print('2.VEGETABLES')
    print('')
    print('3.DRINKS')
    print('')
    print('4.BAKED ITEMS')
    print('')
    print('5.DAIRY')
    print('')
    print('6.HOUSEHOLD AND CLEANING')

    print('')
    print('7.MEAT ITEMS')
    print('')
    print('8.CANNED PRODUCTS')
    print('')
    choice = int(input("ENTER YOUR CHOICE(1/2/3/4/5/6):"))


    #IF THE CUSTOMER WISHES TO BUY FRUITS

    if choice == 1:
        print("AVAILABLE FRUIT OPTIONS ARE:")
        cursor.execute("select * from fruits")
        data=cursor.fetchall()
        for i in data:
            print()
            print(i)
        c=input('ENTER FRUIT OF CHOICE:')
        q=int(input("Enter Required Quantity:"))
        cursor.execute("SELECT qty FROM fruits WHERE Iname='{}'".format(c))
        data=cursor.fetchall()
        quantity=int(data[0][0])
        if quantity >= q:
            n1=cursor.execute('select * from fruits where Iname="{}"'.format(c))
            j1=cursor.fetchall()
            for j in j1:
                cart.append(c)
            cursor.execute("select price*{} from fruits where Iname ='{}'".format(q, c))
            new=cursor.fetchall()
            for f in new:
                l1.append(f)
            update('fruits', q, c)
        else:
            print("NOT ENOUGH QUANTITY OF PRODUCT AVAILABLE")


    #IF THE CUSTOMER WISHES TO BUY VEGETABLES

    if choice == 2:
        print("AVAILABLE VEGETABLES OPTIONS ARE:")
        cursor.execute("select * from veg")
        data = cursor.fetchall()
        for i in data:
            print()
            print(i)
        c = input('ENTER VEGETABLES OF CHOICE:')
        q = int(input("Enter Required Quantity:"))
        cursor.execute("SELECT qty FROM veg WHERE Iname= '{}'".format(c))
        data = cursor.fetchall()
        quantity = int(data[0][0])
        if quantity >= q:
            n2 = cursor.execute('select * from veg where Iname="{}"'.format(c))
            j2 = cursor.fetchall()
            for j in j2:
                cart.append(c)
            cursor.execute("select price*{} from veg where Iname = '{}'".format(q, c))
            new = cursor.fetchall()
            for f in new:
                l1.append(f)
            update('veg', q, c)
        else:
            print("NOT ENOUGH QUANTITY OF PRODUCT AVAILABLE")


    #IF THE CUSTOMER WISHES TO BUY DRINKS

    if choice == 3:
        print("AVAILABLE DRINKS ARE:")
        cursor.execute("select * from drinks")
        data = cursor.fetchall()
        for i in data:
            print()
            print(i)
        c = input('ENTER DRINKS OF CHOICE:')
        q = int(input("Enter Required Quantity:"))

        n3 = cursor.execute('select * from drinks where Iname="{}"'.format(c))
        j3 = cursor.fetchall()
        for j in j3:
            cart.append(c)
        cursor.execute("select price*{} from drinks where Iname = '{}'".format(q, c))
        new = cursor.fetchall()
        for f in new:
            l1.append(f)
        update('drinks', q, c)


    #IF THE CUSTOMER WISHES TO BUY BAKED ITEMS

    if choice == 4:
        print("AVAILABLE BAKED ITEMS ARE:")
        cursor.execute("select * from baked")
        data = cursor.fetchall()
        for i in data:
            print()
            print(i)
        c = input('ENTER ITEM OF CHOICE:')
        q = int(input("Enter Required Quantity:"))
        n4 = cursor.execute('select * from baked where Iname="{}"'.format(c))
        j4 = cursor.fetchall()
        for j in j4:
            cart.append(c)
        cursor.execute("select price*{} from baked where Iname = '{}'".format(q, c))
        new = cursor.fetchall()
        for f in new:
            l1.append(f)
        update('baked', q, c)


    #IF THE CUSTOMER WISHES TO BUY DAIRY PRODUCTS

    if choice == 5:
        print("AVAILABLE DAIRY PRODUCTS ARE:")

        cursor.execute("select * from dairy")
        data = cursor.fetchall()
        for i in data:
            print()
            print(i)
        c = input('ENTER PRODUCTS OF CHOICE:')
        q = int(input("Enter Required Quantity:"))
        n5 = cursor.execute('select * from dairy where Iname="{}"'.format(c))
        j5 = cursor.fetchall()
        for j in j5:
            cart.append(c)
        cursor.execute("select price*{} from dairy where Iname = '{}'".format(q, c))
        new = cursor.fetchall()
        for f in new:
            l1.append(f)
        update('dairy', q, c)

    #IF THE CUSTOMER WISHES TO BUY HOUSEHOLD AND BABY-CARE PRODUCTS

    if choice == 6:
        print("AVAILABLE HOUSEHOLD AND CLEANING PRODUCTS ARE:")
        cursor.execute("select * from household")
        data = cursor.fetchall()
        for i in data:
            print()
            print(i)
        c = input('ENTER HOUSEHOLD AND CLEANING PRODUCTS OF CHOICE:')
        q = int(input("Enter Required Quantity:"))
        n6 = cursor.execute('select * from household where Iname="{}"'.format(c))
        j6 = cursor.fetchall()
        for j in j6:
            cart.append(c)
        cursor.execute("select price*{} from household where Iname = '{}'".format(q, c))

        new = cursor.fetchall()
        for f in new:
            l1.append(f)
        update('household', q, c)

    #IF THE CUSTOMER WISHES TO BUY MEAT PRODUCTS

    if choice == 7:
        print("AVAILABLE MEAT OPTIONS ARE:")
        cursor.execute("select * from meat")
        data=cursor.fetchall()
        for i in data:
            print()
            print(i)
        c=input('ENTER ITEM OF CHOICE:')
        q=int(input("Enter Required Quantity:"))
        n7=cursor.execute('select * from meat where Iname="{}"'.format(c))
        j7=cursor.fetchall()
        for j in j7:
            cart.append(c)
        cursor.execute("select price*{} from meat where Iname = '{}'".format(q, c))
        new=cursor.fetchall()
        for f in new:
            l1.append(f)
        update('meat', q, c)

    #IF THE CUSTOMER WISHES TO BUY CANNED ITEMS

    if choice == 8:
        print("AVAILABLE CANNED ITEMS ARE:")
        cursor.execute("select * from cans")
        data=cursor.fetchall()
        for i in data:
            print()
            print(i)

        c=input('ENTER CANNED ITEM OF CHOICE:')
        q=int(input("Enter Required Quantity:"))
        n8=cursor.execute('select * from cans where Iname="{}"'.format(c))
        j8=cursor.fetchall()
        for j in j8:
            cart.append(c)
        cursor.execute("select price*{} from cans where Iname = '{}'".format(q, c))
        new=cursor.fetchall()
        for f in new:
            l1.append(f)
        update('cans', q, c)

    again= input("Do you want to add more y/n : ")   #CHOICE OF PURCHASING MORE PRODUCTS
    if again =='Y' or again =='y':
        print()
    else:
        break
c=0
for i in range(len(l1)):                             #TRAVERSING THE LIST THAT HAS THE PRICExQUANTITY OF ALL THE PRODUCTS PURCHASED
    t=list(l1[i])                                    #PART THAT CONVERTS EACH TUPLE TYPE ELEMENTS TO LIST TYPE
    l1[i]=t                                          #REASSIGNING THE VALUES AS TUPLE FORM ELEMENTS
print("\n"*10)
print('--------------------------------------------------------------------------------------------------------------')
print()
print("                                                     BILL                                                     ")
for i in range(len(l1)):
    c=c+l1[i][0]                                      #VARIABLE THAT HAS BEEN ASSIGNED THE TOTAL BILL AMOUNT
print()
print("YOUR PURCHASED ITEMS ARE:")
for i in cart:
    print(i)

print("Your Total Bill Amount Is: Rs.",c)
print()
print("*******************************************THANK YOU FOR VISITING*********************************************")
print()
print("-----------------------------------------------HAVE A NICE DAY------------------------------------------------")
print('**********************************************PLEASE VISIT AGAIN**********************************************')
conn.close()



#*****************************************************END OF PROGRAM ****************************************************
