# lib/helpers.py

from models.user import User

def list_users():
    print("\nListing users...")
    
    users = User.get_all()
    for user in users:
        print(f'User ID: {user.id} Username: {user.username} Email: {user.email} Age: {user.age}')
    
def update_user():
    import re
    
    user_id = input("\nEnter User ID: ")
    user = User.find_by_id(user_id)
    if user:
        print("User Exists")
        
        username = input("\nEnter new username: ") 
        if isinstance(username, str) and len(username) > 0:
            valid_username = True
        else:
            print("Invalid username. Username must be a string.")
            valid_username = False
            return
        
        email = input("\nEnter new email: ")
        email_pattern = r'^\S+@\S+\.\S+$'
        if isinstance(email, str) and re.match(email_pattern, email) is not None:
            valid_email = True
        else:
            print("Invalid email.")
            valid_email = False
            return
            
        age = input("\nEnter new age: ")
        try:
            age = int(age)
        except ValueError:
            print("Age must be an integer")
        if age >= 5:
            valid_age = True
        else:
            print("Age must be greater than or equal to 5")
            valid_age = False
            return
            
        #Update the row in the table corresponding to the inputed user ID
        if valid_username and valid_email and valid_age:
            user.username = username
            user.email = email
            user.age = age
            user.update()
    else:
        print(f'User with ID {user_id} does not exist. ID must be an integer')
        
    
    
def exit_program():
    print("Goodbye!")
    exit()
