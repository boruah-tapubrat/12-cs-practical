import mysql.connector as msc
db1= None
def connect(): 
    global db1
    db1=msc.connect(host="localhost",user="root",password="root",database="project")
      
def login():
    global db1
    print("-"*40)
    print("\t Library Mangement System")
    print("-"*40)
    print("\t LOGIN")

    user=input("Enter username: ")
    passw=input("Enter password: ")
    q1='Select * from user_password where username = %s and password = %s'
    val=(user,passw)
    c1=db1.cursor()
    c1.execute(q1,val)
    res=c1.fetchall()
    print("-"*50)
    if len(res) == 0:
        print("INVALD username or password")
        print("-"*50)
        return False
    else:
        print("Connection Established")
        print("Access Granted!!!!")
        return True

def Signup():
    print("-"*40)
    print("\t SIGNUP")
    print("-"*40)
    user=input("Enter username: ")
    password=input("Enter password(give a strong password): ")
    q1="insert into user_password values(%s,%s)"
    val=(user,password)
    c1=db1.cursor()
    c1.execute(q1,val)
    db1.commit()
    print("You are signed up!!!")

def Add_member():
    print("-"*50)
    print("\t Adding a member")
    print("-"*50)
    while True:
        Mid=int(input("Enter Member Id: "))
        Name=input("Enter Member Name: ")
        Email=input("Enter Member Email: ")
        Phone=int(input("Enter Member Phone Number: "))
        q="insert into Member values(%s,%s,%s,%s)"
        val=(Mid,Name,Email,Phone)
        c1=db1.cursor()
        c1.execute(q,val)
        db1.commit()
        print("MEMBER ADDED SUCCESSFULLY!!!")
        print("-"*50)
        ch=input("Do you want to add more?(Y/N): ")
        if ch.lower() =="y":
            continue
        elif ch.lower() =="n":
            break
        else:
            print("invalid choice!!!")

def show_member():
    print("-"*50)
    print("\t Members Details ")
    print("-"*50)
    q="Select * from member"
    c1=db1.cursor()
    c1.execute(q)
    res=c1.fetchall()
    print("ID  NAME  EMAIL  PHONE_NO")
    for i in res:
        print(i[0],"",i[1],"",i[2],"",i[3])

def del_member():
    print("-"*50)
    c1=db1.cursor()
    while True:
        ch=input("For deleting a member, you have to give either the name or ID choose(type 'N'FOR Name/ 'i' FOR Id): ")
        if ch.lower()=="n":
            Del = input("Enter the name of the member you want to delete: ")
            q1="Delete from member where name ='{0}'".format(Del)
            c1.execute(q1)
            res="{0} is Successfully Deleted".format(Del)
            print(res)
        elif ch.lower()=="i":
            Del2=int(input("Enter the ID of the member you want to delete: "))
            q2="Delete from member where Mid ={0}".format(Del2)
            c1.execute(q2)
            res2="{0} is Successfully Deleted".format(Del2)
            print(res2)

def show_books():
    print("-"*50)
    print("\t Books Details ")
    print("-"*50)
    q="Select * from books"
    c1=db1.cursor()
    c1.execute(q)
    res=c1.fetchall()
    print("BOOKID  Title  Author  Publisher  Cost")
    for i in res:
        print(i[0],"",i[1],"",i[2],"",i[3],"",i[4])

def Add_Books():
    print("-"*50)
    print("\t Adding a Book")
    print("-"*50)
    while True:
        Bookid=int(input("Enter BOOK Id: "))
        Title=input("Enter Book Title: ")
        Author=input("Enter Author Name: ")
        Publisher=input("Enter Publisher: ")
        Cost=int(input("Enter Cost of the book: "))
        q="insert into books values(%s,%s,%s,%s,%s)"
        val=(Bookid,Title,Author,Publisher,Cost)
        c1=db1.cursor()
        c1.execute(q,val)
        db1.commit()
        print("BOOK ADDED SUCCESSFULLY!!!")
        print("-"*50)
        ch=input("Do you want to add more?(Y/N): ")
        if ch.lower() =="y":
            continue
        elif ch.lower() =="n":
            break
        else:
            print("invalid choice!!!")
def Delete_Books():
    print("-"*50)
    print("\t Deleting a Book")
    print("-"*50)
    c1=db1.cursor()
    while True:
        ch=input("For deleting a Book, you have to give either the BookTitle or BookID choose(type 'T'FOR BookName/ 'i' FOR BookId): ")
        if ch.lower()=="t":
            Del = input("Enter the Title of the Book you want to delete: ")
            q1="Delete from Books where title ='{0}'".format(Del)
            c1.execute(q1)
            res="{0} is Successfully Deleted".format(Del)
            print(res)
        elif ch.lower()=="i":
            Del2=int(input("Enter the BookID of the Book you want to delete: "))
            q2="Delete from Books where bookid ={0}".format(Del2)
            c1.execute(q2)
            res2="{0} is Successfully Deleted".format(Del2)
            print(res2)
            
