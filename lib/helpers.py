# lib/helpers.py

from models.user import User

def list_users():
    print("\nListing users...")
    
    #Gets all of users from the users table
    users = User.get_all()
    for user in users:
        print(f'User ID: {user.id} Username: {user.username} Email: {user.email} Age: {user.age}')
    
def update_user():
    import re
    
    user_id = input("\nEnter User ID: ")
    user = User.find_by_id(user_id)
    #Validatest that the user exists in the users table
    if user:
        print("User Exists")
        
        username = input("\nEnter new username: ") 
        #Validates that the username entered is a string and > 0
        if isinstance(username, str) and len(username) > 0:
            valid_username = True
        else:
            print("Invalid username. Username must be a string.")
            valid_username = False
            return
        
        email = input("\nEnter new email: ")
        email_pattern = r'^\S+@\S+\.\S+$'
        #Validates that the email entered is of the correct form
        if isinstance(email, str) and re.match(email_pattern, email) is not None:
            valid_email = True
        else:
            print("Invalid email.")
            valid_email = False
            return
            
        age = input("\nEnter new age: ")
        #Validates that the age entered is an integer
        try:
            age = int(age)
        except ValueError:
            print("Age must be an integer")
        #Validates that the age entered is greater than or equal to 5
        if age >= 5:
            valid_age = True
        else:
            print("Age must be greater than or equal to 5")
            valid_age = False
            return
            
        #If all inputs are valid updates the dictionary user object and updates the row in the users table
        if valid_username and valid_email and valid_age:
            user.username = username
            user.email = email
            user.age = age
            user.update()
    else:
        print(f'User with ID {user_id} does not exist. ID must be an integer')
        
def find_by_username():
    username = input("\nEnter username: ")
    if isinstance(username, str) and len(username) > 0:
        found_user = User.find_by_username(username)
        if found_user:
            print("\nUser found\n")
            print(f'User ID: {found_user.id} Username: {found_user.username} Email: {found_user.email} Age: {found_user.age}')
        else:
            print(f'\nUsername {username} does not exist')
            
    else:
        print("Invalid username. Username must be a string.")
        return
    
def create_user():
    username = input("\nEnter username: ")
    email = input("\nEnter email: ")
    age = input("\nEnter user's age: ")
    
    
    
def exit_program():
    print("Goodbye!")
    exit()
