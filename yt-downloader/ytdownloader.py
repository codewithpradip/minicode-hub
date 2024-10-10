# importing the module 
from pytube import YouTube

# link of the video to be downloaded 
link = input("Enter The Link : ")

try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link)
    #Title of video
    print("Title : ", yt.title)
    #Number of views of video
    print("Number of views: ",yt.views)
    #Length of the video
    print("Length of video: ",yt.length,"seconds")
    #Description of video
    print("Description: ",yt.description)
    #get the video highest resolution
    ys = yt.streams.get_highest_resolution()
    # downloading the video 
    ys.download('')
    print('Task Completed!') 
except: 
    print("Connection Error") #to handle exception 

    
