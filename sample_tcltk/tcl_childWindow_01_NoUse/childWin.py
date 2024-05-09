import tkinter as tk

import datetime

class ChildWindow(tk.Toplevel):
    def __init__(self, master=None, parent=None, mode=None):
        super().__init__(master)
        self.master = master
        self.parent = parent

        #self.geometry(str(400) + "x" + str(200) + "+" + str(400) + "+" + str(400))
        self.geometry("400x200+400+400")
        self.title("child window")

        self.g_cnt = 0

        # 部品定義　全体レイアウトのためのフレーム
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame5 = tk.Frame(self)
        # 部品配置　全体レイアウトのためのフレーム
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.frame4.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.frame5.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        if mode == 1:
            self.label1 = tk.Label(self.frame1, text="Mode 1: Label 1")
            self.label1.pack(side='left')
        elif mode == 2:
            self.label2 = tk.Label(self.frame2, text="Mode 2: Label 2")
            self.label2.pack(side='left')
        else:
            self.label_invalid = tk.Label(self, text="Invalid Mode")
            self.label_invalid.pack(side='left')

        # 部品定義
        self.button_c1= tk.Button(self.frame3, text="親ウィンドウから情報取得", command=self.func_on_button_c1_clicked)
        self.entry_c1 = tk.Entry(self.frame3)
        # 部品配置
        self.button_c1.pack(side='left', padx=5, pady=5)
        self.entry_c1.pack(side='left', padx=5, pady=5)

        # 部品定義
        self.button_c2= tk.Button(self.frame4, text="親ウィンドウへ情報送付", command=self.func_on_button_c2_clicked)
        self.entry_c2 = tk.Entry(self.frame4)
        # 部品配置
        self.button_c2.pack(side='left', padx=5, pady=5)
        self.entry_c2.pack(side='left',  padx=5, pady=5)

        # 部品定義
        self.button_close = tk.Button(self.frame5, text="子ウィンドウを閉じる", command=lambda: self.destroy())
        # 部品配置
        self.button_close.pack(side='left', padx=5, pady=5)

        # 親に情報送付
        self.parent.g_parent_str = "from child:" + datetime.datetime.now().isoformat()

    def func_on_button_c1_clicked(self):
        msg = self.parent.entry_p1.get()
        self.entry_c1.delete(0, tk.END)
        self.entry_c1.insert(tk.END, msg)

    def func_on_button_c2_clicked(self):
        self.g_cnt += 1
        self.parent.entry_p2.delete(0, tk.END)
        self.parent.entry_p2.insert(0, "from child test1: " + str(self.g_cnt))
        self.parent.g_parent_str = "from child test2: " + str(self.g_cnt)
