#Official file
#Shailja Shaktawat
#XII-B

import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd


mycon = mysql.connect(
    host='localhost',
    user ='root',
    password = 'jamless7',
    database='library')

if mycon.is_connected():
    print('MySQL connection successfully established.')

cur = mycon.cursor()


#Functions in sequence:
'''
1) exit_func
2) check_id
3) register
4) issue_book
5) return_book
6) book_exc
7) member_exc
8) menu3-For Admin
9) menu2-issue,return,exit
10) login
11) startmenu1-login,register,exit
'''


#To exit the running application anytime.

def exit_func():
    print('Thank you for paying a visit to us! Have a fulfilling day! :)')
    wait = input('\n\n\n Press any key to exit...') 
    

#To check if the inputed id already exists.
    
def check_id():
    correct=True
    while correct:
        m_id = int(input('Enter a chosen id number:'))
        
        cur.execute('SELECT member_id FROM member_details WHERE member_id = %s;'%(m_id))
        x=cur.fetchall()
        if x==[]:
            correct=False
            break
        y=x.pop(0)
        z= y[0]

        if z == m_id:
            print('The ID already exists, try again')
            pass
        
        
        
#Registration
def register():
    print('So you wanna become a member of our low profile hi-tech library? \nSure. \nHere you go.')
    check_id()
    mem_id=input('Confirm your id:')
    f_name = input('Enter first name: ')
    l_name = input('Enter last name: ')
    add = input('Enter address: ')
    dob = input('Date of Birth (YYYY-MM-DD): ')
    phone = input('Contact number: ')
    password=input('Set password: ')
    email=input('Enter your email id:')

    cur.execute('INSERT INTO member_details(member_id,first_name,last_name,address_,dob,phone_no,pass_key,email_id) VALUES({},"{}","{}","{}","{}",{},"{}","{}")'.format(mem_id,f_name,l_name,add,dob,phone,password,email))
    mycon.commit()
    
    print('Welcome to the club',f_name,'!')
    wait = input('\n\n\n Press any key to continue....')

          
#To issue books by members

def issue_book():
    cans="y"
    while (cans=="y"):
        print('You can choose any genre from the following: ')
        genre_list=pd.Series(['','Fantasy','Self-Help','Historical Fiction','Autobiography','Psychology','Astrology','Detective Fiction','Children','Humour','Philosophy','Hindi Literature','Young Adult Fantasy'])
        print(genre_list)
        genre=input('Select a genre name\IN CASE SENSITIVE:')
        cur.execute('SELECT*FROM book_details WHERE genre = "%s";'%(genre))
        
        o=cur.fetchall()
        
        p=pd.DataFrame(o)
        print(p)

        book_choice = int(input('Enter accession no. of the book you would like to issue: '))
        
        cur.execute('SELECT * FROM book_details WHERE availability = "Available" AND acc_no = %s;'%(book_choice))
        u = cur.fetchall()
        #type conversion
        l=u.pop(0)
        b_name=l[1]
        a_name=l[2]
        m=pd.Series(l)
        
        print('Book details-------------')
        print(m)
        
        cur.execute('SELECT phone_no FROM member_details WHERE member_id = %s;'%(mid))
        so=cur.fetchall()
        #type conversion
        y=so.pop(0)
        z= y[0]
        pno=int(z)

        
        cur.execute('UPDATE book_details SET availability = "{}" WHERE acc_no = {}'.format("Unavailable",book_choice))
        mycon.commit()
                    
        cur.execute('INSERT INTO issued(m_id,book_acc_no,book_name,author,f_name,phone_no,status,Date_issued) VALUES({},{},"{}","{}","{}",{},"ISSUED",CURDATE())'.format(mid,book_choice,b_name,a_name,k,pno))
        mycon.commit()
        
        print('Your book has been successfully issued. Kindly note that your due date is 1 month from the date of issuement.')
        print('Thank you and have a good day!')
        proceed=input('Enter any key to proceed...')
        cans=input("Do you want to issue any more books?y/n ")


#To return books by members

