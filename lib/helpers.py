# lib/helpers.py

from models.user import User
from models.playlist import Playlist
from models.song import Song

#User helper functions

def list_users():
    """Lists all the users"""
    print("\nListing users...")
    
    #Gets all of users from the users table
    users = User.get_all()
    for user in users:
        print(user)
    
def update_user():
    """Updates a user by id"""
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
    """Finds user by username"""
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
    """Creates a user"""
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
    """Deletes a user by id"""
    user_id = input("\nEnter User Id of user to be deleted: ")
    
    user = User.find_by_id(user_id) 
    if  user:
        print("\nDeleting user...")
        user.delete()
        print(f'\nUser with id {user_id} deleted')
    else:
        print("\nInvalid id. Id must be an integer and exist in the database")
    
      
    
    
#Playlist helper functions

def list_playlists():
    """Prints all the playlists in the table"""
    print("\nListings playlists...")
    playlists = Playlist.get_all()    
    
    for playlist in playlists:
        print(playlist)
        
def create_playlist():
    """Creates a new playlist given input values"""
    title = input("\nEnter title of new playlist: ")
    #Validates that the title entered is a string and > 0
    if isinstance(title, str) and len(title) > 0:
            valid_title = True
    else:
        print("Invalid title. Title must be a string.")
        valid_title = False
        return
    
    description = input("\nEnter a brief description of the playlist: ")
    #Validates that the username entered is a string and > 0
    if isinstance(description, str) and len(description) > 0:
            valid_description = True
    else:
        print("Invalid description. Description must be a string.")
        valid_description = False
        return
    
    username = input("\nEnter the username that the playlist belongs to: ")
    user = User.find_by_username(username)
    if user:
            valid_username = True
    else:
        print("Invalid username. Username must exist.")
        valid_username = False
        return
    
    if valid_title and valid_description and valid_username:
        print("\nCreating new playlist...")
        new_playlist = Playlist.create(title, description, user.id)
        print("\nPlaylist created")
        print(new_playlist)
        
def delete_playlist():
    """Deletes a playlist by id"""
    playlist_id = input("\nEnter id of playlist to be deleted: ")
    playlist = Playlist.find_by_id(playlist_id)
    if  playlist:
        print("\nDeleting playlist...")
        playlist.delete()
        print(f'\nPlaylist with id {playlist_id} deleted')
    else:
        print("\nInvalid id. Id must be an integer and exist in the database")
        
def update_playlist():
    """Updates a playlist by the given id"""
    playlist_id = input("\nEnter the id of the playlist to be updated: ")
    playlist = Playlist.find_by_id(playlist_id)
    if playlist:
        
        title = input("\nEnter new title for the playlist: ")
        if isinstance(title, str) and len(title) > 0:
            valid_title = True
        else:
            valid_title = False
            print("\nTitle must be a string and have a length longer than 0")
            return 
        
        description = input("\nEnter a new description of the playlist: ")
        if isinstance(description, str) and len(title) > 0:
            valid_description = True
        else:
            valid_description = False
            print("\Description must be a string and have a length longer than 0")
            return
        
        user_id = input("\nEnter the User id that the playlist will belong to: ")
        user = User.find_by_id(user_id)
        if user:
            valid_user = True
        else:
            valid_user = False
            print("\nUser Id must be an integer and exist in the database")
            return
        
        if valid_user and valid_description and valid_title:
            print("\nUpdating user...")
            #Changes user_id from a string to an id
            user_id = int(user_id)
            playlist.title = title
            playlist.description = description
            playlist.user_id = user_id
            playlist.update()
            print("\nUser updated")
            print(playlist)
    else:
        print("\nPlaylist Id must be an integer and exist in the database")
        
