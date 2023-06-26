from youtubesearchpython import VideosSearch

def search_youtube_videos(query):
    videos_search = VideosSearch(query, limit=1)
    results = videos_search.result()
    videos = []
    for video in results['result']:
        video_data = {
            'title': video['title'],
            'video_id': video['id'],
            'duration': video['duration'],
            'thumbnail': video['thumbnails'][0]['url'],
            'link':video['link']
        }
        print(video)
        videos.append(video_data)
    return videos
query = 'Oh Penne by Anirudh Ravichander'
results = search_youtube_videos(query)
for video in results:
    print(f"Title: {video['title']}")
    print(f"Video ID: {video['video_id']}")
    print(f"Duration: {video['duration']}")
    print(f"Thumbnail URL: {video['thumbnail']}")
    print(f"Link : {video['link']}")
# https://www.youtube.com/watch?v=nIYiEBniMv8