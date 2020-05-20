def login():

    username = input("Please enter your username to login:\n")
    password = input("Please enter your password to login:\n")

  
    for line in open("user.txt", "r").readlines(): #Read the lines
        login_info = line.split(',') #Slipt on the space, and store the results in a list of two strings

        if username in login_info[0] and password in login_info[1]:
            print("You are login.")
            print("\nPlease select one of the following options: \n r - register user  :Activation key -'r()' \n a - add task  :Activation key -'a()' \n va - view all tasks  :Activation key -'va()' \n vm - view all my tasks  :Activation key -'vm()' \n gr - generate reports  :Activation key -'gr()' \n e - exist  :Activation key -'e()'")
            print("\nNB: To initiate desired fuction, please type what is in the quotation marks of activation key eg: a() ")

        while username not in login_info[0] and password in login_info[1]: #Prompt if password is incorrect
            print("Your username is incorrect.")
            username = input("Please enter a valid username:\n")

        while username in login_info[0] and password not in login_info[1]: #Prompt if password is incorrect
            print("Your username is correct but your password is incorrect.")
            password = input("Please enter a valid password:\n")
            
activation = input("Would you like to login (Yes/No): ")
if activation == "Yes":
    login()
else:
    print("Do have a pleasant day further")




def r():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    con_password = input("Please confirm the above password: ")

    if password == con_password:
        file = open("user.txt", "a") #Not w, a for add
        file.write(username)
        file.write(", ")
        file.write(password)
        file.write("\n")
        file.close()

    while password != con_password: 
        print("Incorrect, confirmed password")
        con_password = input("Please confirm the above password: ")

    
def a():
    username_for_task = input("Please enter the username of person to whom task is for: ")
    task_t = input("Please enter the title of the task: ")
    task_des = input("Please enter a description of the task: ")
    Assigned_date = input("Please confirm the date when the task was assigned: ")
    due_date = input("Please confirm the due date of the task: ")
    task_completion = input("Please confirm if the task is complete (Yes or No): ")

    file = open("tasks.txt", "a") #Not w, a for add
    file.write(username_for_task)
    file.write(", ")
    file.write(task_t)
    file.write(", ")
    file.write(task_des)
    file.write(", ")
    file.write(Assigned_date)
    file.write(", ")
    file.write(due_date)
    file.write(", ")
    file.write(task_completion)
    file.write("\n")
    file.close()

def va():
    with open('tasks.txt', 'r+') as task: # Open the file again!
        for line in task:
            line = line.split(',')
            print("Username of person task is assigned:" + line[0] + "\nTitle of task:" +line[1]+ "\nDescription of the task:" +line[2]+ "\nDate task assigned:" +line[3]+ "\nDue date of the task:" +line[4]+ "\nTask complete:" +line[5])



def vm():
    with open('tasks.txt', 'r+') as task: # Open the file again!

        user_1 = input("Please input your username again: ")
        
        for line in task:
            line = line.split(',')
            if user_1 == line[0]:
                print("Username of person task is assigned:" + line[0] + "\nTitle of task:" +line[1]+ "\nDescription of the task:" +line[2]+ "\nDate task assigned:" +line[3]+ "\nDue date of the task:" +line[4]+ "\nTask complete:" +line[5])


                    
def e():
    x = input("Please confirm if you wish to exit this program (Yes/No): ")

    if x == "Yes":
        print("Enjoy your day!")

    else:
        print("You are still logged in")
