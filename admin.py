import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor() 
print("1.Initialize")
print("2.Insert")
print("3.Update")
print("4.View All")
print("5.Delete")
print("6.Exit")
while True:
    i=int(input("Enter the choice "))
    if i==1:
        conn.execute('''CREATE TABLE CHAT
         (id INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
         question           TEXT    NULL,
         response           TEXT     NULL);''')
        print("Table created successfully")
        data = [(1, 'hi', 'Hello!'),
             (2,'Hi','Good to see you again!'),
             (3,'hi','Hi there, how can I help?'),
             (4,'how are you','Hello'),
             (5,'how are you?','Good to see you again!'),
             (6,'How are you?','Hi there, how can I help?'),
             (7,'see you later','Talk to you later'),
             (8,'See you later','Goodbye!'),
             (9,'goodbye','Goodbye!'),
             (10,'Goodbye','Talk to you later'),
             (11,'what are your hours','We are open 9am-3:20pm Monday-saturday!'),
             (12,'hours of operation','9am-3:20pm Monday-saturday!'),
             (13,'Hours of operation','9am-3:20pm Monday-saturday!')        
             ]
        c.executemany('INSERT INTO CHAT VALUES (?,?,?)', data)
        conn.commit()
    elif i==2:
        q=input("Enter question ")
        r=input("Enter response ")
        qry="INSERT INTO CHAT (question,response) VALUES('"+q+"','"+r+"')"
        c.execute(qry)
        conn.commit()
    elif i==3:
        id=int(input("Enter id "))
        a=id
        id=(id,)
        d=c.execute('SELECT * FROM CHAT WHERE id=?',id)
        for row in d:
            print(row)
        a=str(a)
        q=input("Enter question")
        r=input("Enter response")
        qry="UPDATE CHAT SET question='"+q+"',response='"+r+"' WHERE id="+a
        print(qry)
        c.execute(qry)
        conn.commit()
    elif i==4:
        d=c.execute('SELECT * FROM CHAT')
        for row in d:
            print(row)
    elif i==5:
        id=int(input("Enter id"))
        id=(id,)
        d=c.execute('SELECT * FROM CHAT WHERE id=?',id)
        if(d):
            c.execute("DELETE FROM CHAT WHERE id=?",id)
            conn.commit()
        else:
            print("Data not found")
    elif i==6:
        exit()
    else:
        print("Invalid Choice")
