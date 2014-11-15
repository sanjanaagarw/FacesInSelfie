import os
import json
import urllib
import urllib2
from instagram.client import InstagramAPI
 
#ur client id and secret id
INSTAGRAM_CLIENT_ID = ''
INSTAGRAM_CLIENT_SECRET = ''
 
api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID,client_secret=INSTAGRAM_CLIENT_SECRET)

def find_images(query, path):
    recent = api.tag_recent_media(1,100,query)
    #print recent
    link = recent[1]
    #print link
    response = urllib2.urlopen(link)
    #print response
    ig = json.load(response)
    #print ig
    status=ig['meta']['code']
 
    while status == 200:
        data = ig['data']
        if not data:
            link = ig['pagination']['next_url']
            response = urllib2.urlopen(link)
            ig = json.load(response)
        else:
            image = ig['data'][0]['images']['standard_resolution']['url']
            unique = str(ig['data'][0]['created_time'])
            str(image)
            urllib.urlretrieve(image, os.path.join(path, '%s.jpg') % unique )
            link = ig['pagination']['next_url']
            response = urllib2.urlopen(link)
            ig = json.load(response)
#pass the parameter which will be hashtag, and second parameter is path, which means images will be downloaded #into same folder in which this script is reciding
find_images("selfie",'')