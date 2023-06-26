from youtube_search import YoutubeSearch

# Specify the search query
query = 'YOUR_SEARCH_QUERY'  # Replace with your desired search query

# Perform the search
results = YoutubeSearch(query, max_results=10).to_dict()

# Extract video information from the results
for video in results:
    video_id = video['id']
    video_title = video['title']
    video_duration = video['duration']
    video_thumbnail = video['thumbnails'][0]

    # Print or process the video information as needed
    print(f'Title: {video_title}')
    print(f'Video ID: {video_id}')
    print(f'Duration: {video_duration}')
    print(f'Thumbnail: {video_thumbnail}')
    print('---')
