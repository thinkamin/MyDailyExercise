import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root,borderwidth=2)
frame.pack(fill=tk.BOTH,expand=1)
label = tk.Label(frame,text='hello,world')
label.pack(fill=tk.X,expand=1)
button = tk.Button(frame,text='Exit',command=root.destroy)
button.pack(side=tk.BOTTOM)
tk.mainloop()

