import tkinter as tk
root = tk.Tk()
input_label = tk.Label(text='input')
input_label.pack()
text1 = tk.Text(root)
text1.pack()
output_label = tk.Label(text='output')
output_label.pack()
text2 = tk.Text(root)
text2.pack()
def add_string(event=None):
    text = text1.get(1.0,tk.END)
    if len(text)>0:
        text2.insert('end',text)
    text1.delete(1.0,tk.END)
root.bind('<Return>',add_string)


root.mainloop()


