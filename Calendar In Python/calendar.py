import tkinter
import calendar

def print_cal():
    y=year.get("1.0","end-1c")
    if not y:
        res_label.config(text='Enter Year First')
    else:
        y=int(y)
        if y<=0:
            res_label.config(text='Year Must Be Whole Number')
        else:
            wi=tkinter.Tk()
            wi.title(y)
            wi.geometry('600x600')
            wi.iconbitmap('cal.ico')
            wi.resizable(width=False,height=False)
            i=1
            for r in range(4):
                for c in range(3):
                    label=tkinter.Label(wi,text=calendar.month(y,i),font="Consolas 10 bold",anchor= 'w')
                    label.grid(row=r,column=c,padx=20)
                    i+=1
            Ok=tkinter.Button(wi,text="OK",command=lambda: can(wi))
            Ok.place(x=270,y=550)

                

def can(win):
    win.destroy()
window=tkinter.Tk()
window.title("calendar")
window.iconbitmap("cal.ico")

window.resizable(width=False,height=False)

window.geometry("700x400")

heading=tkinter.Label(window,text="Calendar",font=('Algerian',20))
heading.pack()

tkinter.Label(window,text="").pack()

message=tkinter.Label(window,text="Enter Year : ",font=('Arial',13))
message.pack()

tkinter.Label(window,text="").pack()

year=tkinter.Text(window,height=1,width=5)
year.pack()

Ok=tkinter.Button(window,text="SUBMIT",command=lambda: print_cal())
Ok.pack()

cancel=tkinter.Button(window,text="QUIT",command=lambda: can(window))
cancel.pack()

res_label=tkinter.Label(window,text='')
res_label.pack()

window.mainloop()