def return_book():
    cans="y"
    while (cans=="y"):
        b_no=int(input('Enter accession no. of the book you would like to return: '))
        cur.execute('UPDATE book_details SET availability = "{}" WHERE acc_no = {}'.format("Available",b_no))#updating in book table
        mycon.commit()
        cur.execute('UPDATE issued SET status = "RETURNED" WHERE book_acc_no = {}'.format(b_no))#updating in issued table
        mycon.commit()
        
        cur.execute('UPDATE issued SET Date_returned = CURDATE() WHERE book_acc_no = {}'.format(b_no))#updating in issued table
        mycon.commit()
        print('Your book has been successfully returned.')
        print('Thank you and have a good day!')
        proceed=input('Enter any key to proceed...')
        cans=input("Do you want to return any more books?y/n ")
        



'''
The next set of functions are specifically the types which can view,insert or delete
both book and member records, as this is considered as sensitive information.
The following falls under the category of ADMIN RIGHTS.
Kindly note that Admin id:127 and passkey-Czennie
'''

#ADMIN RIGHTS

def book_exc():
    print('Editing/viewing library books-------------')
    cans="y"
    while (cans=="y"):
        chooce=input('What would you like to do? \n V-To view all library book records \n A-To add library book records \n D-To delete library book records \n  E-Exit \t >>>')
    

    
        if chooce=='V':
            cur.execute('SELECT*FROM book_details;')
            det=cur.fetchall()
            chnge=pd.DataFrame(det)
            print(chnge)
            
            
        
        elif chooce=='A':
        
            cur.execute('SELECT acc_no FROM book_details WHERE acc_no=(SELECT MAX(acc_no) FROM book_details);')
            chk1=cur.fetchall()
            chk2=chk1.pop(0)#type conversion
            chk3= chk2[0]
            last_num=int(chk3)
        
            print('Kindly note that the last book entry accession no. is: ',last_num)
            print('Format as follows eg. 2003,3005,etc.')
        
            b_no=int(input('Book Accession Number: '))
            b_name=input('Book name: ')
            a_name=input('Author name: ')
            
            print('Choose any genre from the following; if it doesnt exits...add it:')
            genre_list=pd.Series(['','Fantasy','Self-Help','Historical Fiction','Autobiography','Psychology','Astrology','Detective Fiction','Children','Humour','Philosophy','Hindi Literature','Young Adult Fantasy'])
            print(genre_list)
            
            genre=input('Book Genre(): ')
            ava=input('Available/Unavailable: ')
            lang=input('Book language: ')
            cur.execute('INSERT INTO book_details(acc_no,book_name,author_name,genre,availability,language) VALUES({},"{}","{}","{}","{}","{}")'.format(b_no,b_name,a_name,genre,ava,lang))
            mycon.commit()
        
            print('Book successfully added to the Official Neo Library Book Records.')
            
        
        elif chooce=='D':
        
            print('Take a look at the book list first.')
        
            cur.execute('SELECT acc_no,book_name FROM book_details;')
            info=cur.fetchall()
            info1=pd.DataFrame(info)
            print(info1)
        

            book_no=int(input('Book Accession number of the book to be DELETED: '))
            cur.execute('SELECT book_name FROM book_details WHERE acc_no=%s;'%(book_no))
            chk1=cur.fetchall()
            chk2=chk1.pop(0)#type conversion
            chk3= chk2[0]
            chk4=str(chk3)
            print('Are you sure you wanna delete---',chk4)
        

            conf=input('Enter C to confirm:')
            if conf=='C':
                cur.execute('DELETE FROM book_details WHERE acc_no = %s;'%(book_no))
                mycon.commit()

            print('Book successfully deleted from the Neo Library Records.')
            
        
            
        elif chooce=='E':
            exit_func()
        
        else:
            print('Invalid input! Try again.')
            pass

        cans=input("Do you want to continue or not?y/n ")
    
        



        

