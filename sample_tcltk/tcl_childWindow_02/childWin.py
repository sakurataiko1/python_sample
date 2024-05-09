#参考 https://qiita.com/hatorijobs/items/ddd435d749cd97581a6c

import tkinter as tk
from tkinter import messagebox

import datetime

class ChildWindow:
    def __init__(self, master, parent, mode):
        #super().__init__(master)
        self.master = master
        self.parent = parent
        self.mode = mode

        self.window = None

        self.g_cnt = 0

        print("[DEBUG]childWin.py __init__")

    def func_init_01(self):
        self.create_widgets()
        self.window.mainloop()

    # -start- org
    # def this_window_close(self):
    #     self.window.withdraw()
    #     # ↓これをしないと、子ウィンドウを閉じた後に、再度開くことが出来なくなる。
    #     self.window = None
    #     return "break"
    # -end- org

    def this_window_close(self):
        self.window.withdraw()
        # ↓これをしないと、子ウィンドウを閉じた後に、再度開くことが出来なくなる。
        #self.window = None
        self.parent.child_window1 = None # 親Windowで持っているChildWindow情報のリセット
        self.window.quit()  # エラーメッセージが出るがこれを入れないと、親ウィンドウで次の処理がされない self.window.mainloop()の終了
        self.window.destroy()
        return "break"

    def create_widgets(self):
        if not self.window:
            self.window = tk.Toplevel(self.master)

        # ×ボタンの処理をカスタマイズする
        self.window.protocol('WM_DELETE_WINDOW', self.this_window_close)

        #self.geometry(str(400) + "x" + str(200) + "+" + str(400) + "+" + str(400))
        self.window.geometry("600x200+400+400")
        self.window.title("child window")

        # 部品定義　全体レイアウトのためのフレーム
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.frame5 = tk.Frame(self.window)
        # 部品配置　全体レイアウトのためのフレーム
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.frame4.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.frame5.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        if self.mode == 1:
            self.label1 = tk.Label(self.frame1, text="Mode 1: Label 1")
            self.label1.pack(side='left')
        elif self.mode == 2:
            self.label2 = tk.Label(self.frame2, text="Mode 2: Label 2")
            self.label2.pack(side='left')
        else:
            self.label_invalid = tk.Label(self.frame3, text="Invalid Mode")
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
        #self.button_close = tk.Button(self.frame5, text="子ウィンドウを閉じる", command=lambda: self.window.destroy())
        self.button_close = tk.Button(self.frame5, text="子ウィンドウを閉じる", command=self.this_window_close)
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

    def func_on_buttonC1_clicked(self):
        DEBUGstr = "[DEBUG]childWin.py func_on_buttonC1_clicked "
        tk.messagebox.showinfo("info", "[DEBUG] child buttonC1 clicked" )