def show_playlists():
    """Shows all the playlists that belong to a specific user"""
    username = input("\nEnter username to view their playlists: ")
    user = User.find_by_username(username)
    if user:
        playlists = Playlist.get_all()
        user_playlists = [ playlist for playlist in playlists if playlist.user_id == user.id ]
        if user_playlists:
            print(f"\n{user.username}'s playlists: ")
            for playlist in user_playlists:
                print(playlist)
        else:
            print(f'\n{user.username} does not have any playlists')
            return
    else:
        print("\nInvalid username. User must exist in the database")
        return
    
def show_songs_from_playlist():
    """Shows all songs from a given playlist"""
    playlist_id = input("\nEnter the id of the playlist: ")
    playlist = Playlist.find_by_id(playlist_id)
    if playlist:
        songs = Song.get_all()
        playlist_songs = [ song for song in songs if song.playlist_id == playlist.id ]
        print(f'\nListing songs in {playlist.title} playlist: ')
        for song in playlist_songs:
            print(song)
    else:
        print("\nPlaylist id must be an integer and must exist in the database")
        
def find_playlist_by_id():
    """Finds playlist by id"""
    playlist_id = input("\nEnter the id of the playlist: ")
    playlist = Playlist.find_by_id(playlist_id)
    if playlist:
        print("\nFinding playlist...")
        print("\nPlaylist found")
        print(playlist)
    else:
        print("\nInvalid id. Playlist must exist in the database")
        
        
#Song helper functions        
        
def list_songs():
    """Lists all songs"""
    print("\nListing songs...")
    songs = Song.get_all()
    if songs:
        for song in songs:
            print(song)
    else:
        print("\nThere are no songs in the database")
        
def create_song():
    """Creates new song given input values"""
    title = input("\nEnter title of new song: ")
    #Validates that the title entered is a string and > 0
    if isinstance(title, str) and len(title) > 0:
            valid_title = True
    else:
        print("\nInvalid title. Title must be a string.")
        valid_title = False
        return
    
    genres= ['pop','dance','rock','r&b','country', 'hip hop']
    genre = input("\nEnter genre of new song: ")
    genre_lower = genre.lower()
    #Validates that the genre entered is a string and > 0
    if isinstance(genre_lower, str) and len(genre_lower) >= 3 and genre_lower in genres:
            valid_genre = True
    else:
        print("\nInvalid genre. Genre must be pop, dance, rock, r&b, country, or hip hop")
        valid_genre = False
        return
    
    duration = input("\nEnter the duration of the song in seconds: ") 
    #Validates that the age entered is an integer
    try:
        duration = int(duration)
    except ValueError:
        print("\nDuration must be an integer")
        return
    #Validates that the age entered is greater than or equal to 5
    if duration > 0:
        valid_duration = True
    else:
        print("\nDuration must be greater than 0")
        valid_duration = False
        return
    
    artist = input("\nEnter the artist of the new song: ")
    #Validates that the artist entered is a string and > 0
    if isinstance(artist, str) and len(artist) > 0:
            valid_artist = True
    else:
        print("\nInvalid artist. Artist must be a string.")
        valid_artist = False
        return

    playlist_id = input("\nEnter the id of the playlist the song belongs to: ")
    try:
        playlist_id = int(playlist_id)
    except ValueError:
        print("\nPlaylist id must be an integer")
        return
    playlist = Playlist.find_by_id(playlist_id)
    if playlist:
            valid_playlist_id = True
    else:
        print("\nInvalid playlist id. Associated playlist must exist in the database")
        valid_playlist_id = False
        return
    
    if valid_title and valid_genre and valid_duration and valid_artist and valid_playlist_id:
        print("\nCreating new song...")
        new_song = Song.create(title, genre, duration, artist, playlist_id)
        print("\nSong created")
        print(new_song)
        
def delete_song():
    """Deletes song by id"""
    song_id = input("\nEnter the id of the song to be deleted: ")
    song = Song.find_by_id(song_id)
    if song:
        print(f'\nDeleting song with id {song_id}')
        song.delete()
        print("\nSong deleted")
    else:
        print("\nInvalid song id. Song must exist in the database")
    
