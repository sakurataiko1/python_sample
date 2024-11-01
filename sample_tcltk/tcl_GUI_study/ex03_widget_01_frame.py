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

        #==========================
        # Frmame and LabelFrame
        # 部品定義
        self.label00_1 = ttk.Label(self.frame00, text="■ Frame and LabelFrame")
        self.frame00_1 = ttk.Frame(self.frame00, width=200, relief='groove', borderwidth=1)
        self.button00_1 = ttk.Button(self.frame00_1, text="button1")
        self.frame00_2 = ttk.Frame(self.frame00, width=200, height="50", relief='groove', borderwidth=1)
        self.frame00_2.propagate(False) # frameサイズを、中に配置された部品のサイズに自動設定する設定をOFFする。デフォルトではONで、width設定しても無効になる。
        self.button00_2 = ttk.Button(self.frame00_2, text="button2")
        self.labelframe00_1 = ttk.LabelFrame(self.frame00, text="LabelFrame") # relief='groove', borderwidth=1)
        self.button00_3 = ttk.Button(self.labelframe00_1, text="button1")
        # 部品配置
        self.label00_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')  # anchorで左寄せ
        self.frame00_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button00_1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor="w")
        self.frame00_2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button00_2.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='nw') # anchorで左・上寄せ
        self.labelframe00_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button00_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()