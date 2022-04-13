import mysql.connector as sql
import panda as pd

u = input('PLEASE PROVIDE YOUR MYSQL USERNAME:  ')
p = input('PLEASE GIVE YOUR MYSQL PASSWORD:  ')
conn = sql.connect(host='localhost',
                   user=u,
                   password=p)



if conn.is_connected():
    print('Connection Successful...'.upper())


cur = conn.cursor()

def line(n):
    print('*'*n)

def drop_database():
    q='drop database travel_management'
    cur.execute(q)

def create_database():
    q='create database travel_management'
    cur.execute(q)

def use_database():
    q='use travel_management'
    cur.execute(q)

def create_tables():
    q='''create table customer(cust_ID varchar(20) PRIMARY KEY,
                               Name varchar(50) NOT NULL,
                               Contact_Number bigint NOT NULL,
                               Email_ID varchar(35))'''
    cur.execute(q)

    q='''create table bus(book_ID varchar(10) PRIMARY KEY,
                          cust_ID varchar(20) NOT NULL,
                          Seat_num int NOT NULL,
                          Start_dest varchar(300) NOT NULL,
                          End_dest varchar(300) NOT NULL,
                          Date_of_journey date)'''
    cur.execute(q)

    q='''create table flight(book_ID varchar(10) PRIMARY KEY,
                             cust_ID varchar(20) NOT NULL,
                             Seat_num int NOT NULL,
                             Start_dest varchar(300) NOT NULL,
                             End_dest varchar(300) NOT NULL,
                             Date_of_journey date)'''
    cur.execute(q)

    q='''create table cab(book_ID varchar(10) PRIMARY KEY,
                          cust_ID varchar(20)NOT NULL,
                          Type varchar(20) NOT NULL,
                          Start_dest varchar(300) NOT NULL,
                          End_dest varchar(300) NOT NULL,
                          Date_of_journey date)'''
    cur.execute(q)

    
def set_database():
    q='show databases'
    cur.execute(q)
    db=cur.fetchall()
    if ('travel_management',) not in db:
        print(f"""
The required database is not present.

Please wait while the database is being created.....
""")
        create_database()
        print("The database with the name 'travel_management' is created successfully")
    use_database()
    cur.execute('show tables')
    res=cur.fetchall()
    if res==[]:
        create_tables()


def show_tables():
    q='show tables'
    tab=cur.execute(q)
    nrec=cur.rowcount
    if nrec==0:
        create_tables()

    
'''CANCEL BOOKING FUNCTION'''
def cancel_booking():                                                   
    ans='y'
    while ans.lower()=='y':
        _id = input('Please give booking id to cancel booking: ')
        if _id[:3]=='BUS':
            q='delete from bus where book_ID in(\"{}\")'.format(_id)

        elif _id[:3]=='OCB':
            q='delete from cab where book_ID in(\"{}\")'.format(_id)

        elif _id[:3]=='FLI':
            q='delete from flight where book_ID in(\"{}\")'.format(_id)

        elif _id[:3]=='CAB':
            q='delete from cab where book_ID in(\"{}\")'.format(_id)
        cur.execute(q)
        conn.commit()
        print(f'The Booking for the booking ID {_id} has been Cancelled Successfully.')
        ans=input('Any more bookings to be cancelled? (y/n) :')



