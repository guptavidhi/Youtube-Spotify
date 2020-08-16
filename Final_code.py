import pandas as pd
import requests
from bs4 import BeautifulSoup

url = ""
spotify_auth_token=''
spotify_user_id=''
# playlist_name_in_spotify='New_YT'

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
# soup=BeautifulSoup(r.content,'html5lib')

soup=soup.encode("utf-8")
src_pg=str(soup)
var1=src_pg.split('"title":{"accessibility":{"accessibilityData":{"label":"')
var2=[x for x in var1 if " by " in x]
var3=[""]*len(var2)

for i in range(0,len(var2)):
    var3[i]=var2[i].split(" by ",1)[0]

song_list=var3[1:]
# print(var3)

s1=["\\U0026","(",")","[","]","Official","Video","Music","Lyric","-","/","\\"]
s2=""
for i in range(0,len(song_list)):
    for j in range(0,len(s1)):
        song_list[i]=song_list[i].title().replace(s1[j],s2)

import string, re
for i in range(0,len(song_list)):
    song_list[i]=re.sub(r'[^A-Za-z0-9 ]+', '', song_list[i]).strip()
# df=pd.DataFrame(var3,columns=['Names'])
# df.to_csv(r'C:\Users\Vidhi Gupta\Desktop\Python_practice\Excel sheets\first.csv',encoding='utf-8')
print(song_list)

def create_spotify_playlist():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(spotify_auth_token),
    }

    data = '{"name":"Youtube_playlist","description":"Playlist created from youtube","public":false}'

    response = requests.post('https://api.spotify.com/v1/users/{}/playlists'.format(spotify_user_id), headers=headers, data=data)
    json_response=response.json()
    playlist_id=json_response["id"]
    return playlist_id

def spotify_search_song(song_name):
    try:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(spotify_auth_token),
        }

        params = (
            ('q', song_name),
            ('type', 'track'),
        )

        response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

        json_response=response.json()
        # song_uri=json_response['tracks']['items'][0]['id']
        return json_response['tracks']['items'][0]['id']
    except:
        return ''
def add_spotify_playlist(song_uri):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(spotify_auth_token),
    }

    params = (
        ('uris', 'spotify:track:{}'.format(song_uri)),
    )

    response = requests.post('https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id), headers=headers, params=params)

playlist_id=create_spotify_playlist()

# song_uri=['']*len(song_list)
# spotify_track_uri=['']*len(song_list)

# for i in range(0,len(song_list)):
#     if len(spotify_search_song(song_list[i]))>1:
#         song_uri[i]='spotify:track:'+spotify_search_song(song_list[i])
#     else:
#         song_uri[i]='Not_found'
#
# song_uri=[i for i in song_uri if 'Not_Found' not in song_uri]
#
# song_uri=",".join(song_uri)
# print(len(song_uri))
for i in range(0,len(song_list)):
    add_spotify_playlist(spotify_search_song(song_list[i]))

# def create_spotify_playlist():
#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer {}'.format(spotify_auth_token),
#     }
#
#     data = '{"name":"Youtube_playlist","description":"Playlist created from youtube","public":false}'
#
#     response = requests.post('https://api.spotify.com/v1/users/{}/playlists'.format(spotify_user_id), headers=headers, data=data)
#     json_response=response.json()
#     playlist_id=json_response["id"]
#     return playlist_id
#
# def spotify_search_song(song_name):
#     try:
#         headers = {
#             'Accept': 'application/json',
#             'Content-Type': 'application/json',
#             'Authorization': 'Bearer {}'.format(spotify_auth_token),
#         }
#
#         params = (
#             ('q', song_name),
#             ('type', 'track'),
#         )
#
#         response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
#
#         json_response=response.json()
#         # song_uri=json_response['tracks']['items'][0]['id']
#         return json_response['tracks']['items'][0]['id']
#     except:
#         return ''
# def add_spotify_playlist(song_uri):
#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer {}'.format(spotify_auth_token),
#     }
#
#     params = (
#         ('uris', song_uri),
#     )
#
#     response = requests.post('https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id), headers=headers, params=params)
#
# playlist_id=create_spotify_playlist()
#
# song_uri=['']*len(song_list)
# spotify_track_uri=['']*len(song_list)
#
# for i in range(0,len(song_list)):
#     if len(spotify_search_song(song_list[i]))>1:
#         song_uri[i]='spotify:track:'+spotify_search_song(song_list[i])
#     else:
#         song_uri[i]='Not_found'
#
# song_uri=[i for i in song_uri if 'Not_Found' not in song_uri]
#
# song_uri=",".join(song_uri)
# print(len(song_uri))
#
# add_spotify_playlist(song_uri)
# playlist_id=create_spotify_playlist()
# print(playlist_id)
