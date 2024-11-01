import os
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog

class MainWindow(tk.Frame):
    #　 プログラム内容
    #      Window全体にスクロールバーを設定する
    #
    def __init__(self, master=None):
        super().__init__(master)

        self.g_padx = 2 #　ウィジェット配置の余白
        self.g_pady = 2

        # GUIレイアウト
        self.func_create_GUI()

    def func_create_GUI(self):
        # 全体レイアウトのためのフレーム　縦にならべる(row)
        # 部品定義
        self.frame00 = tk.Frame(self.master, relief='groove', borderwidth=1)  # relief=枠線スタイル bd=枠線太さ

        # 部品配置
        self.frame00.grid(row=0, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 列数＝1なので使ってないので 1つだけ設定
        self.master.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # ウィンドウ全体がリサイズされた時に、内部部品も追従するようにする
        # 効かないので一旦コメントアウト # self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        #-----------------------
        # ■　Listbox & ScrollBar"
        # 部品定義
        self.label_exListBox_1 = ttk.Label(self.frame00, text="■ Listbox & ScrollBar")
        self.scrollbar_frame = ttk.Frame(self.frame00)

        list_value = tk.StringVar()
        list_value.set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
        # selectmodeの種類(single:1つだけ選択できる、multiple:複数選択できる、extended：複数選択可能＋ドラッグでも選択可能)
        self.listbox_ex1 = tk.Listbox(self.scrollbar_frame, height=5, listvariable=list_value, selectmode="multiple")
        # 例まで、Listboxの内容設定は以下のようにもできる
        # for i in range(1000):
        #     self.listbox_ex1.insert(tk.END, i)
        self.scroll_bar = tk.Scrollbar(self.scrollbar_frame, command=self.listbox_ex1.yview)
        self.listbox_ex1.config(yscrollcommand=self.scroll_bar.set)
        self.button_exlb_result = ttk.Button(self.frame00, text="選択されたものを表示", command=self.func_on_button_exlb_result_clicked)
        self.button_exlb_allselect = ttk.Button(self.frame00, text="全選択", command=self.func_on_button_exlb_allselect_clicked)
        self.button_exlb_allclear = ttk.Button(self.frame00, text="全クリア", command=self.func_on_button_exlb_allclear_clicked)
        # 部品配置
        self.label_exListBox_1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.scrollbar_frame.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.listbox_ex1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.button_exlb_result.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.button_exlb_allselect.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.button_exlb_allclear.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')

    def func_on_button_exlb_result_clicked(self):
        # ボタンを押したら選択しているアイテムを表示する
        text_check = self.listbox_ex1.curselection()
        if(len(text_check) < 1):
            return
        tmpstr = ""
        for i in text_check:
            tmpstr += self.listbox_ex1.get(i) + " "
        tk.messagebox.showinfo("info", tmpstr + "\nが選択されました")

    def func_on_button_exlb_allselect_clicked(self):
        # 全選択する
        self.listbox_ex1.select_set(0, tk.END)   # 1～3番目を選択したい場合は (1, 3) のように書く

    def func_on_button_exlb_allclear_clicked(self):
        # 全クリアする
        self.listbox_ex1.select_clear(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()