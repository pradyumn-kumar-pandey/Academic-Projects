import tkinter
from PIL import Image
from PIL import ImageTk

import os
import tkinter.filedialog


def cancel_scrn(f):
    f.destroy()
    main()
    

def decode(image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data




def image_select_dec(f):
    new_frame=tkinter.Frame(window)
    new_frame.pack()

    myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
    if not myfile:
        tkinter.messagebox.showerror("Error","Please Select Something!")
    else:
        Intro_lbl=tkinter.Label(new_frame,text="Image Steganography",font=('Algerian',24))
        Intro_lbl.pack()
        myimg = Image.open(myfile, 'r')
        myimage = myimg.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l4= tkinter.Label(new_frame,text='Image You Selected:')
        l4.pack()
        panel = tkinter.Label(new_frame, image=img)
        panel.image = img
        panel.pack()
        hidden_data = decode(myimg)
        space_lbl=tkinter.Label(new_frame,text='')
        space_lbl.pack()
        l2 = tkinter.Label(new_frame, text='Decoded Data:')
        l2.pack()
        text_area = tkinter.Text(new_frame, width=30, height=10)
        text_area.insert(tkinter.INSERT,hidden_data)
        text_area.pack()
        
        space_lbl=tkinter.Label(new_frame,text='')
        space_lbl.pack()
        back_button = tkinter.Button(new_frame, text='Cancel', command= lambda :cancel_scrn(new_frame))
        back_button.pack()

        f.destroy()


    
def dec(f):
    f.destroy()
    
    new_f=tkinter.Frame(window)
    new_f.pack()
    
    space_lbl=tkinter.Label(new_f,text='')
    space_lbl.pack()
    
    Intro_lbl=tkinter.Label(new_f,text="Image Steganography",font=('Algerian',24))
    Intro_lbl.pack()
    space_lbl=tkinter.Label(new_f,text='')
    space_lbl.pack()
    
    img_slct=tkinter.Button(new_f,text='Select Image To Decode',command=lambda:image_select_dec(new_f))
    img_slct.pack()
    
    space_lbl=tkinter.Label(new_f,text='')
    space_lbl.pack()
    
    cancel_btn=tkinter.Button(new_f,text='Cancel',command=lambda:cancel_scrn(new_f))
    cancel_btn.pack()
    
 


def genData(data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd


def modPix(pix,data):
        datalist = genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            # Eigh^th pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
            
def encode_enc(newimg,data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1
def enc_fun(text_area,myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            tkinter.messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            encode_enc(newimg, data)

            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            d_image_w,d_image_h = newimg.size
            tkinter.messagebox.showinfo("Success","Encoding Successful\nFile is savaved in the same directory")

def image_select_enc(f):
        ep= tkinter.Frame(window)
        ep.pack()
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            tkinter.messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= tkinter.Label(ep,text='Selected Image')
            l3.pack()
            panel = tkinter.Label(ep, image=img)
            panel.image = img
            panel.pack()
            l2 = tkinter.Label(ep, text='Enter the message')
            l2.pack()
            text_area =tkinter.Text(ep, width=50, height=10)
            text_area.pack()
            encode_button = tkinter.Button(ep, text='Cancel', command=lambda : cancel_scrn(ep))
            
            back_button = tkinter.Button(ep, text='Encode', command=lambda : [enc_fun(text_area,myimg),cancel_scrn(ep)])
            back_button.pack()
            encode_button.pack()
            f.destroy()


def enc(f):
    f.destroy()
    new_f=tkinter.Frame(window)
    new_f.pack()
    
    space_lbl=tkinter.Label(new_f,text='')
    space_lbl.pack()
    
    Intro_lbl=tkinter.Label(new_f,text="Image Steganography",font=('Algerian',24))
    Intro_lbl.pack()
    
    img_slct=tkinter.Button(new_f,text='Select Image To Encode',command=lambda:image_select_enc(new_f))
    img_slct.pack()
    
    space_lbl=tkinter.Label(new_f,text='')
    space_lbl.pack()
    
    cancel_btn=tkinter.Button(new_f,text='Cancel',command=lambda:cancel_scrn(new_f))
    cancel_btn.pack()
    


window=tkinter.Tk()

def main():
    window.title("Image Steganography")
    window.geometry('500x600')
    window.resizable(width=True,height=True)
    
    window.iconbitmap('hacker.ico')
    frame=tkinter.Frame(window)
    frame.pack()
    Intro_lbl=tkinter.Label(frame,text="Image Steganography",font=('Algerian',24))
    Intro_lbl.pack()
    
    space_lbl=tkinter.Label(frame,text='')
    space_lbl.pack()
    encode_btn=tkinter.Button(frame,text="Encode",command=lambda:enc(frame))
    encode_btn.pack()
    
    space_lbl=tkinter.Label(frame,text='')
    space_lbl.pack()
    
    decode_btn=tkinter.Button(frame,text="Decode",command=lambda:dec(frame))
    decode_btn.pack()

   
main()
window.mainloop()