'CUSTOMER BOOKING FUNCTION'
def cust_booking():                                                         
    inp2=input('''
                   #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                   # 1. FOR BOOKING A CAB              #--->(1)
                   #-----------------------------------#
                   # 2. FOR BOOKING AN OUTSTATION CAB  #--->(2)
                   #-----------------------------------#
                   # 3. FOR BOOKING A BUS              #--->(3)
                   #-----------------------------------#
                   # 4. FOR BOOKING A FLIGHT           #--->(4)
                   #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                --->''')

    
    if inp2=='1':  # CAB BOOKING
        ans='y'
        while ans.lower()=='y':
            book_ID = '"CAB' + '{}\"'.format(input('Please enter booking ID: '))
            cust_ID = '\"{}\"'.format(input('Please give customer ID: '))
            start_des = '\"{}\"'.format(input("Please Enter starting destination: "))
            end_des = '\"{}\"'.format(input("Please Enter ending destination: "))
            jour_date = '\"{}\"'.format(input("Enter date of journey(YYYY-MM-DD): "))
            typ1 = '"IN-STATION"'
            query = "insert into cab values({0},{1},{2},{3},{4},{5})".format(book_ID,cust_ID,typ1,start_des,end_des,jour_date)
            cur.execute(query)
            conn.commit()
            print(f"Your In-station Cab has been booked. your booking ID is {book_ID}")
            ans = input("Any more bookings(y/n)? ")
 

    elif inp2=='2':  # OUTSTATION CAB BOOKING
        ans='y'
        while ans.lower()=='y':
            book_ID = '\"OCB' + '{}\"'.format(input('Please enter booking ID: '))
            cust_ID = '\"{}\"'.format(input('Please give customer ID: '))
            start_des = '\"{}\"'.format(input("Please Enter starting destination: "))
            end_des = '\"{}\"'.format(input("Please Enter ending destination: "))
            jour_date = '\"{}\"'.format(input("Enter date of journey(YYYY-MM-DD): "))
            typ1 = '"OUT-STATION"'
            query = "insert into cab values({0},{1},{2},{3},{4},{5})".format(book_ID,cust_ID,typ1,start_des,end_des,jour_date)
            cur.execute(query)
            conn.commit()
            print(f"Your Out-station Cab has been booked. your booking ID is {book_ID}")
            ans = input("Any more bookings(y/n)? ")


    elif inp2=='3':  # BUS BOOKING
        ans='y'
        while ans.lower()=='y':
            book_ID = '\"BUS' + '{}\"'.format(input('Please enter booking ID: '))
            cust_ID = '\"{}\"'.format(input('Please give customer ID: '))
            st = int(input('Please Enter seat no. (Between 1 to 100)'))
            start_des = '\"{}\"'.format(input("Please Enter starting destination: "))
            end_des = '\"{}\"'.format(input("Please Enter ending destination: "))
            jour_date = '\"{}\"'.format(input("Enter date of journey(YYYY-MM-DD): "))
            query = "insert into bus values({0},{1},{2},{3},{4},{5})".format(book_ID,cust_ID,st,start_des,end_des,jour_date)
            cur.execute(query)
            conn.commit()
            print(f"Your Bus has been booked. your booking ID is {book_ID}")
            ans = input("Any more bookings(y/n)? ")


    elif inp2=='4': # FLIGHT BOOKING
        ans='y'
        while ans.lower()=='y':
            book_ID = '\"FLI' + '{}\"'.format(input('Please enter booking ID: '))
            cust_ID = '\"{}\"'.format(input('Please give customer ID: '))
            st = int(input('Please Enter seat no. (Between 1 to 100)'))
            start_des = '\"{}\"'.format(input("Please Enter starting destination: "))
            end_des = '\"{}\"'.format(input("Please Enter ending destination: "))
            jour_date = '\"{}\"'.format(input("Enter date of journey(YYYY-MM-DD): "))
            query = "insert into flight values({0},{1},{2},{3},{4},{5})".format(book_ID,cust_ID,st,start_des,end_des,jour_date)
            cur.execute(query)
            conn.commit()
            print(f"Your Flight has been booked. your booking ID is {book_ID}")
            ans = input("Any more bookings(y/n)? ")

    

