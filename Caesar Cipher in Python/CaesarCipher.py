import tkinter
import tkinter.font as font
import random


def encrypt_text():
    INPUT = T.get("1.0", "end-1c")
    resultant=''
    if INPUT=="":
        resultLabel.config(text="Enter text")
    else:
        key=random.randint(1,25)
        
        for i in INPUT:
            val=ord(i)
            if i.isdigit():
                resultant+=i
            
            elif (val>=65 and val<=90) or (val>=97 and val<=122):
                temp=val-key
                if temp<97 and i.islower():
                    temp+=26
                if temp<65 and i.isupper():
                    temp+=26
                temp=chr(temp)
                resultant+=temp
            else:
                resultant+=i
        resultLabel.config(text=resultant+" \nkey ="+str(key))


        
   


def decrypt_text():
    TEXT=T.get("1.0","end-1c")
    Key=T2.get("1.0","end-1c")
    if Key=='':
        resultLabel.config(text="Enter Key")
    else:
        resultant=''
        Key=int(Key)
        for i in TEXT:
            
            val=ord(i)
            if i.isdigit():
                resultant+=i
            elif(val>=65 and val<=90) or (val>=97 and val<=122):
                temp=val+Key
                if temp>122 and i.islower():
                    temp-=26
                if temp>90 and i.isupper():
                    temp-=26
                temp=chr(temp)
                resultant+=temp
            else:
                resultant+=i
        resultLabel.config(text=resultant)
    
    

window=tkinter.Tk()
window.title("Ceasar Cipher Encryption/Decryption")
window.iconbitmap('hacker.ico')
window.geometry("790x790")
window.resizable(width=True,height=True)

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

user_name = tkinter.Label(window, text = "Caesar Cipher Encryption/Decryption",font=('Algerian',20,'bold'))
user_name.pack(side=tkinter.TOP)
empt=tkinter.Label(window,text="",height=5).pack()
user = tkinter.Label(window, text = "Enter Text : ",font=buttonFont).pack()                                                                                         

T=tkinter.Text(window,height=2,width=50)
T.pack()

user2 = tkinter.Label(window, text = "Enter Key (Only For Decryption) : ",font=buttonFont).pack()                                                                                         

T2=tkinter.Text(window,height=2,width=50)
T2.pack()

emp=tkinter.Label(window,text="",height=5).pack()


btn1=tkinter.Button(window,text="Encrypt",font=buttonFont,height=2,width=15,command=lambda:encrypt_text()).pack()
btn2=tkinter.Button(window,text="Decrypt",font=buttonFont,height=2,width=15,command=lambda:decrypt_text()).pack()

empt=tkinter.Label(window,text="",height=5).pack()

resultLabel = tkinter.Label(window, text = "",font=buttonFont)
resultLabel.pack()

window.mainloop()