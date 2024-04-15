# Music Database manager

## Overview

The music database manager is a command line application that allows users to manage users, playlists, and songs. Users include many playlists, playlists include many songs, but a playlist can only belong to one user and a song can only belong to one playlist

You can run the file `python cli.py` to start up the CLI. This file first seeds the database with sample data, then allows users to navigate the cli.

## Command Line Menus

From the main menu there are 3 menus (Users, Playlists, Songs) that users can enter in order to perform different tasks.

&nbsp;

<img width="963" alt="Screenshot 2024-04-15 095749" src="https://github.com/asuarez9382/python-p3-v2-final-project-template/assets/12467862/47ccdf1f-1d91-49f9-bd4b-f967396690b6">

### Users

Below shows the User menu and the different actions the user can perform 

&nbsp;

<img width="963" alt="Screenshot 2024-04-15 100129" src="https://github.com/asuarez9382/python-p3-v2-final-project-template/assets/12467862/d05b487b-51a2-4e9a-b257-bc4be6375478">

&nbsp;

Users can list all of the current users, create a new user, update a user, delete a user, view a certain user's playlists and find a specific user by username. Once one of these options are entered, the user will be prompted to provide input information that will be validated against the database. 

&nbsp;

### Playlists

Similar to the User menu, users can look through the Playlist menu and perform different actions. 

&nbsp;

<img width="963" alt="Screenshot 2024-04-15 100850" src="https://github.com/asuarez9382/python-p3-v2-final-project-template/assets/12467862/348de9b8-f474-4cfa-90ca-3ab6b5bd8aca">

&nbsp;

The Playlist menu has some of the same features as the User menu however a user can also show songs in a particular playlist and find the playlist by id. 

&nbsp;

### Songs

Similar to the User menu and the Playlist menu, users can look through the Song menu and perform different actions. 

&nbsp;

<img width="963" alt="Screenshot 2024-04-15 101100" src="https://github.com/asuarez9382/python-p3-v2-final-project-template/assets/12467862/e2b5422a-1496-4454-a1bd-c4eebfe3d903">

&nbsp;

The Song menu has some of the same features as the User menu and the Playlist menu however a user can also show all the songs in a particular genre as well as find a song by name. 

&nbsp;

## Helper Functions

`helpers.py` contains numerous helper functions that support the CLI interactivity. Below is an overview of these functions:

`exit_program()` exits the program when a user selects 0 from the main menu.

--

`list_users()` Lists all of the users in the database.

`update_user()` prompts the user to enter the ID of the user to be updated and then asks the user for the updated information.

`find_by_username()` prompts the user to enter the username of the user to be found and then returns that user's information.

`create_user()` prompts the user to enter in information about the new user and then creates a new user in the database.

`delete_user()` prompts the user to enter the ID of the user to be deleted and then deletes the corresponding user. 

`show_playlists()` prompts the user to enter the username of the user and displays that users playlists.

--

`list_playlists()` Lists all of the playlists in the database.

`create_playlist()` prompts the user to enter in information about the new playlist and then adds it to the database

`delete_playlist()` prompts the user to enter the ID of the playlist to be deleted and then deletes the corresponding playlist.

`update_playlist()` prompts the uder to enter the ID of the playlist to be updates and then prompts the user to enter information to update the playlist

`find_playlist_by_id()` prompts the user to enter the ID of the playlist and then displays the information about that playlist. 

`show_songs_from_playlist()` prompts the user to enter the ID of the playlist and displays all the songs that belong to that particular playlist.

--

`list_songs()` Lists all of the songs in the database.

`create_song()` prompts the user to enter information about the new song and then creates the new song.

`delete_song()` prompts the user to enter the ID of the song to be deleted and then deletes that particular song.

`update_song()` prompts the user to enter the ID of the song to be updated and then asks for the updated information about the song.

`show_by_genre()` prompts the user to enter the genre and displays all of the current songs in the database that is under that genre. Also displays a total number of songs in the genre. 

`find_song_by_title()` prompts the user to enter the title of the song, and then displays the information regarding that song. 

&nbsp;

## Models

This project is using 3 classes to manage the functionality of and relationships between users, playlists, and songs. The classes have many of the same methods.

### User

`user.py` contains the `User` class which is responsible for the functionality of all `User` objects. It includes the properties `username`, `email`, `age`, etc which are also validated. It also includes methods to create and drop the 'users' table, create a `User`, update a `User`, delete a `User`, get all `User`s, find a `User` by username or id, and display its playlists. It also includes a method to create a `User` from a row of the database.

Here is an example of a `User` printed: "User ID: 1 Username: mochi9382 Email: mochi@gmail.com Age: 21"

### Playlist

`playlist.py` contains the `Playlist` class which is responsible for the functionality of all `Playlist` objects. It includes the properties `title`, `description`, `user_id` which are also validated. It also includes methods to create and drop the 'playlists' table, create a `Playlist`, update a `Playlist`, delete a `Playlist`, get all `Playlist`s, find a `Playlist` by id, and display all the songs in the `Playlist`. It also includes a method to create a `Playlist` from a row of the database.

Here is an example of a `Playlist` printed: "Playlist ID: 1 Playlist title: Top Hits of 2002 Playlist description: Top songs from the year 2002 UserID: 1"

### Song

`song.py` contains the `Song` class which is responsible for the functionality of all `Song` objects. It includes the properties `title`, `duration`, `genre`, `artist`, `playlist_id` which are also validated. It also includes methods to create and drop the 'songs' table, create a `Song`, update a `Song`, delete a `Song`, get all `Song`s, find a `Song` by title, and display all the songs in a particular genre. It also includes a method to create a `Song` from a row of the database.

Here is an example of a `Song` printed: "Song ID: 1 Song Title: Dilemma Song genre: Hip Hop Duration: 289 Artist: Nelly Playlist ID: 1"
