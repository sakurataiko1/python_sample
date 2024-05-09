
#参考 https://qiita.com/hatorijobs/items/ddd435d749cd97581a6c

import tkinter as tk
from tkinter import messagebox
import childWin

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.geometry(str(320) + "x" + str(200) + "+" + str(200) + "+" + str(200))
        self.master.geometry("350x400+200+200")
        self.master.title("parent window")

        self.child_window1 = None  # ChildWindowのインスタンスを保持するための変数

        self.g_parent_str = ""

        self.create_widgets()

    def create_widgets(self):
        # 部品定義
        msg = '子ウィンドウ起動　複数起動なし(既に起動していたら起動しない）\n'
        msg += '子ウィンドウが閉じるまでは、親ウィンドウは次の処理に進みません\n子ウィンドウが閉じたらメッセージが表示されます'
        self.labelP1 = tk.Label(self, text=msg)
        self.buttonP1 = tk.Button(self, text="子ウィンドウ起動 1", command=self.func_on_buttonP1_clicked)

        # 部品配置
        self.labelP1.pack(side='top', anchor='w', padx=5, pady=5)
        self.buttonP1.pack(side='top', anchor='w', padx=5, pady=5)

        # 部品定義
        self.button2 = tk.Button(self, text="子ウィンドウ起動 2", command=lambda: self.open_child_window1(2))
        self.button3 = tk.Button(self, text="子ウィンドウ起動 3", command=lambda: self.open_child_window1(3))
        self.button4 = tk.Button(self, text="子ウィンドウ起動 4", command=lambda: self.open_child_window1(4))
        self.button5 = tk.Button(self, text="子ウィンドウ起動 5", command=lambda: self.open_child_window1(5))
        # 部品配置
        self.button2.pack(side='top', anchor='w', padx=5, pady=5)
        self.button3.pack(side='top', anchor='w', padx=5, pady=5)
        self.button4.pack(side='top', anchor='w', padx=5, pady=5)
        self.button5.pack(side='top', anchor='w', padx=5, pady=5)

        # 部品定義
        self.label1 = tk.Label(self, text='子ウィンドウへの情報送付欄')
        self.entry_p1 = tk.Entry(self)
        # 部品配置
        self.label1.pack(side='top', anchor='w')  #　左寄せ: anchor='w'
        self.entry_p1.pack(side='top', anchor='w')
        #
        self.entry_p1.insert(0,"from paretn test01")

        # 部品定義
        self.label2 = tk.Label(self, text='子ウィンドウから情報受け取り 01')
        self.entry_p2 = tk.Entry(self)
        # 部品配置
        self.label2.pack(side='top', anchor='w')
        self.entry_p2.pack(side='top', anchor='w')

        # 部品定義
        self.label3 = tk.Label(self, text='子ウィンドウから情報受け取り 02')
        self.entry_p3 = tk.Entry(self)
        # 部品配置
        self.label3.pack(side='top', anchor='w')
        self.entry_p3.pack(side='top', anchor='w')

    def func_on_buttonP1_clicked(self):
        self.open_child_window1(1)


    def open_child_window1(self, in_mode):
        DEBUGstr = "[DEBUG]00_mainWin.py func_on_button1_clicked "
        # ChildWindowが既に存在する場合はメッセージボックスで通知し、新たに開かないようにする
        if self.child_window1 is not None:
            messagebox.showinfo("Info", "Child Window is already open.")
        else:
            if(in_mode == 1):
                print(DEBUGstr, " 01")
                mode = '01'
                self.child_window1 = childWin.ChildWindow(self.master, self, in_mode)
                self.child_window1.func_init_01()
            if(in_mode == 2):
                self.child_window1 = childWin.ChildWindow(self.master, self, in_mode)
                self.child_window1.func_init_01()  # 引数：in_mode で子ウィンドウの表示や処理を切り替える
            if(in_mode == 3):
                self.child_window1 = childWin.ChildWindow(self.master, self, in_mode)
                self.child_window1.func_init_01()  # 引数　in_mode で子ウィンドウの表示や処理を切り替える
            if(in_mode == 4 ):
                self.child_window1 = childWin.ChildWindow(self.master, self, in_mode)
                list1 = ['4_1_1', '4_1_2']
                list2 = ['4_2_1', '4_2_2']
                self.child_window1.func_init_04(list1, list2)  #　子ウィンドウ側の別関数を呼び出すことで、子ウィンドウの表示や処理を切り替える　渡したい引数を多数渡せる
            if(in_mode == 5 ):
                list1 = ['5_1_1', '5_1_2']
                list2 = ['5_2_1', '5_2_2']
                str1 = "test5"
                self.child_window1 = childWin.ChildWindow(self.master, self, in_mode)
                self.child_window1.func_init_05(list1, list2, str1)  # 子ウィンドウ側の別関数を呼び出すことで、子ウィンドウの表示や処理を切り替える　渡したい引数を多数渡せる

            msg = "子ウィンドウが閉じられました。親ウィンドウの処理が再開されます"
            print(DEBUGstr, msg)
            tk.messagebox.showinfo("info", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.pack()
    app.mainloop()
