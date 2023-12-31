# **Welcome to the Weather Plus Spotify Music Player**: :sun_behind_small_cloud:
- This web app is designed to find the weather of a major city and return a playlist based on the weather conditions such as temperature. 
- This is a simple app, the orginal idea was also to utilize the Spotify API, yet there were some issues running the output with allowing the user to search/ be recommended a playlist. 
- The Spotify.py file is an example of running the API and breaking down the JSON responce data. 
- Future plan of adding Spotify Capabilities 

# **How to use the app?** :compass:

Download the required packages before running the code:

- Flask (pip install Flask)
- JSON (pip install json)
- Base64 (pip install pybase24)
- Dotenv (pip install python-dotenv)

# **Required Access for APIs**:world_map:

The following API keys are required to run this app: 

- OpenWeather API (https://openweathermap.org/appid)
- Spoify API (https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

# **Why a Weather Plus Spotify Music Player?**

-Overall felt like it seemed like a fun project that could utilzie 2 APIs and is something I might use in the future whether I am studying or want to change up my playlists. 
-Neat idea to map temperature to different playlists, make it a bit different from the normal weather apps and offers more utility to the end-users. 
-Also always felt that weather typically had a corresponding music mood and wanted to build upon that idea. 

# **How Does it Work**  :cowboy_hat_face:

- This app utilizes the OpenWeather API which returns JSON data. 
- The user will input a desired city "location" and the app will access the API and searched for the desired location and return the JSON data, which will be further split into the desired data points of temperature, feels like temperature, temp. min, temp. max, humidity, wind, and gust speeds. where the response data is broken down based on the location 
- ![Alt text](image-12.png)
- ![Alt text](image.png)
- Once the data has been gathered by the app it will be loaded onto the weather.html page
- The weather.html page has a textbox where all of the data points will be imputed 
- ![Alt text](image-1.png)
- The data points from the API for the specific location will be utilized by the get_playlist_url function to choose from a few pre-selected weather/ temperature themed playlists. 
- The determination of the playlist is based on temperature range and weather conditions
- The get_playlist_url function utilizes a basic if else statement to return a url to the corresponding Spotify playlist
- ![Alt text](image-10.png)
- This corresponding Spotify playlist will then be inputed into the weather.html page, where it will be showcased in a mini Spotify Web Player via embeded code from Spotify
- ![Alt text](image-13.png) 
- ![Alt text](image-2.png)
- The weather.html page additionally has a live weather map that was added from the RainViewer (https://www.rainviewer.com/radars/united-states.html) via embeded code
- ![Alt text](image-3.png)

# **Design Choices/ Issues** :orange:

- One of the first issues that still need to be resolved is fixing how the location is found by the app, since at the moment it only takes in City names and is not able to take in State names, tried reworking the code with Long and Lat yet still ran into the same problems
- Orginally the plan was to utilize the Spotify API yet it proved to be a bit more difficult when implementing into Flask, even though it utilizes JSON data format.
- In the spotify.py file is an area showing the ability to read JSON data from the API and return either with an artist or the song titles listed in a playlist.
- ![Alt text](image-4.png)
- ![Alt text](image-5.png)
- One of the common issues with adding the Spotify API aspect was the connecting multiple pages and ending up with a 404 error
- ![Alt text](image-6.png)
- Sometimes I would be able to obtain the music playlist I searched for and be missing the linking to the OpenWeather Data for my desired location
- ![Alt text](image-7.png)
- After searching a bit, I found that Spotify had the ability to embed a playlist straight into HTML thorugh a mini web player. 
- The embeded playlist seemed like the most effective way forward since it would require less work with the CSS styling
- ![Alt text](image-9.png) 
- One drawback of the embeded playlist is the limit on the various playlist that could be possible for the weather combinations. Since all of the possible playable playlists right now in the website are pre-selected. 

# **Final Product** :star:

- ![Alt text](image-11.png)

# **Future Steps** :next_track_button:

- Work on the full implementation of the Spotify API 
- Additionally figure out how to create customizable playlists based on a user's Spotify's account
- Improve styling on the overall page 
- Fix the geo-location issue with the City Search Bar 
