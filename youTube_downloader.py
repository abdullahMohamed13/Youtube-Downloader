# Before anything:
# In Visual studio code Go to : view => Terminal => And type this : pip install pytube
# Then do right click on youTube_downloader.py and choose Run python file in terminal
# Then paste link of the video you want "")
import pytube

# Prompt the user to input the YouTube video URL / Don't edit it
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object by passing the video URL / Don't edit it
youtube = pytube.YouTube(video_url)

# Select the highest quality video stream

# Download highest quality video
# video_stream = youtube.streams.get_highest_resolution()

# Download 720p quality video
video_stream = youtube.streams.filter(res="720p").first()

# Specify the output directory where the video will be saved / Choose the path you
#                                                              want the video in
output_directory = "D:\Courses\CSS-Template"

# Download the video / Don't edit it
video_stream.download(output_directory)

print("Video downloaded successfully!")