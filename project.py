import mysql.connector

db = mysql.connector.connect(host="localhost",user = "root", passwd = "shambo",database = "project")
cur = db.cursor()

def profile():
    name = input("Enter username : ")
    emal = input("Enter email address : ")
    pswd = input("Enter password : ")
    st = "Insert into account values('{}','{}','{}',{},{},NULL)".format(name,emal,pswd,0,0)
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
            print(                      'Name','     ','Rating','  ','price','    ','Available Rooms')
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
    elif sorter == 4:
        st = f'select * from {city1}'
        cur.execute(st)
        data = cur.fetchall()
        for i in data:
            price = i[2]
            print('Hotel details are:',i[0],'|',i[1],'|',i[2],'|',i[3])

def booking():
    global print
    city = input("Enter your vacation destination : ")
    city1 = city.lower()
    if city1 == 'bangalore':
        cur.execute(f"select booking from account where name like '{n}' and Password = '{pas}'")
        info = cur.fetchall()
        room = info[0][0]
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
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
                    newprice = (rooms-1)*price
                    st = f"update account set Booking = '{rooms + room}' where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set Price = '{price + newprice}' where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                    cur.execute(st)
                    cur.execute(f'select * from account where name = "{n}"')
                    hotel_info = cur.fetchall()
                    for j in hotel_info:
                        if j[5] == None or j[5] == hotel:
                            st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                            cur.execute(st)
                        else:
                            print('You cannot book more than 1 hotel at a time.')
                    cur.execute(f'update bangalore set available_rooms = {i[3]-rooms} where hotel_name = "{i[0]}"')
                    db.commit()
                    print('Total cost is',oprice + newprice + price)
                    db.commit()
                else:
                    print('Number of rooms booked is more than available')
                    newprice = 0
                    price = 0
    if city.lower() == "chennai":
        city1 = city.lower()
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
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
                    newprice = price*(rooms-1)
                    st = f"update account set Booking = '{rooms + room}' where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set price = {price + newprice} where name = '{n}'"
                    cur.execute(st)
                    st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                    cur.execute(st)
                    cur.execute(f'select * from account where name = "{n}"')
                    hotel_info = cur.fetchall()
                    for j in hotel_info:
                        if j[5] == None or j[5] == hotel:
                            st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                            cur.execute(st)
                        else:
                            print('You cannot book more than 1 hotel at a time.')
                            newprice = 0
                            price = 0

                    cur.execute(f'update chennai set available_rooms = {i[3]-rooms} where hotel_name = "{i[0]}"')
                    db.commit()
                    print('Total cost is',oprice + newprice + price)
                    db.commit()
                else:
                    print('Number of rooms booked is more than available')
            else:
                print('Hotel Not found')
    if city.lower() == "mumbai":
        city1 = city.lower()
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
         
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
                    st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                    cur.execute(st)
                    cur.execute(f'select * from account where name = "{n}"')
                    hotel_info = cur.fetchall()
                    for j in hotel_info:
                        if j[5] == None or j[5] == hotel:
                            st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                            cur.execute(st)
                        else:
                            print('You cannot book more than 1 hotel at a time.')
                            newprice = 0
                            price = 0
                    cur.execute(f'update mumbai set available_rooms = {i[3]-rooms} where hotel_name = "{i[0]}"')
                    db.commit()
                    print('Total cost is',oprice + newprice + price)
                    db.commit()
                else:
                    print('Number of rooms booked is more than available')
            else:
                print('hotel not found')

    if city.lower() == "kolkata":
        city1 = city.lower()
        sort(city1)
        hotel = input('Enter name of hotel:')
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
         
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
                    st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                    cur.execute(f'select * from account where name = "{n}"')
                    hotel_info = cur.fetchall()
                    for j in hotel_info:
                        if j[5] == None or j[5] == hotel:
                            st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                            cur.execute(st)
                        else:
                            print('You cannot book more than 1 hotel at a time.')
                            newprice = 0
                            price = 0
                    cur.execute(f'update kolkata set available_rooms = {i[3]-rooms} where hotel_name = "{i[0]}"')
                    db.commit()
                    print('Total cost is',oprice + newprice + price)
                    cur.execute(st)
                    db.commit()
                else:
                    print('Number of rooms booked is more than available')
            else:
                print('Hotel not found')
    
    
    if city.lower() == "delhi":
        sort(city1)
        st = f"select price from account where name = '{n}'"
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]  
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
                    cur.execute(f'select * from account where name = "{n}"')
                    hotel_info = cur.fetchall()
                    for j in hotel_info:
                        if j[5] == None or j[5] == hotel:
                            st = f"update account set hotel_booked = '{hotel}' where name = '{n}'"
                            cur.execute(st)
                        else:
                            print('You cannot book more than 1 hotel at a time.')
                            newprice = 0
                            price = 0
                    cur.execute(f'update delhi set available_rooms = {i[3]-rooms} where hotel_name = "{i[0]}"')
                    db.commit()
                    print('Total cost is',oprice + newprice + price)
            else:
                print('Hotel not found')


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
        print('Hotel booked is',i[5])
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
    for i in data:
        price = i[2]
    if no > cancelled:
        print('Cancelled rooms exceed rooms booked')
    else:
        st = f'update account set Booking = {cancelled-no} where Name = "{n}"'
        cur.execute(st)
        st = f'select price from account where name = "{n}" and password = "{pas}"'
        cur.execute(st)
        info = cur.fetchall()
        for j in info:
            oprice = j[0]
        st = f'update account set price = {oprice-price*no} where name = "{n}"'
        cur.execute(st)
        cur.execute(f'select available_rooms from {l} where hotel_name = "{h}"')
        info = cur.fetchall()
        for i in info:
            r = i[0]
        st = f'update {l} set available_rooms = {r+no} where hotel_name = "{h}"'
        cur.execute(st)
        db.commit()

def delete_account():
    st = f'delete from account where name = "{n}" and password = "{pas}"'
    cur.execute(st)
    db.commit()


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
        