import tkinter
from pytube import YouTube


def analyse_link(link):
    try:
        video=YouTube(link)
    except:
        msg.config(text="Please enter correct URL")
        return -1
    stream=video.streams.filter(type='video')
    return stream

def inp():
    msg.config(text='')
    link=T1.get("1.0","end-1c")
    if not link:
        msg.config(text="Please Enter URL First")
        return
    else:
        stream=analyse_link(link)
        if stream==-1:
            return
        else:
            a=50
            b=100
            for i in stream:
                l2=tkinter.Label(window,text=i)
                l2.place(x=a,y=b)
                b+=15
        
def download():
    msg.config(text='')
    link=T1.get("1.0","end-1c")
    resol=T2.get("1.0","end-1c")
    if not resol:
        msg.config(text="Please Enter Preferred Resolution First")
    else:
        stream=analyse_link(link)
        if stream==-1:
            return
        else:
            stream.filter(res=resol+'p').first().download()
            msg.config(text="Video is being downloaded in the folder where the code exists.")
    
        
       
window=tkinter.Tk()
window.title('YouTube Video Downloader')
window.iconbitmap('yt.ico')
window.geometry('900x700')
window.resizable(width=False,height=False)

l1=tkinter.Label(window,text='Enter URL')
l1.place(x=50,y=30)

T1=tkinter.Text(window,height=2,width=90)
T1.place(x=120,y=30)

btn=tkinter.Button(window,text='Submit',command=lambda:inp())
btn.place(x=400,y=75)


l3=tkinter.Label(window,text='Enter Preferred Resoluton(from Above List):')
l3.place(x=45,y=655)

T2=tkinter.Text(window,height=2,width=10)
T2.place(x=290,y=650)

l4=tkinter.Label(window,text='p')
l4.place(x=370,y=655)


dwnld=tkinter.Button(window,text="Download",command=lambda:download())
dwnld.place(x=400,y=655)


msg=tkinter.Label(window,text='')
msg.place(x=500,y=655)

window.mainloop()