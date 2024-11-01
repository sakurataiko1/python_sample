import os
import tkinter as tk
from tkinter import font
from tkinter import ttk

import ex05_2_subDialog01
import ex05_3_subDialog02_1_WinScroll

class MainWindow(tk.Frame):
    #　 プログラム内容
    #      Window全体にスクロールバーを設定する
    #
    def __init__(self, master=None):
        super().__init__(master)

        self.g_padx = 2 #　ウィジェット配置の余白
        self.g_pady = 2

        self.dialog1 = None
        self.dialog2 = None

        # GUIレイアウト
        self.func_create_GUI()

    def func_create_GUI(self):
        # 全体レイアウトのためのフレーム　縦にならべる(row)
        # 部品定義
        self.frame00 = tk.Frame(self.master, relief='groove', borderwidth=1)  # relief=枠線スタイル bd=枠線太さ
        self.frame01 = tk.Frame(self.master, relief='groove', borderwidth=1)  # relief=枠線スタイル bd=枠線太さ

        # 部品配置
        self.frame00.grid(row=0, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")
        self.frame01.grid(row=1, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 列数＝1なので使ってないので 1つだけ設定
        self.master.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # ウィンドウ全体がリサイズされた時に、内部部品も追従するようにする
        # 効かないので一旦コメントアウト # self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        # frame00
        # 部品定義
        self.button1 = ttk.Button(self.frame00, text="ダイアログ起動", command=self.func_button1_clicked) # 関数に()はつけてはいけない　# lamda付けない場合、引数指定不可
        self.entry1= ttk.Entry(self.frame00)
        self.button1_2 = ttk.Button(self.frame00, text="ダイアログに値設定", command=self.func_button1_2_clicked)
        # 部品配置
        self.button1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button1_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # frame01
        # 部品定義
        self.button2 = ttk.Button(self.frame01, text="ダイアログ起動(スクロールバーあり）", command=self.func_button2_clicked) # 関数に()はつけてはいけない　# lamda付けない場合、引数指定不可
        # 部品配置
        self.button2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_button1_clicked(self):
        # 　子ウィンドウとしてプログラム起動
        # ダイアログの2重起動防止　既に起動していたら2重起動しない
        if self.dialog1 != None:
            return
        # ダイアログ起動
        self.dialog1 = ex05_2_subDialog01.subDialog01(self.master, self)
        tmp_str = "test"
        self.dialog1.init_ui_dialog1(tmp_str)
        self.dialog1 = None  # ダイアログ画面が閉じたらNoneにする

    def func_button1_2_clicked(self):
        if self.dialog1 == None:
            return
        #
        self.dialog1.lineEdit01.delete(0, tk.END)
        self.dialog1.lineEdit01.insert(0, self.entry1.get())

    def func_button2_clicked(self):
        # 　子ウィンドウとしてプログラム起動
        # ダイアログの2重起動防止　既に起動していたら2重起動しない
        if self.dialog2 != None:
            return
        # ダイアログ起動
        self.dialog2 = ex05_3_subDialog02_1_WinScroll.subDialog02_1_WinScroll(self.master, self)
        self.dialog2.func01_init_ui_dialog2()
        self.dialog2 = None  # ダイアログ画面が閉じたらNoneにする

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()