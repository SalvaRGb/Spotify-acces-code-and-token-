# Spotify acces code and token 
A spotify app to retrive private user information and public spotify info provided by spotify API in python.

The Spotify Web API return data about music artists, albums, and tracks, directly from the Spotify Data Catalogue. Web API also provides access to user related data, like playlists and music that the user saves in the Your Music library. Such access is enabled through selective authorization, by the user.

To interact with the spotify Web API at any level you must register as a spotify developer in [Here](https://developer.spotify.com/dashboard/login)  It´s important to configurate the data_init.json file and include the client_id and secret_id provided by your account once you create a new app, in addition if your are interested in acces user private data, you would need to include the scopes your interested in explore as a list of strings; documentation [Here](https://developer.spotify.com/documentation/general/guides/authorization/scopes/)

The objective of catch_accesAndToken.py is to provide a class acces_code in order to acces user related data and a class token thats works either for athorization code flow or client code flow.

 
