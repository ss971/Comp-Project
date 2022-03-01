import mysql.connector

db = mysql.connector.connect(host="localhost",user = "root", passwd = "shambo",database = "project")
cur = db.cursor()

def profile():
    name = input("Enter username : ")
    emal = input("Enter email address : ")
    pswd = input("Enter password : ")
    st = "Insert into account values('{}','{}','{}',{},{})".format(name,emal,pswd,0,0)
    cur.execute(st)
    db.commit()

def sort(city1):
    print('1. Sort by Rating')
    print('2. Sort by Price Range')
    print('3. Sort by Rooms Available')
    print('4. No Sort')
    sorter = int(input('Enter choice:'))
    if sorter == 1:
        rate = int(input('Enter required rating(1-5):'))
        st = f'Select * from {city1} where rating = {rate}'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            price = i[2]
            print('Name','     ','Rating','  ','price','    ','Available Rooms')
            print('Hotel details are:',i[0],'|',i[1],'|',i[2],'|',i[3])
    elif sorter == 2:
        maxrange = int(input('Maximum price is:'))
        minrange = int(input('Minimum price is:'))
        st =f'select * from {city1} where price < {maxrange} and price > {minrange}'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            price = i[2]
            print('Hotel details are:',i[0],'|',i[1],'|',i[2],'|',i[3])
    elif sorter == 3:
        rooms = int(input('Rooms required:'))
        st = f'select * from {city1} where available_rooms > {rooms}'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            price = i[2]
            print('Hotel details are:',i[0],'|',i[1],'|',i[2],'|',i[3])


