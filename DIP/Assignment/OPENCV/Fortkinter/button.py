import tkinter as tk

def hello():
    print("Hello!\n");
    return;

root=tk.Tk();
root.geometry("640x640");

frame=tk.Frame(root, borderwidth=6, bg="gray", relief=tk.SUNKEN);
frame.pack(side=tk.LEFT, anchor="nw");

b1=tk.Button(frame, fg="red", text="Print now", command=hello); # when you will click on this button, then it will call hello() which will print "Hello!"
b1.pack();

root.mainloop();
