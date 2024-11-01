#
# ■　python GUI tkinter ウィンドウ全体リサイズ時にウィジェットサイズも伸縮させる
# ユーザーがウィンドウサイズを横に広げた時
# entry1 はそれに応じて横幅が広がるように
# label1, button1はサイズが変わらないようにする
#

import os
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Resizable Entry Example")
        #self.master.geometry("600x400")

        self.g_padx=2
        self.g_pady=2

        self.func_create_widget()

    def func_create_widget(self):
        # 全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = tk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")  # sticky設定でウィンドウ全体リサイズに追従させる
        # ユーザーによる画面リサイズ時にウィジェット大きさが追従するように設定
        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(2, weight=1) # 画面リサイズ時の、部品リサイズ追従は frame02=canvasのみ

        # ウィジェット配置
        self.master.grid_columnconfigure(0, weight=1)

        label1 = ttk.Label(self.frame00, text="入力")
        label1.pack(side="left")

        entry1 = ttk.Entry(self.frame00)
        entry1.pack(side="left", fill="x", expand=True)

        button1 = ttk.Button(self.frame00, text="選択")
        button1.pack(side="left")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()