def member_exc():
    print('Editing/viewing Library Member Records-------------')
    cans="y"
    while (cans=="y"):
        chooce=input('What would you like to do? \n V-To view all library member records \n A-To add a new member record \n D-To delete a member record \n  E-Exit \t >>>')

        if chooce=='V':
            cur.execute('SELECT*FROM member_details;')
            det=cur.fetchall()
            chnge=pd.DataFrame(det)
            print(chnge)
        
        elif chooce=='A':
        
            cur.execute('SELECT member_id FROM member_details WHERE member_id=(SELECT MAX(member_id) FROM member_details);')
            chk1=cur.fetchall()
            chk2=chk1.pop(0)#type conversion
            chk3= chk2[0]
            last_num=int(chk3)
        
            print('Choose a unique id greater than ',last_num)
        
            check_id()
        
            mem_id=input('Confirm your id(in digits:')
            f_name = input('Enter first name: ')
            l_name = input('Enter last name: ')
            add = input('Enter address: ')
            dob = input('Date of Birth (YYYY-MM-DD): ')
            phone = input('Contact number: ')
            password=input('Set password: ')
            email=input('Enter your email id:')

            cur.execute('INSERT INTO member_details(member_id,first_name,last_name,address_,dob,phone_no,pass_key,email_id) VALUES({},"{}","{}","{}","{}",{},"{}","{}")'.format(mem_id,f_name,l_name,add,dob,phone,password,email))
            mycon.commit()
            print('New member successfully added to the Official Neo Library Member Records.')
        
        elif chooce=='D':
        
            print('Take a look at the existing member records first.')
        
            cur.execute('SELECT member_id,first_name,last_name FROM member_details;')
            info=cur.fetchall()
            info1=pd.DataFrame(info)
            print(info1)
        

            mem_no=int(input('Member id number of the chosen record to be DELETED: '))
            cur.execute('SELECT first_name FROM member_details WHERE member_id=%s;'%(mem_no))
            chk1=cur.fetchall()
            chk2=chk1.pop(0)#type conversion
            chk3= chk2[0]
            chk4=str(chk3)
            print('Are you sure you wanna delete the records of---',chk4)
            
            conf=input('Enter C to confirm:')
            if conf=='C':
                cur.execute('DELETE FROM member_details WHERE member_id = %s;'%(mem_no))
                mycon.commit()
                print('Member records of the chosen member successfully deleted from the Neo Library Records.')
            
                
        elif chooce=='E':
            exit_func()
            
        else:
            print('Invalid input! Try again.')
            pass

        cans=input("Do you want to continue or not?y/n ")
            

#Admin Menu-Modify books and library member records
def menu3():
    print('Welcome Admin! Good to see you!')
    choose=input('What would you like to do? \n B-To edit/view all library books \n M-To edit/view library member details \n E-Exit \t >>>')
    if choose=='B':
        book_exc()
    elif choose=='M':
        member_exc()
    elif choose=='E':
        exit_func()
    else:
        print('Invalid input. Try again.')
        pass
        
        
#DISPLAY MENU 2 - Issue, Return, Exit
def menu2():
    
    print('\nMENU\n')
    choice=input('\tSo what would you like to do today? \t I-Issue a book \t R-Return a book \t E-Exit \t >>>')

    if choice=="I":
        issue_book()

    elif choice=="R":
        return_book()

    elif choice == 'E':
        exit_func()
            
    

#Login function has been added here for a reason, as in case of admin logins---startmenu1 to login to menu3. 
def login():
    correct=False
    while not correct:
        global mid
        mid=int(input('Login ID: '))
        pwd=input('Passkey: ')
        
        cur.execute('SELECT member_id FROM member_details WHERE pass_key="%s" AND member_id = %s;'%(pwd,mid))
        a=cur.fetchall()
        c=a.pop(0)#type conversion
        d= c[0]
        u=cur.execute('SELECT first_name FROM member_details WHERE pass_key="%s" AND member_id = %s;'%(pwd,mid))
        n=cur.fetchall()
        l=n.pop(0)#type conversion
        r=l[0]
        global k
        k=str(r)

        #ADMIN Login
        if mid==127 and pwd=='Czennie':
            menu3()
        
        elif d==mid:
            correct=True
            print('Welcome back',k,'!')
            menu2()
            break
        
        else:
            print('Try again!')
            pass
    

#DISPLAY MENU1 - Login, Register, Exit
def startmenu1():
    print("    Welcome to the Neo Culture Library    ")
    entry = input(" 1. Login - L \n2. Register - R \n3. Exit - E \n\n ^_^ --- ")

    if entry == 'L':
        login()
        

    elif entry == 'R':
        register()
        menu2()

    elif entry == 'E':
        exit_func()
                      
    
startmenu1() 

    




