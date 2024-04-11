# lib/helpers.py

from models.user import User
from models.playlist import Playlist

#User helper functions

def list_users():
    print("\nListing users...")
    
    #Gets all of users from the users table
    users = User.get_all()
    for user in users:
        print(user)
    
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
            print("\nUpdating User...")
            user.username = username
            user.email = email
            user.age = age
            user.update()
            print("User updated")
            print(user)
    else:
        print(f'User with ID {user_id} does not exist. ID must be an integer')
        
def find_by_username():
    username = input("\nEnter username: ")
    if isinstance(username, str) and len(username) > 0:
        found_user = User.find_by_username(username)
        if found_user:
            print("\nUser found")
            print(found_user)
        else:
            print(f'\nUsername {username} does not exist')
            
    else:
        print("Invalid username. Username must be a string.")
        return
    
def create_user():
    import re
    
    username = input("\nEnter username: ")
    #Validates that the username entered is a string and > 0
    if isinstance(username, str) and len(username) > 0:
            valid_username = True
    else:
        print("Invalid username. Username must be a string.")
        valid_username = False
        return
        
    email = input("\nEnter email: ")    
    #Validates that the email entered is of the correct form
    email_pattern = r'^\S+@\S+\.\S+$'
    if isinstance(email, str) and re.match(email_pattern, email) is not None:
            valid_email = True
    else:
        print("Invalid email.")
        valid_email = False
        return
        
    age = input("\nEnter user's age: ") 
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
    
    if valid_age and valid_email and valid_username:
        print("\nCreating User...")
        newUser = User.create(username, email, age)
        print("New User created.")
        print(newUser)
    
def delete_user():
    user_id = input("\nEnter User Id of user to be deleted: ")
    
    deleted_user = User.find_by_id(user_id) 
    
    print("\nDeleting User...")
    deleted_user.delete()
    print(f'User ID {user_id} has been deleted')   
    
    
#Playlist helper functions

def list_playlists():
    print("\nListings playlists...")
    playlists = Playlist.get_all()    
    
    for playlist in playlists:
        print(playlist)
    
    
def exit_program():
    print("\nGoodbye!")
    exit()
