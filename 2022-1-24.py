import tkinter as tk

root = tk.Tk()
root.geometry('500x500+100+200')
for i in range(3):
    btn = tk.Button(text=str(i))
    btn.pack(fill=tk.X)
root.mainloop()
