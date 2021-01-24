from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1= VideoFileClip("city_id=1.avi")
clip2= VideoFileClip("city_id=2.avi")

final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("testing_concat.mp4")
print("done")