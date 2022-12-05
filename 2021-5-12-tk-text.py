import tkinter as tk 
root = tk.Tk()
input_label = tk.Label(text='input')
input_label.pack()
input_text = tk.Text(root)
input_text.pack()
input_label = tk.Label(text='output')
input_label.pack()
output_text = tk.Text(root)
output_text.pack()
def add_string(event=None):
    text = input_text.get(1.0,tk.END)
    if len(text)>0:
        output_text.insert('end',text)
    input_text.delete(1.0,tk.END)
root.bind('<Return>',add_string)

root.mainloop()
