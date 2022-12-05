import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root,text='输入')
label1.pack()
input_text = tk.Text(root)
input_text.pack()
out_text = tk.Text(root)
out_text.pack()
button1 = tk.Button(root,text='exit',command=exit)
button1.pack()
def add_string(event=None):
    text = input_text.get(1.0,tk.END)
    if len(text)>0:
        out_text.insert('end',text)
    input_text.delete(1.0,tk.END)
root.bind('<Return>',add_string)
def exit():
    root.destroy()
    


root.mainloop()


