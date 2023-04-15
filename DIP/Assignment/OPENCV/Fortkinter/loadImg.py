# loading images into tkinter!!

import tkinter as tk
from PIL import Image
from PIL import ImageTk

root=tk.Tk();
root.title("VNPD");

# 1st approach for loading an image
#photo=tk.PhotoImage(file="BreakTime.png"); # doesnot work with jpg images!!! :(
# 2nd approach for loading an image
photo2=Image.open("vehicle.jpg");
resized_image=photo2.resize((300, 500), Image.ANTIALIAS);
"""
(300, 500) in resize() is the size of the window!!
second argument in resize() is the re-sampling rate
"""

converted_image=ImageTk.PhotoImage(resized_image);

label=tk.Label(root, image=converted_image, width=300, height=500, bg="black", fg="yellow");
label.pack();

root.mainloop();
