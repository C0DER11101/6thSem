import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


root=Tk();

frame=Frame(root);

lbl_pic_path=Label(frame, text='Image path:', padx=25, pady=25, font=('verdana', 16));
lbl_show_pic=Label(frame);

entry_pic_path=Entry(frame, font=('verdana', 16));

btn_browse=Button(frame, text='Select image:', bg='gray', fg='white', font=('verdana', 16));

def selectPic():
    global img
    filename=filedialog.askopenfilename(initialdir="/Desktop", title="Select image", filetypes=(("png images", "*.png"),("jpg images", "*.jpg")));
    img=Image.open(filename);
    img=img.resize((400, 400), Image.ANTIALIAS);
    img=ImageTk.PhotoImage(img);
    lbl_show_pic['image']=img;
    entry_pic_path.insert(0, filename);
    return;
btn_browse['command']=selectPic;

frame.pack();

lbl_pic_path.grid(row=0, column=0);

entry_pic_path.grid(row=0, column=1, padx=(0, 20));

lbl_show_pic.grid(row=1, column=0, columnspan="2");

btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10);

root.mainloop();
