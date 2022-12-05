import tkinter as tk
from tkinter import ttk

def xfunc(event):
    print('事件触发键盘输入：{},对应的ascii码：{}'.format(event.char,event.keycode))
root = tk.Tk()
root.geometry('600x500+200+20')
'''
组合所有事件
<Control-Alt-x>
<Shift-Up>
<Control-p>
'''
label =tk.Label(root,text='hello')
label.focus_set()
label.pack()
label.bind('<Control-p>',xfunc)
root.mainloop()
