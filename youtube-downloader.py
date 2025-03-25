from tkinter import *
from pytubefix import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Video Downloader 🎥')
root.configure(bg='#AACDE2')

Label(root, text='Download Your Videos!', font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)
link = StringVar()

Label(root, text='Insert URL here: ', font='arial 12', bg='#AACDE2').place(x=190, y=90)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=120)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 13 bold', bg='#AACDE2', fg='#B57199').place(x=180, y=240)

Button(root,text='DOWNLOAD', font='arial 13 bold italic', bg='#B57199', padx=2, command=Downloader).place(x=180, y=180)
root.mainloop()