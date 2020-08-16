# Youtube-Spotify
Creating a Youtube playlist on Spotify. 

# How it works:
1. The youtube playlist page is scraped and the list of song names are generated
2. Spotify API is used to create a playlist
3. The URI for the list of songs is created
4. The songs are added to created playlist 

# Python libraries used:
1. Pandas
2. Requests
3. BeautifulSoup
4. Strings and re

# Limitations:
1. Does not work on a playlist with more than 100 songs.
2. Does not work with differently scripted song titles (Hindi, Korean etc.)

# Mistakes:
1. Youtube scraping instead of using Youtube API.