def booking():
    global print
    city = input("Enter your vacation destination : ")
    city1 = city.lower()
    cur.execute(f"select booking from account where name like '{n}' and Password = '{pas}'")
    info = cur.fetchall()
    room = info[0][0]
    if city.lower() == "bangalore":
        print('''+------------------+--------+-------+-----------------+
| hotel_name       | rating | price | available_rooms |
+------------------+--------+-------+-----------------+
| Enchanted Garden |      5 |  7590 |              12 |
| Hill view hotel  |      4 |  4995 |              33 |
| Residency Hotel  |      5 |  6500 |               8 |
| Suprema Lodge    |      3 |  1099 |              60 |
+------------------+--------+-------+-----------------+''')
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        print(oprice)
        hotel = input("Enter Hotel name : ")
        st = f'select price from bangalore where hotel_name = "{hotel}"'
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            price = j[0]
        st = f'select * from bangalore where hotel_name = "{hotel}"'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            if i[0] == hotel:
                print("HOTEL FOUND!!!!!!!!!")
                rooms = int(input("Enter number of rooms you would like to book : "))
                if rooms < i[3]:
                    newprice = rooms*price
                    st = f"update account set Booking = '{rooms + room}' where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set Price = '{price + newprice}' where name = '{n}'"
                    cur.execute(st)
                    db.commit()
                else:
                    print('Number of rooms booked is more than available')
    if city.lower() == "chennai":
        city1 = city.lower()
        print('''+----------------------+--------+-------+-----------------+
| hotel_name           | rating | price | available_rooms |
+----------------------+--------+-------+-----------------+
| Cliff Seaview Hotel  |      4 |  5999 |              25 |
| Felton Heights Hotel |      4 |  5999 |              30 |
| Red velvet inn       |      3 |  3999 |              39 |
| Watson creek         |      5 |  8999 |               7 |
+----------------------+--------+-------+-----------------+''')
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        print(oprice)
        hotel = input('Enter name of hotel you would like to book:')
        st = f'select * from chennai where hotel_name = "{hotel}"'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            if i[0] == hotel:
                print("HOTEL FOUND!!!!!!!!!")
                price = i[2]
                rooms = int(input("Enter number of rooms you would like to book : "))
                if rooms < i[3]:
                    newprice = price*rooms
                    st = f"update account set Booking = '{rooms + room}' where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set price = {price + newprice} where name = '{n}'"
                    cur.execute(st)
                    db.commit()
                    print('Total cost is:',newprice + oprice)
                else:
                    print('Number of rooms booked is more than available')
            else:
                print('Hotel Not found')
    if city.lower() == "mumbai":
        city1 = city.lower()
        print('''+--------------------+--------+-------+-----------------+
| hotel_name         | rating | price | available_rooms |
+--------------------+--------+-------+-----------------+
| Hotel Grande       |      4 |  5999 |              30 |
| Moonlit Inn        |      3 |  5999 |            NULL |
| Morning wood hotel |      3 |  5999 |              15 |
+--------------------+--------+-------+-----------------+''')
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        print(oprice)
        hotel = input('Enter hotel name:')
        st = f'select * from mumbai where hotel_name = "{hotel}"'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            if i[0] == hotel:
                print("HOTEL FOUND!!!!!!!!!")
                print = i[2]
                rooms = int(input("Enter number of rooms you would like to book : "))
                if rooms < i[3]:
                    newprice = (rooms-1)*price
                    st = f"update account set Booking = '{rooms + room}' where name = '{n}'" 
                    cur.execute(st)
                    st = f"update account set Price  = '{oprice + newprice}' where name = '{n}'"
                    cur.execute(st)
                    db.commit()
                    print('Total price is:',oprice + newprice)
                else:
                    print('Number of rooms booked is more than available')
            else:
                print('hotel not found')

    if city.lower() == "kolkata":
        city1 = city.lower()
        print('''+----------------------+--------+-------+-----------------+
| hotel_name           | rating | price | available_rooms |
+----------------------+--------+-------+-----------------+
| Big Innit hotel      |      5 |  5599 |               1 |
| Lush Green Gardens   |      4 |  4999 |              15 |
| Skyraise Hotel       |      3 |  2999 |              29 |
| Small Manifold hotel |      5 |  5999 |              10 |
+----------------------+--------+-------+-----------------+''')
        sort(city1)
        hotel = input('Enter name of hotel:')
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        print(oprice)
        st = f'select * from kolkata where hotel_name = "{hotel}"'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            if i[0] == hotel:
                print("HOTEL FOUND!!!!!!!!!")
                price = i[2]
                rooms = int(input("Enter number of rooms you would like to book : "))
                if rooms < i[3]:
                    newprice = price*(rooms-1)
                    st = f"update account set Booking = '{rooms+room}' where name = '{n}'"
                    cur.execute(st) 
                    st = f"update account set Price  = '{oprice + newprice}' where name = '{n}'"
                    cur.execute(st)
                    db.commit()
                    print('Total price is:',oprice + newprice)
                else:
                    print('Number of rooms booked is more than available')
            else:
                print('Hotel not found')
    
    
    if city.lower() == "delhi":
        print('''+---------------+--------+-------+-----------------+
| hotel_name    | rating | price | available_rooms |
+---------------+--------+-------+-----------------+
| Calrion Hotel |      4 |  4999 |              24 |
| International |      5 |  7999 |               4 |
| St German     |      4 |  7999 |              12 |
| Trivage       |      3 |  1399 |              44 |
+---------------+--------+-------+-----------------+''')
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        print(oprice)
        hotel = input('Enter Hotel Of choice:')
        st = f"select * from delhi where hotel_name = '{hotel}'"
        cur.execute(st)
        data = cur.fetchall() 
        for i in data:
            if i[0] == hotel:
                print("HOTEL FOUND!!!!!!!!!")
                price = i[2]
                rooms = int(input("Enter number of rooms you would like to book : "))
                if rooms > i[3]:
                    print('There are only',i[3],'rooms available')
                else:
                    newprice = (rooms-1)*price
                    st = f"update account set Booking = '{rooms+room}' where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set Price  = '{price + newprice}' where name = '{n}'"
                    cur.execute(st)
                    db.commit()
                    print('Total cost is',oprice + newprice)
            else:
                print('Hotel not found')
        else:
            print('City not found')

def show_profile():
    st1 = "select * from account where Name = '{}' and Password = '{}'".format(n,pas)
    cur.execute(st1)
    data1 = cur.fetchall()
 
    for i in data1:
        print('username is',i[0])
        print('email is',i[1])
        print('Password is',i[2])
        print('Rooms booked is',i[3])
        print('Total cost is',i[4])
        print('=============================================================================')