def update_song():
    """Updates song by id"""
    song_id = input("\nEnter the id of the song to be updated: ")
    song = Song.find_by_id(song_id)
    if song:
        title = input("\nEnter the new title of the song: ")
        #Validates that the title entered is a string and > 0
        if isinstance(title, str) and len(title) > 0:
                valid_title = True
        else:
            print("\nInvalid title. Title must be a string.")
            valid_title = False
            return
        
        genres= ['pop','dance','rock','r&b','country', 'hip hop']
        genre = input("\nEnter the new genre of the song: ")
        genre_lower = genre.lower()
        #Validates that the genre entered is a string and > 0
        if isinstance(genre_lower, str) and len(genre_lower) >= 3 and genre_lower in genres:
                valid_genre = True
        else:
            print("\nInvalid genre. Genre must be pop, dance, rock, r&b, country, or hip hop")
            valid_genre = False
            return
        
        duration = input("\nEnter the new duration of the song in seconds: ") 
        #Validates that the age entered is an integer
        try:
            duration = int(duration)
        except ValueError:
            print("\nDuration must be an integer")
            return
        #Validates that the age entered is greater than or equal to 5
        if duration > 0:
            valid_duration = True
        else:
            print("\nDuration must be greater than 0")
            valid_duration = False
            return
        
        artist = input("\nEnter the new artist of the song: ")
        #Validates that the artist entered is a string and > 0
        if isinstance(artist, str) and len(artist) > 0:
                valid_artist = True
        else:
            print("\nInvalid artist. Artist must be a string.")
            valid_artist = False
            return

        playlist_id = input("\nEnter the new id of the playlist the song belongs to: ")
        try:
            playlist_id = int(playlist_id)
        except ValueError:
            print("\nPlaylist id must be an integer")
            return
        playlist = Playlist.find_by_id(playlist_id)
        if playlist:
                valid_playlist_id = True
        else:
            print("\nInvalid playlist id. Associated playlist must exist in the database")
            valid_playlist_id = False
            return
        
        if valid_title and valid_genre and valid_duration and valid_artist and valid_playlist_id:
            print("\nUpdating song...")
            song.title = title
            song.genre = genre
            song.duration = duration
            song.artist = artist
            song.playlist_id = playlist_id
            song.update()
            print("\nSong updated")
            print(song)
        
    else:
        print("\nInvalid song id. Song must exist in the database") 
        
def show_by_genre():
    """Shows all the songs under a specified genre and totals the number of songs"""
    genres= ['pop','dance','rock','r&b','country', 'hip hop']
    genre = input("\nEnter genre: ")
    try:
        genre_lower = genre.lower()
    except ValueError:
        print("\nGenre must be one of the following: pop, dance, rock, r&b, country, hip hop")
    if genre_lower in genres:
        songs = Song.get_all()
        genre_songs = [ song for song in songs if genre_lower == song.genre.lower() ]
        if genre_songs:
            print(f'\nShowing songs under the genre {genre_lower}...')
            total = len(genre_songs)
            for song in genre_songs:
                print(song)
            print(f'\nTotal number of songs under the genre {genre_lower}: {total}')
        else:
            print(f'\nThere are no songs in the database under the genre {genre_lower}')
    else:
        print("\nGenre must be one of the following: pop, dance, rock, r&b, country, hip hop") 
        return  
    
def find_song_by_title():
    """Finds song by title"""
    song_title = input("\nEnter the title of the song you wish to find: ")
    try:
        song_title = song_title.title()
    except ValueError:
        print("\nSong title must be a string")
        return
    song = Song.find_by_title(song_title)
    if song:
        print("\nFinding song...")
        print("\nSong found")
        print(song)
    else:
        print("\nInvalid title. Song must exist in the database")
    
def exit_program():
    print("\nGoodbye!")
    exit()
