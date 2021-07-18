import urllib.request
import json
import ssl
from Yt_concate3.pipeline.Steps.step import Step  #package下面絕對路徑從Yt_concate3裡面的steps目錄的step.py import step class
from Yt_concate3.setting import API_KEY

#寫Step class
#寫GetVideoList class
#channel id怎麼來
#何時用StepException把main修完

class GetVideoList(Step):    #繼承Step class.上面要有import的路徑
    def process(self,data,inputs):    #一定要有method process for @abstractmethod
        channel_id = inputs['channel_id']
        #self.get_all_video_in_channel(inputs['channel_id'])    #call self裡面的get_all_video_in_channel()
                                                               #從字典inputs裡面的channel_id拿到id
        ssl._create_default_https_context = ssl._create_unverified_context

        api_key = 'AIzaSyAlgPzH59jGMNXY9V9sLPybdzG-HX00bkU'

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, channel_id)

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
        print(video_links)
        return video_links


