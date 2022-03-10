import mysql.connector
db = mysql.connector.connect(host="localhost",user = "root", passwd = "shambo",db = 'project')
cur = db.cursor()

bang = '''create table Bangalore(
hotel_name varchar(50) primary key,
rating int,
price int,
available_rooms int
);'''
cur.execute(bang)

chen = '''create table chennai(
hotel_name varchar(50) primary key,
rating int,
price int,
available_rooms int
);'''
cur.execute(chen)

delh = '''create table delhi(
hotel_name varchar(50) primary key,
rating int,
price int,
available_rooms int
);'''
cur.execute(delh)

mumb = '''create table mumbai(
hotel_name varchar(50) primary key,
rating int,
price int,
available_rooms int
);'''
cur.execute(mumb)

kolk = '''create table kolkata(
hotel_name varchar(50) primary key,
rating int,
price int,
available_rooms int
);'''
cur.execute(kolk)

acc = '''create table account(
    name varchar(50) primary key,
    email varchar(100),
    password varchar(50),
    booking int,
    price int,
    hotel_booked varchar(100)
    );'''
cur.execute(acc)

cur.execute("Insert into bangalore (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Enchanted Garden',5,7950,12))
cur.execute("Insert into bangalore (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Hill view hotel',4,4995,33))
cur.execute("Insert into bangalore (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Residency Hotel',5,6500,8))
cur.execute("Insert into bangalore (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Suprema Lodge',3,1099,60))
cur.execute("Insert into delhi (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Calrion Hotel',4,4999,22))
cur.execute("Insert into delhi (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('International',5,7999,4))
cur.execute("Insert into delhi (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('St German',4,7999,12))
cur.execute("Insert into delhi (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Trivage',3,1399,41))
cur.execute("Insert into kolkata (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Big Innit hotel',5,5599,1))
cur.execute("Insert into kolkata (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Lush Green Gardens',4, 4999,15))
cur.execute("Insert into kolkata (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Skyraise Hotel',3,2999,29))
cur.execute("Insert into kolkata (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Small Manifold hotel',5,5999,10))
cur.execute("Insert into chennai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Cliff SeaView Hotel',4,5999,25))
cur.execute("Insert into chennai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Felton Heights Hotel',4,5999,30))
cur.execute("Insert into chennai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Red Velvet Inn',3,3999,39))
cur.execute("Insert into chennai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Watson Creek',5,8999,7))
cur.execute("Insert into mumbai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Hotel Grande',4,5999,30))
cur.execute("Insert into mumbai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Moonlight Inn',3,1999,40))
cur.execute("Insert into mumbai (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format('Morning Wood Hotel',5,7999,15))
db.commit()
