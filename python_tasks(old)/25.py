import pymysql.cursors
import sys

connection = pymysql.connect(host='localhost',
                             port= 3306,
                             user='root',
                             password='1234',
                             database='bookshop',
                             cursorclass=pymysql.cursors.DictCursor)

command=sys.argv


def create_table():
    with connection.cursor() as cursor:
        sql="""
        create table Book_info(
        id int not null primary key auto_increment,
        title varchar(100) not null,
        author  varchar(100) not null,
        published_at date,
        exist boolean default true,
        genre varchar(100) not null,
        language varchar(100) not null,
        price decimal(10,2) not null
        );
        """
        cursor.execute(sql)
    connection.commit()    

def create_book(book_name,author_name,date,genre_,lang,price_):
    with connection.cursor() as cursor:
        sql="""
        insert into Book_info(title,author,published_at,genre,language,price) values (%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql,(book_name,author_name,date,genre_,lang,price_))
    connection.commit()          

def show_all():
    with connection.cursor() as cursor:
        sql="""
        select * from Book_info;
        """
        cursor.execute(sql)
    return cursor.fetchall()

def show_book(id):
    with connection.cursor() as cursor:
        sql="""
        select * from Book_info where id=%s;
        """
        cursor.execute(sql,id)
    return cursor.fetchone()

def change_status(id):
    with connection.cursor() as cursor:
        sql="""
        UPDATE Book_info
            SET exist = CASE
                 WHEN exist=0 THEN 1
                 WHEN exist=1 THEN 0
             END
        WHERE id=%s
        """
        cursor.execute(sql,id)
    connection.commit()

def change_price(price,id):
    with connection.cursor() as cursor:
        sql="""
        update Book_info set price = %s where id = %s
        """
        cursor.execute(sql,(price,id))
    connection.commit()

def remove(id):
    with connection.cursor() as cursor:
        sql="""
        delete from Book_info where id=%s
        """
        cursor.execute(sql,id)
    connection.commit()    

def search_book(key):
    with connection.cursor() as cursor:
        sql=f"""
        select * from Book_info where title like "%{key}%" or author like "%{key}%";
        """
        cursor.execute(sql)
    return cursor.fetchall()


 

if len(command)==3 and command[1]=="add" and command[2]=="table":
    create_table()

elif len(command)==3 and command[1]=="add" and command[2]=="book":
    book_name =input('Enter BookName:')
    author_name =input('Enter AuthorName:')
    date =input('Enter date [yyyy-mm-dd]:')
    genre_ =input('Enter genre:')
    lang =input('Enter language:')
    price_ =input('Enter price:')
    create_book(book_name,author_name,date,genre_,lang,price_)

elif len(command)==3 and command[1]=="show" and command[2]=="all":
    for book in show_all():
        print(book)

elif len(command)==3 and command[1]=="show" and command[2]=="book":
    id=input('ID daxil edin gorey:')
    print(show_book(id))

elif len(command)==3 and command[1]=="change" and command[2]=="status":
    id=input('ID yaz gorum:')
    change_status(id)
    print('Status changed') 

elif len(command)==4 and command[1]=="change" and command[2]=="price":
    id=input('ID yaz gorum:')
    new_price = command[3]
    change_price(new_price,id)
    print('Price changed') 

elif len(command)==2 and command[1]=="remove":
    id=input('ID yaz gorey, tezol:')
    remove(id)
    print('Removed') 

elif len(command)==2 and command[1]=="search":
    word=input('Ne axtarirsan a bala?')
    print(word)
    for book in search_book(word):
        print(book)
