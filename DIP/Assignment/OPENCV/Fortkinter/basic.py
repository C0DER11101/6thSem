import tkinter as tk

root=tk.Tk();
root.title("Vehicle number plate detection");
root.geometry("640x640");

label=tk.Label(root, text="Welcome to vehicle number plate detection", width=300, height=150, bg="black", fg="yellow");
label.pack();

root.mainloop();