'BOOKING DETAILS FUNCTION'
def booking_details():                                                
    _id=input("Please provide your booking id: ")
    if _id[:3]=='BUS':
        q='select * from customer natural join bus where book_ID in(\"{}\")'.format(_id)
        q1='desc bus'
        
    elif _id[:3]=='OCB':
        q='select * from customer natural join cab where book_ID in(\"{}\") and type in("OUT-STATION")'.format(_id)
        q1='desc cab'

    elif _id[:3]=='FLI':
        q='select * from customer natural join flight where book_ID in(\"{}\")'.format(_id)
        s1='desc flight'

    elif _id[:3]=='CAB':
        q='select * from customer natural join cab where book_ID in(\"{}\") and type in("IN-STATION")'.format(_id)
        q1='desc cab'

    q2='desc customer'
    cur.execute(q)
    bkdt=cur.fetchone()
    head=[]

    cur.execute(q2)
    dat1=cur.fetchall()
    for rec in dat1:
        if rec[0] not in head:
            head.append(rec[0])

    cur.execute(q1)
    dat1=cur.fetchall()
    for rec in dat1:
        if rec[0] not in head:
            head.append(rec[0])
 
            
    line(80)
    if dat1!=None:
        for p in range(len(head)):
            print(head[p],bkdt[p],sep=': ')
    else:
        print('Empty Set')
    line(80)
    
'UPDATE CUSTOMER FUNCTION'
def update_c(_id,table,field,value):
    q='update {1} set {2}={3} where cust_ID in(\"{0}\")'.format(_id,table,field,value)
    cur.execute(q)
    conn.commit()
    print(f"The field {field} has been updated to {value} for customer ID {_id}")

'UPDATE BOOKING FUNCTION'
def update_b(_id,table,field,value):
    q='update {1} set {2}={3} where book_ID in(\"{0}\")'.format(_id,table,field,value)
    cur.execute(q)
    conn.commit()
    print(f"The field {field} has been updated to {value} for booking ID {_id}")


##______________________________MAIN METHOD______________________________
'########################################################################'



cur.execute('show databases')
l=cur.fetchall()
if ('travel_management',) not in l:
    set_database()
    
elif ('travel_management',) in l:
    set_database()





run = True


