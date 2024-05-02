import os

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("sample wintop scrollbar")
        #self.master.geometry("2000x1500")  # (1300x600)  必ず、全部の部品が見えるサイズ以上にする
        self.g_winsizeW = 1000
        self.g_winsizeH = 2000
        str_sizeWH = str(self.g_winsizeW) + "x" + str(self.g_winsizeH)
        self.master.geometry(str_sizeWH)

        # -start- 全体スクロールバー設定
        self.canvas_wintop = tk.Canvas(self.master)
        self.frame_wintop = tk.Frame(self.canvas_wintop)
        self.scrollbarV = tk.Scrollbar(
            self.canvas_wintop, orient=tk.VERTICAL, command=self.canvas_wintop.yview
        )
        # スクロールの設定
        self.canvas_wintop.configure(scrollregion=(0, 0, self.g_winsizeW, self.g_winsizeH))
        self.canvas_wintop.configure(yscrollcommand=self.scrollbarV.set)

        # 水平方向スクロールバー
        self.scrollbarH = tk.Scrollbar(
            self.canvas_wintop, orient=tk.HORIZONTAL, command=self.canvas_wintop.xview
        )
        self.canvas_wintop.configure(xscrollcommand=self.scrollbarH.set)

        # 諸々を配置
        self.scrollbarV.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbarH.pack(side=tk.BOTTOM, fill=tk.X)  # 水平方向スクロールバー
        self.canvas_wintop.pack(expand=True, fill=tk.BOTH)

        # Canvas上の座標(0, 0)に対してFrameの左上（nw=north-west）をあてがうように、Frameを埋め込む
        self.canvas_wintop.create_window((0, 0), window=self.frame_wintop, anchor="nw", width=self.g_winsizeW, height=self.g_winsizeH)
        # -end- 全体スクロールバー設定

        # 全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = tk.Frame(self.frame_wintop, relief='groove', bd=2)  # relief=枠線スタイル bd=枠線太さ
        self.frame01 = tk.Frame(self.frame_wintop, relief='groove', bd=2)
        # 配置　フレーム
        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky="nsew") # DEBUGメニュー
        self.frame01.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")  # プロット画面と上下メニュー
        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        for i in range(3):
            #root.rowconfigure(i, weight=1)
            root.columnconfigure(i, weight=1)
        root.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # 部品定義　1段目
        self.button1 = ttk.Button(self.frame00, text="テスト")
        # 部品配置　1段目
        self.button1.pack(side='left')

        # 部品定義　2段目
        self.canvas1 = tk.Canvas(self.frame01)
        # 部品配置　2段目
        self.canvas1.pack(side="left", fill="both", expand=True, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()