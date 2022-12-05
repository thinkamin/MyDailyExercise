import tkinter as tk
from tkinter import ttk

def xfunc(event):
    print('事件触发键盘输入：{},对应的ascii码：{}'.format(event.char,event.keycode))
root = tk.Tk()
root.geometry('600x500+200+20')
'''
响应所有事件(键盘)
<key>所有键盘按键都会触发
'''
label =tk.Label(root,text='hello')
label.focus_set()
label.pack()
label.bind('<Key>',xfunc)
root.mainloop()
