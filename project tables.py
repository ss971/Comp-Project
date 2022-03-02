import mysql.connector
db = mysql.connector.connect(host="localhost",user = "root", passwd = "shambo",db = 'project')
cur = db.cursor()

cur.execute("use testbase")

bang = '''create table Bangalore(
hotel_name varchar(50) primary key,
rating int,
price int,
available_rooms int
);'''
cur.execute(bang)

chen = '''create table chennai(
hotel_name varchar(50) primary key,
rating int
price int
available_rooms int
);'''

delh = '''create table delhi(
hotel_name varchar(50) primary key,
rating int
price int
available_rooms int
);'''

mumb = '''create table mumbai(
hotel_name varchar(50) primary key,
rating int
price int
available_rooms int
);'''

kolk = '''create table kolkata(
hotel_name varchar(50) primary key,
rating int
price int
available_rooms int
);'''

acc = '''create table account(
    name varchar(50) primary key
    email varchar(100)
    password varchar(50)
    booking int
    price int
    hotel_booked varchar(100)
    );'''

cur.execute("Insert into bangalore (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format(('Enchanted Garden',5,7950,12),('Hill view hotel',4,4995,33),('Residency Hotel',5,6500,8),('Suprema Lodge',3,1099,60)))
db.commit()