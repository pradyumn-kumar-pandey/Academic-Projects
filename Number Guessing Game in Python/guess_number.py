import tkinter
import random

def match_val(v,n):
    
    if v<n:
        final_msg=tkinter.Label(window,text='Smaller')
        final_msg.place(x=220,y=290)
    elif v>n:
        final_msg=tkinter.Label(window,text=' Larger ')
        final_msg.place(x=220,y=290)
    else:
        window.destroy()
        
def start_gm():
    start=start_val.get("1.0","end-1c")
    end=end_val.get("1.0","end-1c")
    
    if not start or not end:
        res_label.config(text="Please Enter The Range First")
        return
    else:
        if int(end)<int(start):
            res_label.config(text="End Can't Be Smaller Than Start")
            return
        if int(start)<=0 or int(end)<=0:
            res_label.config(text="Value Can't Be Negative or Zero")
            return            
        else:
            start=int(start)
            end=int(end)
            num=random.randint(start,end)
            res_label.config(text="Enter Your Guess : ")
            user_val=tkinter.Text(window,height=1,width=5)
            user_val.place(x=220,y=220)
            def get_val():
                val=user_val.get("1.0","end-1c")
                val=int(val)
                match_val(val,num)
            ok_btn=tkinter.Button(window,text="OK",command=lambda:get_val())
            ok_btn.place(x=230,y=250)

        
window=tkinter.Tk()
window.title("Number Guess Game")
window.geometry("500x500")
window.resizable(width=False,height=False)
window.iconbitmap("num.ico")

l1=tkinter.Label(window,text="Number Guessing Game",font=('Algerian',20))
l1.pack()

tkinter.Label(window,text='').pack()


l2=tkinter.Label(window,text="Enter The Range Of Number: ")
l2.pack()

l3=tkinter.Label(window,text="From : ")
l3.place(x=100,y=100)

start_val=tkinter.Text(window,height=1,width=5)
start_val.place(x=145,y=100)

l4=tkinter.Label(window,text="To : ")
l4.place(x=300,y=100)

end_val=tkinter.Text(window,height=1,width=5)
end_val.place(x=335,y=100)

start_game=tkinter.Button(window,text="START GAME",command=lambda:start_gm())
start_game.place(x=210,y=140)


res_label=tkinter.Label(window,text='')
res_label.place(x=190,y=190)
window.mainloop()