while run:
    global nm
    global ml
    global ph
    print('''
                                       **********************************
                                 ******|   WELCOME TO THE SERVICES OF   |******
                                    ***|       APOLLO TRAVELLING        |***
                                       **********************************
                                        ''')
    
    while run:
        inp=input('''
                                  +------------------------------------------+
                                  |  PLEASE SELECT AN APPROPRIATE OPTION :-  |
                                  |------------------------------------------|
                                  |  0. IF YOU ARE FIRST-TIME USER           |--->(0)
                                  |------------------------------------------|
                                  |  1. TO MAKE A BOOKING                    |--->(1)
                                  |------------------------------------------|
                                  |  2. TO CANCEL A BOOKING                  |--->(2)
                                  |------------------------------------------|
                                  |  3. TO CHECK BOOKING DETAILS             |--->(3)
                                  |------------------------------------------|
                                  |  4. TO GET CUSTOMER DETAILS              |--->(4)
                                  |------------------------------------------|
                                  |  5. TO GET LIST OF CUSTOMERS             |--->(5)
                                  |------------------------------------------|
                                  |  6. TO UPDATE BOOKING DETAILS            |--->(6)
                                  |------------------------------------------|
                                  |  7. TO UPDATE CUSTOMER DETAILS           |--->(7)
                                  |------------------------------------------|
                                  |  8. FOR EXIT                             |--->(8)
                                  +------------------------------------------+
                                  
                                                --->''')

        if inp=='0':
            ans='y'
            while ans.lower()=='y':
                cust_ID = '\"{}\"'.format(input('Please allot the customer ID: '))
                nm = '\"{}\"'.format(input('Please Enter customer name: '))
                ml = '\"{}\"'.format(input('Please Enter customer e-mail ID: '))
                ph = '\"{}\"'.format(int(input('Please enter customer contact number: ')))
                q="insert into customer values({0},{1},{2},{3})".format(cust_ID,nm,ph,ml)
                cur.execute(q)
                conn.commit()
                print(f'New Customer Added. Customer ID:[{cust_ID}]')
                ans = input('Anymore New Customers to be added? (y/n) ')
                
        elif inp=='1':
            cust_booking()

        elif inp=='2':
            cancel_booking()       

        elif inp=='3':
            booking_details()

        
        elif inp=='4':
            _id = input('Please provide your customer ID: ')
            q='select * from customer where cust_ID={}'.format(_id)
            cur.execute(q)
            dat=cur.fetchone()
            if data!=None:
                line(96)
                print(f'''
                    cust_ID         :{dat[0]}
************************************************************************************************
                    Name            :{dat[1]}
************************************************************************************************
                    Contact_Number  :{dat[2]}
************************************************************************************************
                    E-mail_ID       :{dat[3]}
    ''')
                line(96)

            
        elif inp=='5':
            q='select * from customer'
            cur.execute(q)
            cust=cur.fetchall()
            line(92)
            cid,name,phone,email,bl=[],[],[],[],[]
            for i in cust:
                bl.append("                ")
                cid.append(i[0])
                name.append(i[1])
                phone.append(i[2])
                email.append(i[3])
            rec={
                '':bl,
                'Cust_ID':cid,
                'Name':name,
                'Contact Number':phone,
                'Email_ID':email
                }
            pd.set_option('display.max_rows',None,'display.max_columns',None)
            rec_df=pd.DataFrame(rec)
            rec_df=rec_df.set_index('')
            print(rec_df)
            line(92)
            

        elif inp=='6':
            ans='y'
            while ans.lower()=='y':
                _id=input("Please enter booking ID: ")
                if _id[:3]=='CAB':
                    table='cab'
                    ques=input("""
                                    
                                    Which Booking Details need to be updated?
                                    +---------------------------+
                                    | 1. TYPE                   |--->(1)
                                    |---------------------------|
                                    | 2. STARTING DESTINATION   |--->(2)
                                    |---------------------------|
                                    | 3. ENDING DESTINATION     |--->(3)
                                    |---------------------------|
                                    | 4. DATE OF JOURNEY        |--->(4)
                                    +---------------------------+
                                                --->""")
                    if ques=='1':
                        field='Type'
                        value='\"OUT-STATION\"'
                        new_id=f'\"OCB{_id[3:]}\"'
                        q='update cab set {field}="{value}", book_ID="{new_id}" where book_ID in(\"{_id}\")'
                        cur.execute(q)
                        conn.commit()
                        m=f'Booking ID has been changed from {_id} to {new_id}'
                    elif ques=='2':
                        field='Start_dest'
                        value='\"{}\"'.format(input('Please give the new Start Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='3':
                        field='End_dest'
                        value='\"{}\"'.format(input('Please give the new End Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='4':
                        field='Date_of_journey'
                        value='\"{}\"'.format(input('Please give the new date of journey(YYYY-MM-DD): '))
                        update_b(_id,table,field,value)


                elif _id[:3]=='OCB':
                    table='cab'
                    ques=input("""
                                    
                                    Which Booking Details need to be updated?
                                    +---------------------------+
                                    | 1. TYPE                   |--->(1)
                                    |---------------------------|
                                    | 2. STARTING DESTINATION   |--->(2)
                                    |---------------------------|
                                    | 3. ENDING DESTINATION     |--->(3)
                                    |---------------------------|
                                    | 4. DATE OF JOURNEY        |--->(4)
                                    +---------------------------+
                                                --->""")
                    if ques=='1':
                        field='Type'
                        value='\"IN-STATION\"'
                        new_id=f'\"CAB{_id[3:]}\"'
                        q='update cab set {field}="{value}", book_ID="{new_id}" where book_ID in(\"{_id}\")'
                        cur.execute(q)
                        conn.commit()
                        m=f'Booking ID has been changed from {_id} to {new_id}'
                    elif ques=='2':
                        field='Start_dest'
                        value='\"{}\"'.format(input('Please give the new Start Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='3':
                        field='End_dest'
                        value='\"{}\"'.format(input('Please give the new End Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='4':
                        field='Date_of_journey'
                        value='\"{}\"'.format(input('Please give the new date of journey(YYYY-MM-DD): '))
                        update_b(_id,table,field,value)


                elif _id[:3]=='BUS':
                    table='bus'
                    ques=input("""
                                    
                                    Which Booking Details need to be updated?
                                    +---------------------------+
                                    | 1. SEAT NUMBER            |--->(1)
                                    |---------------------------|
                                    | 2. STARTING DESTINATION   |--->(2)
                                    |---------------------------|
                                    | 3. ENDING DESTINATION     |--->(3)
                                    |---------------------------|
                                    | 4. DATE OF JOURNEY        |--->(4)
                                    +---------------------------+
                                                --->""")
                    if ques=='1':
                        field='Seat_num'
                        value='{}'.format(input('Please give the new seat number: '))
                        update_b(_id,table,field,value)
                    elif ques=='2':
                        field='Start_dest'
                        value='\"{}\"'.format(input('Please give the new Start Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='3':
                        field='End_dest'
                        value='\"{}\"'.format(input('Please give the new End Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='4':
                        field='Date_of_journey'
                        value='\"{}\"'.format(input('Please give the new date of journey(YYYY-MM-DD): '))
                        update_b(_id,table,field,value)


                elif _id[:3]=='FLI':
                    table='flight'
                    ques=input("""
                                    
                                    Which Booking Details need to be updated?
                                    +---------------------------+
                                    | 1. SEAT NUMBER            |--->(1)
                                    |---------------------------|
                                    | 2. STARTING DESTINATION   |--->(2)
                                    |---------------------------|
                                    | 3. ENDING DESTINATION     |--->(3)
                                    |---------------------------|
                                    | 4. DATE OF JOURNEY        |--->(4)
                                    +---------------------------+
                                                --->""")
                    if ques=='1':
                        field='Seat_num'
                        value='{}'.format(input('Please give the new seat number: '))
                        update_b(_id,table,field,value)
                    elif ques=='2':
                        field='Start_dest'
                        value='\"{}\"'.format(input('Please give the new Start Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='3':
                        field='End_dest'
                        value='\"{}\"'.format(input('Please give the new End Destination: '))
                        update_b(_id,table,field,value)
                    elif ques=='4':
                        field='Date_of_journey'
                        value='\"{}\"'.format(input('Please give the new date of journey(YYYY-MM-DD): '))
                        update_b(_id,table,field,value)

                        
                if (_id[:3]=='CAB' or _id[:3]=='OCB') and ques=='1':
                    print(m)
                ans=input(f'{field} has been updated to {value} for the booking ID {_id}. Any more Updating of records? (y/n) ')


        elif inp=='7':
            ans='y'
            table='customer'
            while ans.lower()=='y':
                _id=input('Please give CUSTOMER ID: ')
                ques=input("""
                
                                    Which Customer Details need to be updated?

                                    +---------------------------+
                                    | 1. CONTACT NUMBER         |--->(1)
                                    |---------------------------|
                                    | 2. E-MAIL ID              |--->(2)
                                    +---------------------------+
                                        --->""")
                if ques=='1':
                    field='Contact_Number'
                    N='{}'.format(input('Please enter the new contact number:'))
                    update_c(_id,table,field,N)
                elif ques=='2':
                    field='Email_ID'
                    M='\"{}\"'.format(input('Please enter the new e-mail ID:'))
                    update_c(_id,table,field,M)
                ans=input(f"{field} has been updated to {value} for Customer ID {_id}. Any more records to be updated? (y/n) ")


        elif inp=='8':
            ans=input('Are you sure you want to exit?(Y/N)'.upper())
            if ans.upper()=='Y':
                run=False
            elif ans.upper()=='N':
                continue
    print('Thank you for using our services! Have a nice day ahead!')
    cur.close()
