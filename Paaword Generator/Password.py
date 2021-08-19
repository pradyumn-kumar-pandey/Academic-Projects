import tkinter
import string
import random


def final_step(s):
    if not s:
        pass
    else:
        length_pass=length.get("1.0","end-1c")
        if not length_pass:
            return
        else:
            length_pass=int(length_pass)
            res_string=random.sample(s,length_pass)
            res_string="".join(res_string)
            l6=tkinter.Label(window,text="Generated Pasword:")
            l6.place(x=210,y=270)
            
            l7=tkinter.Label(window,text='',font=('Arial',16,'bold'),width=35)
            l7.place(x=30,y=300)
            
            l7.config(text=res_string)
        
      


def sixth_step1(s):
    final_step(s)

def sixth_step2(s):
    s+=string.punctuation
    final_step(s)


def fifth_step(s):
    l5=tkinter.Label(window,text="Special Characters:")
    l5.place(x=120,y=230)
    btn5=tkinter.Button(window,text="NO",command=lambda: sixth_step1(s))
    btn5.place(x=230,y=230)
    
    btn6=tkinter.Button(window,text="YES",command=lambda: sixth_step2(s))
    btn6.place(x=270,y=230)     
    
    
def fourth_step1(s):
    fifth_step(s)

def fourth_step2(s):
    s+=string.digits
    s=str(s)
    fifth_step(s)


def third_step(s):
    l4=tkinter.Label(window,text="Numbers:")
    l4.place(x=160,y=190)
    btn3=tkinter.Button(window,text="NO",command= lambda: fourth_step1(s))
    btn3.place(x=230,y=190)
    
    btn4=tkinter.Button(window,text="YES",command=lambda : fourth_step2(s))
    btn4.place(x=270,y=190) 
    

def second_step(val):
    if val==1:
        password_str=''
        password_str+=string.ascii_letters
        third_step(password_str)
        
    else:
        password_str=''
        third_step(password_str)

def first_step():
    l3=tkinter.Label(window,text='Alphabets:')
    l3.place(x=160,y=160)

    btn1=tkinter.Button(window,text="NO",command=lambda: second_step(val=0))
    btn1.place(x=230,y=160)
    
    btn2=tkinter.Button(window,text="YES",command=lambda: second_step(val=1))
    btn2.place(x=270,y=160)
    
 

password_str=''    
window=tkinter.Tk()
window.iconbitmap('pass.ico')
window.resizable(width=False,height=False)
window.geometry("500x500")
window.title("Password Generator")

l1=tkinter.Label(window,text="Password Generator",font=('Algerian',20))
l1.pack()


l2=tkinter.Label(window,text="Enter Length:")
l2.place(x=150,y=80)

length=tkinter.Text(window,height=2,width=10)
length.place(x=230,y=75)

cont=tkinter.Button(window,text="Continue",command=lambda:first_step())
cont.place(x=240,y=115)

window.mainloop()