def Issue_Book():
    c1=db1.cursor()  
    print("-"*50)
    print("\t Issue a Book")
    print("-"*50)
    while True:
        mid = int(input("Enter Member ID: "))
        bid = int(input("Enter Book ID: "))
        doi = input("Enter Date of Issue (YYYY-MM-DD): ")

        # Check if the book is available
        check_query = "SELECT * FROM books WHERE bookid = %s"
        check_values = (bid,)
        c1.execute(check_query, check_values)
        book_available = c1.fetchone()

        if not book_available:
            print("Book not available for issue.")
            continue

        # Check if the book is already issued
        check_issue_query = "SELECT * FROM issue WHERE bid = %s AND return_date IS NULL"
        check_issue_values = (bid,)
        c1.execute(check_issue_query, check_issue_values)
        already_issued = c1.fetchone()

        if already_issued:
            print("Book already issued to another member.")
            continue

        # Issue the book
        issue_query = "INSERT INTO issue (mid, bid, doi) VALUES (%s, %s, %s)"
        issue_values = (mid, bid, doi)
        c1.execute(issue_query, issue_values)
        db1.commit()
        print("Book issued successfully!")
        break
def Show_Issued_Books():
     print("-"*50)
     print("\t Issued Books Details ")
     print("-"*50)
     q="Select * from issue"
     c1=db1.cursor()
     c1.execute(q)
     res=c1.fetchall()
     print("mid bid doi")
     for i in res:
        print(i[0],"",i[1],"",i[2],"",i[3])
def Return_Book():
    c1=db1.cursor()
    print("-"*50)
    print("\t Return a Book")
    print("-"*50)
    while True:
        mid = int(input("Enter Member ID: "))
        bid = int(input("Enter Book ID: "))
        return_date = input("Enter Date of Return (YYYY-MM-DD): ")
  
        check_query = "SELECT * FROM issue WHERE mid = %s AND bid = %s AND return_date IS NULL"
        check_values = (mid, bid)
        c1.execute(check_query, check_values)
        issued_book = c1.fetchone()

        if not issued_book:
            print("Book not issued to the member or already returned.")
            continue

        return_query = "UPDATE issue SET return_date = %s WHERE mid = %s AND bid = %s"
        return_values = (return_date, mid, bid)
        c1.execute(return_query, return_values)
        db1.commit()
        print("Book returned successfully!")
        break
def Show_Returned_Books():
    print("-"*50)
    print("\t Returned Books Details ")
    print("-"*50)
    q="Select * from books"
    c1=db1.cursor()
    c1.execute(q)
    res=c1.fetchall()
    print("bid title author publisher cost")
    for i in res:
        print(i[0],"",i[1],"",i[2],"",i[3],"",i[4],"",i[5])

connect()
print("-"*40)
print("\t Library Mangement System")
print("-"*40)
print("\t Choose one Option")
print("1.Login")
print("2.Signup")
print("3.Quit.")
while True:
    ch1=int(input("Enter your choice: "))
    if ch1==1:
        if login():
            while True:
                print("-"*50)
                print("\t CHOOSE AN OPERATION!!")
                print("-"*50)
                print("1.Add member.")
                print("2.Show all members.")
                print("3.Delete a member")
                print("4.Show all Books")
                print("5.Add Books")
                print("6.Delete an Existing Book")
                print("7.Issue a Book")
                print("8.Show Issued Books")
                print("9.Return a Book")
                print("10.Show Returned Books")
                print("11.Quit.")
                ch=int(input("Enter your choice: "))
                if ch==1:
                    Add_member()
                elif ch==2:
                    show_member()
                elif ch==3:
                    del_member()
                elif ch==4:
                    show_books()
                elif ch==5:
                    Add_Books()
                elif ch==6:
                    Delete_Books()
                elif ch==7:
                    Issue_Book()
                elif ch==8:
                    Show_Issued_Books()
                elif ch==9:
                    Return_Book()
                elif ch==10:
                    Show_Returned_Books()
                elif ch ==11:
                    break
                else:
                    print("Invalid choice")
                    continue
    elif ch1==2:
        Signup()

    elif ch==3:
        break

    else:
        print("INVALID CHOICE!!!")
        continue

db1.close()




