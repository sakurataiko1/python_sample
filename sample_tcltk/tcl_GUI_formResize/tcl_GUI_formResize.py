import os
import tkinter as tk
import tkinter.messagebox as tk_msgbox

from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("GUIlayout_expand")
        self.master.geometry("400x300")

        # 全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = tk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame01 = tk.Frame(self.master, relief='groove', borderwidth=2)

        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")  # sticky設定でウィンドウ全体リサイズに追従させる
        self.frame01.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # ユーザーによる画面リサイズ時にウィジェット大きさが追従するように設定
        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        #for i in range(1):
        #   root.columnconfigure(i, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1) # 画面リサイズ時の、部品リサイズ追従は 3=canvasのみ

        # -------------------------
        # Labelframe and Label 1, 2
        # 0行目
        # 部品定義
        self.button1 = tk.Button(self.frame00, text="テスト", command=self.func_button1_clicked)
        # 部品配置
        self.button1.pack(side='left')

        # 0行目
        # 部品定義
        self.canvas1 = tk.Canvas(self.frame01, relief='groove', borderwidth='2')
        # 部品配置
        self.canvas1.pack(side='left', fill="both", expand=True)  # fill, expand設定で配置箇所いっぱいに広げる

    def func_button1_clicked(self):
        tk.messagebox.showinfo("[DEBUG]cliked")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
