import urllib.request
import json
from .settings import API_KEY


# channel_url = "https://www.youtube.com/c/OverSimplified"
channel_id = "UCNIuvl7V8zACPpTmmNIqP2A"
print(API_KEY)

def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = f"{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25"
    video_links = []
    url = first_url
    while True:
        http_response = urllib.request.urlopen(url)
        json_data = json.load(http_response)

        for i in json_data['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = json_data['nextPageToken']
            url = f"{first_url}&pageToken{next_page_token}"
        except KeyError:
            break
    return video_links

# video_list = get_all_video_in_channel(channel_id)
# print(video_list)