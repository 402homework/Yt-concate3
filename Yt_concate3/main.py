import urllib.request
import json
import ssl
import os
from Yt_concate3.setting import API_KEY

ssl._create_default_https_context = ssl._create_unverified_context
CHANNEL_ID = 'UCGGrblndNzi86WY5lJkQJiA'
def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyAlgPzH59jGMNXY9V9sLPybdzG-HX00bkU'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
