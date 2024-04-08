# lib/cli.py

from helpers import (
    exit_program,
    list_users,
    update_user
)


def main_menu():
    print("\nMain Menu:")
    print("0. Exit the program")
    print("1. User Menu")
    print("2. Playlist Menu")
    print("3. Song Menu")
    
def user_menu():
    while True:
        print("\nUser Menu:")
        print("0. Go back to main menu")
        print("1. List users")
        print("2. Update user information")
        print("3. Create user")
        print("4. Delete User")
        print("5. Find user by name")
        choice = input("\nEnter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            list_users()
        elif choice == "2":
            update_user()
        elif choice == "3":
            print("Creating user")
        elif choice == "4":
            print("Deleting user")
        elif choice == "5":
            print("Finding user by name")
        else:
            print("Invalid choice. Please try again.")

def playlist_menu():
    while True:
        print("\nPlaylist Menu:")
        print("0. Go back to main menu")
        print("1. Create a new playlist")
        print("2. View existing playlists")
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            print("Creating a new playlist...")
            # Implement create new playlist functionality
        elif choice == "2":
            print("Viewing existing playlists...")
            # Implement view existing playlists functionality
        else:
            print("Invalid choice. Please try again.")
            

def song_menu():
    while True:
        print("\nSong Menu:")
        print("0. Go back to main menu")
        print("1. Add a new song")
        print("2. View songs")
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            print("Adding a new song...")
            # Implement add new song functionality
        elif choice == "2":
            print("Viewing songs...")
            # Implement view songs functionality
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1":
            user_menu()
        elif choice == "2":
            playlist_menu()
        elif choice == "3":
            song_menu()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
