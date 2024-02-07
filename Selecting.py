import sqlite3

#connecting to database
conn = sqlite3.connect('MiniEpic.db')
cursor = conn.cursor()


######################################################################################################################################################################################
#Login page
######################################################################################################################################################################################
count = 0

#function to verify user credentials
def validate_user(username, password):
    global name
    cursor.execute("SELECT UserID FROM login WHERE username=? AND password=?", (username, password)) #checks login table for provided username and password
    row = cursor.fetchone() #returns first row of database

    if row is not None:
        return True
    else:
        return False
    
def login(username, password):

    if validate_user(username, password): #checks if username and password are valid

        cursor.execute("SELECT UserID FROM login WHERE Username=? AND Password=?", (username, password)) #checks login table for provided username and password
        row = cursor.fetchone() #returns first row of database
        user_id = int(row[0]) #gets user ID from database
        cursor.execute("SELECT Name FROM Users WHERE UserID=?", (user_id,)) #checks Users table for UserID
        row = cursor.fetchone() #returns first row of database
        name = row[0] #assigns name from database to name variable

        print("Login successful")
        print("Welcome to ISEagles", name)
        verify_role(user_id) #returns to verify role screen

    else:
        print("Invalid username or password")
        print("Please try again")

    

def create_account(username, password, name, surname, email, phone):
    cursor.execute("INSERT INTO Users (Name, Surname, Email) VALUES (?,?,?)", (name, surname, email)) #creates new record in Users table with provided data
    conn.commit() #commits attributes to database

    cursor.execute("SELECT UserID FROM Users WHERE Name=? AND Surname=? AND Email=?", (name, surname, email)) #checks Users table for provided name, surname and email
    row = cursor.fetchone() #returns first row of database
    user_id = int(row[0]) #gets user ID from database

    cursor.execute("INSERT INTO login (username, password) VALUES (?,?)", (username, password)) #creates new record in login table with provided username and password
    cursor.execute("INSERT INTO PhoneNumber (UserID, PhoneNumber) VALUES (?,?)", (user_id, phone)) #creates new record in PhoneNumber table with user ID and provided phone number
    conn.commit() #commits attributes to database


def signup(username, password, name, surname, email, phone):

    confirmation = input("Please confirm your details(Confirm(C)/Deny(D)): ") #prompts user to confirm details++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if confirmation == "C":
        create_account(username, password, name, surname, email, phone)
    elif confirmation == "D":
        signup()
    else:
        print("Invalid option")
        signup()

    print("Signup successful")
    print("Please Login", name)
  

def verify_role(user_id):
    cursor.execute("SELECT Role, ApprovalStatus FROM Users WHERE UserID=?", (user_id,)) #checks role of user from Users table
    row = cursor.fetchone() #returns first row of database
    role = row[0]
    approval_status = row[1]

    if approval_status != "approved":
        print("You're approval status is", approval_status)
   
   
    if role == "ADMIN":
        print("You are an Admin")######################################################Admin page

    elif role == "COORDINATOR":
        print("You are a Coordinator")######################################################Coordinator page
    
    elif role == "STUDENT":
        print("You are a Student")######################################################Student page
    
    else:
        print("ERROR: Invalid role")




##########################################################################################################################
#                                                    START OF PROGRAM                                                    #
##########################################################################################################################
#Login
username = input("Enter username:")
password = input("Enter password:")

login(username, password)


#Signup
#username = input("Enter username:")
#password = input("Enter password:")
#name = input("Enter name:")
#surname = input("Enter surname:")
#email = input("Enter email:")
#phone = input("Enter phone:")

#signup(username, password, name, surname, email, phone)

conn.close()#closes connection to database
