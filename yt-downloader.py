#python script by somanshu srivastava
from tkinter import *
from pytube import YouTube

def NewFile():
    print("new file")
    

def ShowOptionsScreen(li):
    window = Toplevel(root)
    
    x=""
    for lo in li:
        
        x = x+str(lo)
        
    options_label = Label(window, text=x)
    options_label.pack(fill=X)
        
    print(x)
        
    
    

def VideoScreen():
    x = E.get()
    Yt = YouTube(x)
    li = Yt.get_videos()
    ShowOptionsScreen(li)
    


        

root = Tk()
root.attributes('-alpha', 0.9)
root.minsize(width=1000, height=600)
root.maxsize(width=1000, height=600)
flag=True

C = Canvas(root, bg="blue", height=800, width=800)
filename = PhotoImage(file = "bg1.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

msg = "Welcome to Somanshu's simple YOUTUBE VIDEO DOWNLOADER"
intro_msg = Message(root, text="YOUTUBE VIDEO DOWNLOADER")
intro_msg.config(font= ('Georgia', 24, 'bold'), background="orange", width=850)
intro_msg.place(relx=0, rely=0, x= 0, y=10)
intro_msg.pack(fill=X)

url_message=Message(root, text="Enter the URL of the video")
url_message.config(font= ('Georgia', 20, 'italic'), background='orange', width=1000)
E=Entry(root, font=('Georgia', 20, 'bold'))
submit_url = Button(root, text="DOWNLOAD",font=('Georgia', 16, 'bold'), command = VideoScreen)

url_message.place(relx=0, rely=0, x=0,y=20)
E.place(relx=0, rely=0, x=0,y=20)
submit_url.place(relx=0, rely=0, x=0,y=20)
url_message.pack(fill=X)
E.pack(fill=X)
submit_url.pack(fill=X)
if flag == False:
    opt_msg = Message(root, text="SELECT THE OPTION YOU WANT TO CHOOSE", background="orange", width=850)
    opt_msg.place(relx=0,rely=0, x=0,y=20)
    opt_msg.pack(fill=X)
    

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)



C.pack()

root.mainloop()
