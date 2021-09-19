from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os
import idcheck

class IDCheckGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("身份证信息校验系统")
        self.geometry("800x510+400+200")
        self.resizable(0,0)
        self["bg"] = "whitesmoke"
        self.setup_UI()

    def setup_UI(self):
        self.style01 = Style()
        self.style01.configure("input.TLabel",font=("微软雅黑",20,"bold"))
        self.style01.configure("TLabel",font=("微软雅黑",20,"bold"),foreground = "navy")
        self.style01.configure("TButton",font=("微软雅黑",20,"bold"),background = "lightblue")

        # 图片
        self.Login_image = PhotoImage(file = "."+os.sep+"img"+os.sep+"id2.png")
        self.Label_image = Label(self,image = self.Login_image)
        self.Label_image.place(x=5,y=5)
        # 输入信息
        self.Label_id_input = Label(self,text = "请输入身份证号码:",style="input.TLabel")
        self.Label_id_input.place(x=400,y=20)
        self.var_input = StringVar()
        self.Entry_id_input = Entry(self,textvariable = self.var_input,width=20,font=("微软雅黑",18,"bold"))
        self.Entry_id_input.place(x = 400,y=70)
        self.Button_id_input = Button(self,text="校验",command = self.get_info)
        self.Button_id_input.place(x = 660,y = 70)
        # 具体信息
        self.Label_is_exsit = Label(self,text = "是否有效：")
        self.Label_is_exsit.place(x=400,y=170)
        self.var_enable = StringVar()
        self.Entry_is_exsit = Entry(self, state=DISABLED,textvariable=self.var_enable, width=10, font=("微软雅黑", 18, "bold"))
        self.Entry_is_exsit.place(x=530, y=165)

        self.Label_is_gender = Label(self, text="性       别：")
        self.Label_is_gender.place(x=400, y=220)
        self.var_gender = StringVar()
        self.Entry_is_gender = Entry(self, state=DISABLED,textvariable=self.var_gender, width=10, font=("微软雅黑", 18, "bold"))
        self.Entry_is_gender.place(x=530, y=215)

        self.Label_is_birthday = Label(self, text="出生日期：")
        self.Label_is_birthday.place(x=400, y=270)
        self.var_birthday = StringVar()
        self.Entry_is_birthday = Entry(self, state=DISABLED,textvariable=self.var_birthday, width=18, font=("微软雅黑", 19, "bold"))
        self.Entry_is_birthday.place(x=530, y=265)

        self.Label_is_area = Label(self, text="所  在  地：")
        self.Label_is_area.place(x=400, y=320)
        self.var_area = StringVar()
        self.Entry_is_area = Entry(self,state=DISABLED, textvariable=self.var_area, width=18, font=("微软雅黑", 19, "bold"))
        self.Entry_is_area.place(x=530, y=315)

        self.Button_close = Button(self,text = "关闭",command = self.close_window)
        self.Button_close.place(x = 650, y= 450)

    def close_window(self):
        self.destroy()

    def get_info(self):
        id_number = self.var_input.get()
        if len(id_number) == 18:
            check_id = idcheck.IdCheck(id_number)
            if check_id.is_true_id_number == 0 or len(check_id.birthday) == 0 or len(check_id.area_name) == 0:
                self.var_enable.set("无效!")
            else:
                self.var_enable.set("有效")
                self.var_gender.set(check_id.gender)
                self.var_birthday.set(check_id.birthday)
                self.var_area.set(check_id.area_name)
        else:
            self.var_enable.set("无效")
            self.var_gender.set("")
            self.var_birthday.set("")
            self.var_area.set("")
            showinfo("系统消息", "输入的身份证号码不满18位，请重新输入！")


