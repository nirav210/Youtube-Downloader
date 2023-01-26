from tkinter import *
from pytube import YouTube
from pytube import Playlist

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DOM")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()
var = IntVar()
R1 = Radiobutton(root, text="Single Video", variable=var, value=1)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Playlist", variable=var, value=2)
R2.pack( anchor = W )

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 54,textvariable = link).place(x = 32, y = 90)

def Downloader():
    if var.get() == 1:     
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
    else:
        url = Playlist(str(link.get()))
        for video in url.videos:
            video.streams.first().download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'dark grey', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()