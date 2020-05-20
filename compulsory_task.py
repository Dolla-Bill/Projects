# Importing file that stores the functions ===================================
from system_functions import *
# Variables ==================================================================
close = False
login = False
user_names = ""
user_passwords = ""
logged_in = False
# Handles all user options ===================================================
while close == False:
    # Logging in ================================================
    while logged_in == False:
        users = open("user.txt","r")
        user_names = []
        user_passwords = []
        for line in users:
            temp = line.strip()
            temp = temp.split(", ")
            user_names.append(temp[0])
            user_passwords.append(temp[1])
        users.close()
        print("Would you like to login?")
        print("Yes - Login")
        print("No - Exit")
        choice = input(": ")
        if choice == "Yes":
            while logged_in == False:
                username = input("Username: ")
                password = input("Password: ")
                if username not in user_names:
                    print("\nThe username you entered does not exist")
                elif password not in user_passwords:
                    print("\nThe password you entered is inccorect")
                else:
                    logged_in = True
        elif choice == "No":
            print("Thank you for using our task manager system, do have a pleasant day further!")
            close = True
            break
    # Logged in =================================================
    while logged_in == True:
    # Option menu ===============================================
        print("\nPlease select one of the following options: ")
        if username == "admin":
            print("r  - Register user")
        print("a  - Add task")
        print("va - View  all tasks")
        print("vm - View my tasks")
        if username == "admin":
            print("ds - Display statistics")
            print("gr - Generate reports")
        print("b  - Back to login")
        option = input(": ")
        # Handles Options =======================================
        # Registers new user =========================
        if option == "r" and username == "admin":
            reg_user(user_names)
        # Adds task ==================================
        if option == "a":
            add_task(user_names)
        # All tasks output ===========================
        if option == "va":
            view_all()
        # User's tasks output ========================
        if option == "vm":
            view_mine(username,user_names)
        # Displays stats =============================
        if option == "ds" and username == "admin":
            show_stats()
        # Generates reports ==========================
        if option == "gr" and username == "admin":
            generate_report()
        # Exits Menu =================================
        if option == "b":
            logged_in = False
        # ====================================================================
