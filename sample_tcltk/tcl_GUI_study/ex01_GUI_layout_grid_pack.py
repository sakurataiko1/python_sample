#
#
#  参考URL gridについて： https://imagingsolution.net/program/python/tkinter/widget_layout_grid/
#  参考URL packについて:　https://imagingsolution.net/program/python/tkinter/widget_layout_pack/
#

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
        self.frame00 = ttk.Frame(self.master, relief='groove', borderwidth=2)  # relief=枠線スタイル bd=枠線太さ
        self.frame01 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame02 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame03 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        # 部品配置
        self.frame00.grid(row=0, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")
        self.frame01.grid(row=1, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")
        self.frame02.grid(row=2, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")
        self.frame03.grid(row=3, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 列数＝1なので使ってないので 1つだけ設定
        #self.master.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # ウィンドウ全体がリサイズされた時に、内部部品も追従するようにする
        # 効かないので一旦コメントアウト # self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        # -------------------------
        # ０行目　　横配置
        # 部品定義
        self.label1 = ttk.Label(self.frame00, text="■ 横配置")
        self.text1 = tk.Text(self.frame00, height=5)
        self.button1 = ttk.Button(self.frame00, text="button1")
        # 部品配置
        self.label1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.text1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.button1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')

        # -------------------------
        # 1行目　　縦配置
        # 部品定義
        self.label2 = ttk.Label(self.frame01, text="■ 縦配置")
        self.text2 = tk.Text(self.frame01, height=5)
        self.button2= ttk.Button(self.frame01, text="button2")
        # 部品配置
        self.label2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.text2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')

        # -------------------------
        # 2行目　　縦配置Fillで残り面積全て使うサイズにして配置
        # 部品定義
        self.label2 = ttk.Label(self.frame02, text="■ expandとfillで領域いっぱいのサイズにして配置")
        self.text2 = tk.Text(self.frame02, height=5)
        # 部品配置
        self.label2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.text2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w', expand=True, fill=tk.BOTH)

        # -------------------------
        # 2行目　packで縦、横　混在して配置　frame を入れ子にする  （gridで配置すると部品点数や場所が変わった時の対応に手間がいるので、packで配置した方が簡単）
        # 部品定義 フレーム
        self.frame03_1 = tk.Frame(self.frame03, relief='groove', borderwidth=2)
        self.frame03_2 = tk.Frame(self.frame03, relief='groove', borderwidth=2)
        self.frame03_3 = tk.Frame(self.frame03, relief='groove', borderwidth=2)
        # 部品配置　フレーム
        self.frame03_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.frame03_2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.frame03_3.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        #
        #　部品定義 & 配置　各Widget
        self.label3 = tk.Label(self.frame03_1, text="■ packで縦、横　混在して配置　frame を入れ子にする")
        self.label3.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='w')
        #
        self.entry3_2 = tk.Entry(self.frame03_2)
        self.button3_2 = tk.Button(self.frame03_2, text="button2")
        self.entry3_2.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button3_2.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='w')
        #
        self.entry3_3 = tk.Entry(self.frame03_3)
        self.button3_3 = tk.Button(self.frame03_3, text="button3")
        self.entry3_3.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button3_3.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='w')

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()