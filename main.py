import tkinter as tk
from tkinter import messagebox
import os
tk.textDnD = True


OutNum =1

# 创建一个窗口对象
root = tk.Tk()

# 设置窗口大小和标题
root.geometry("750x600")
root.title("YouGet工具包1.0")

def onSave():
    messagebox.showinfo("YouGet的温馨提示：", "微信：13262333362")

def onOpen():
    messagebox.showinfo("YouGet的温馨提示：", "官网：http://youget.vip")

def OutText():
    global OutNum

    with open( str(OutNum) + '.txt', 'w') as f:

        f.write(text2.get("1.0", tk.END))
        OutNum += 1
    messagebox.showinfo("YouGet的温馨提示：", "导出成功！")
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="官网", command=onOpen)
filemenu.add_command(label="联系作者", command=onSave)
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="菜单", menu=filemenu)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="导出", command=OutText)
menubar.add_cascade(label="功能", menu=filemenu)
root.config(menu=menubar)



def cmd_exec(event):
    text2.delete('1.0',tk.END)
    command = text.get("1.0", tk.END)

    print(command)
    result = os.popen(command).read()
    #label.config(text=result)
    text2.insert(tk.END, result)

    #text.insert(tk.END,'1')
    #text2.config(text=result)
    #text2.xview_scroll(200, tk.CHARACTERS)
    #content = text.get('1.0', tk.END)  # 获取文本框中的内容
    #print(f"输入内容为：{content}")
    text.delete('1.0', tk.END)  # 清空文本框
    text.insert(tk.END, event.char)
    text.focus_set()
    #text.mark_set(tk.INSERT, "1.end")
    #text.see(tk.INSERT)
    #text.delete('1.0', tk.END)  # 清空文本框
    return "break"
# 创建标签和按钮控件
label1 = tk.Label(root, text="输入命令，回车执行 :")
label = tk.Label(root, text="命令执行结果 :")
text = tk.Text(root,width=20,height=1,font=20)#,wrap="none",insertwidth=0
text2 = tk.Text(root,width=80,height=30,font=1)
#button = tk.Button(root, text="执    行", command=lambda: print("Button clicked!"),width=20,height=2)
#button = tk.Button(root, text="执    行", command=cmd_exec,width=10,height=1)

text.bind('<Key-Return>', cmd_exec) # 绑定回车键事件







# 将控件添加到窗口上
label.pack()
#button.pack()

#label.pack()
label1.place(x=50,y=20)
label.place(x=50,y=80)
text.place(x=50,y=50)
text2.place(x=50,y=100)
#button.place(x=200,y=50)
#button.pack(side='left')

"""
def update_mouse_pos(event):
    x, y = event.x_root, event.y_root  # 获取鼠标在屏幕上的坐标
    label.config(text=f"Mouse position: ({x}, {y})")

root.bind("<Motion>", update_mouse_pos)  # 绑定鼠标移动事件
"""
































# 进入消息循环，等待用户操作
root.mainloop()