# lib/cli.py

from helpers import (
    exit_program,
    list_users,
    update_user,
    find_by_username,
    create_user,
    delete_user,
    list_playlists,
    create_playlist,
    delete_playlist,
    update_playlist,
    show_playlists,
    show_songs_from_playlist
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
        print("5. Find user by username")
        print("6. Show playlists that belong to user")
        choice = input("\nEnter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            list_users()
        elif choice == "2":
            update_user()
        elif choice == "3":
            create_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            find_by_username()
        elif choice == '6':
            show_playlists()
        else:
            print("Invalid choice. Please try again.")

def playlist_menu():
    while True:
        print("\nPlaylist Menu:")
        print("0. Go back to main menu")
        print("1. View existing playlists")
        print("2. Create a new playlist")
        print("3. Update playlist metadata")
        print("4. Delete a playlist")
        print("5. Show songs in a playlist")
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            list_playlists()
        elif choice == "2":
            create_playlist()
        elif choice == "3":
            update_playlist()
        elif choice == "4":
            delete_playlist()
        elif choice == "5":
            show_songs_from_playlist()
        else:
            print("Invalid choice. Please try again.")
            

def song_menu():
    while True:
        print("\nSong Menu:")
        print("0. Go back to main menu")
        print("1. View all songs")
        print("2. Create a new song")
        print("3. Update a song")
        print("4. Delete a song")
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
            exit_program()
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
