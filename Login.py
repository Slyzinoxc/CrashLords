import pyrebase

firebaseConfig = {
               'apiKey': "AIzaSyDD7nMvbDIzYNvQ_KLTDauSyhSFJeQTHIk",
               'authDomain': "crash-projekt.firebaseapp.com",
               'databaseURL': "https://crash-projekt-default-rtdb.asia-southeast1.firebasedatabase.app",
               'projectId': "crash-projekt",
               'storageBucket': "crash-projekt.firebasestorage.app",
               'messagingSenderId': "188763631253",
               'appId': "1:188763631253:web:0c3274e3c9b797b26e359c",
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email=email,password=password)
        print("Successfully logged in!")
    except:
        print("Invalid email or password")
    return

def signup():
    print ("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
       user = auth.create_user_with_email_and_password(email=email, password=password) 
       print("Account Created Successfullyy")   
    except:
        print("Email already exist")
    return

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()
