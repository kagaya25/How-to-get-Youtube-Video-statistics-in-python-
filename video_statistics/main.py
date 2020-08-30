import urllib.request
import json 
from apikey import apikey 
#https://github.com/kagaya25/How-to-get-Youtube-Video-statistics-in-python-

def getViews(VID_ID, API_KEY):

        url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='  + VID_ID + '&key=' + API_KEY
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        res = json.loads(respData.decode('utf-8'))
        print(url)
        print(res)
        statistics = res["items"][0]["statistics"]
        viewCount = statistics["viewCount"]

        return viewCount
#Example  https://www.youtube.com/watch?v=YwNlVeReXXc
#YwNlVeReXXc is the id we need 

url = input("Paste your youtubevideo id :")
print(getViews(url,apikey))
