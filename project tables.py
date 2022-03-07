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
cur.execute("Insert into delhi (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format(('Calrion Hotel',4,4999,22),('International',5,7999,4),('St German',4,7999,12),('Trivage',3,1399,41)))
cur.execute("Insert into kolkata (hotel_name,rating,price,available_rooms) values('{}',{},{},{})".format(('Big Innit hotel',5,5599,1),('Lush Green Gardens',4, 4999,15),('Skyraise Hotel',3,2999,29),('Small Manifold hotel',5,5999,10)))
db.commit()