def existing_profile():
    print('--------------------------------------- ACCOUNT -------------------------------------')
    global n,pas
    n = input('Enter username:')
    pas = input('Enter password:')
    st1 = "select * from account where Name = '{}' and Password = '{}'".format(n,pas)
    cur.execute(st1)
    data1 = cur.fetchall()
    if data1 != []:
        print('Welcome back',n)
        print('=================================================================================')
    else:
        print('Username and password not matching')
        retry = input('Would you like to retry?(y/n)')
        if retry == 'y':
            existing_profile()
        else:
            print('=====================================================================================')

def cancel_booking():
    st = 'select booking from account where name = "{}" and Password = "{}"'.format(n,pas)
    cur.execute(st)
    info = cur.fetchall()
    for i in info:
        for j in i:
            cancelled = j
    no = int(input('Enter number of rooms you would like to cancel:'))
    l = input('Enter city:')
    h = input('Enter name of hotel which rooms you would like to cancel:')
    st = f'select * from {l} where hotel_name = "{h}"'
    cur.execute(st)
    data = cur.fetchall()
    print(data)
    for i in data:
        price = i[2]
    if no > j:
        print('Cancelled rooms exceed rooms booked')
    else:
        st = f'update account set Booking = {j-no} where Name = "{n}"'
        cur.execute(st)
        st = f'select price from account where name = "{n}" and password = "{pas}"'
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        st = f'update account set price = {oprice-price*no} where name = "{n}"'
        cur.execute(st)
        db.commit()

def delete_account():
    st = f'delete from account where name = "{n}" and password = "{pas}"'
    cur.execute(st)


print('1. Create an account')
print('2. Login from account')
use = int(input('Select choice:'))
if use == 1:
    try:
        profile()
        existing_profile()
        while True:
            print('3. View Profile')
            print('4. Check hotels booked')
            print('5. Book hotel')
            print('6. Cancel Booking')
            print('7. Delete Account')
            print('====================================================================================')
            use = int(input('Select choice:'))
            if use ==3:
                show_profile()
            if use == 4:
                st = 'select Booking from account where name = "{}"'.format(n)
                cur.execute(st)
                data = cur.fetchall()
                for i in data:
                    print('Booked:',i[0])
            if use == 5:
                booking()
            if use == 6:
                cancel_booking()
            if use == 7:
                delete_account()
            c = input('Continue: (y/n)')
            print('=================================================================================')
            if c != 'y':
                print('Thank you') 
                break
    except mysql.connector.errors.IntegrityError:
        print('Username already exists')
        existing_profile()
        while True:
            print('3. View Profile')
            print('4. Check hotels booked')
            print('5. Book hotel')
            print('6. Cancel Booking')
            print('7. Delete Account')
            print('====================================================================================')
            use = int(input('Select choice:'))
            if use ==3:
                show_profile()
            if use == 4:
                st = 'select Booking from account where name = "{}"'.format(n)
                cur.execute(st)
                data = cur.fetchall()
                for i in data:
                    print('Booked:',i[0])
            if use == 5:
                booking()
            if use == 6:
                cancel_booking()
            if use == 7:
                delete_account()
            c = input('Continue: (y/n)')
            print('=================================================================================')
            if c != 'y': 
                break    
elif use == 2:
    existing_profile()
    while True:
        print('3. View Profile')
        print('4. Check hotels booked')
        print('5. Book hotel')
        print('6. Cancel Booking')
        print('7. Delete Account')
        print('====================================================================================')
        use = int(input('Select choice:'))
        if use ==3:
            show_profile()
        if use == 4:
            st = 'select Booking from account where name = "{}"'.format(n)
            cur.execute(st)
            data = cur.fetchall()
            for i in data:
                print('Booked:',i[0])
        if use == 5:
            booking()
        if use == 6:
            cancel_booking()
        if use == 7:
            delete_account()
        c = input('Continue: (y/n)')
        print('=================================================================================')
        if c != 'y': 
            break
        