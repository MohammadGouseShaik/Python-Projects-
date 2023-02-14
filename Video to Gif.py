from moviepy.editor import *

# Load the video file
video = VideoFileClip('video.mp4')

# Convert the video to a GIF file
gif = video.subclip(0,10).resize(0.5).to_gif()

# Save the GIF file
with open('output.gif', 'wb') as f:
    f.write(gif)
