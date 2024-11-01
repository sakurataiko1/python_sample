#
# ■　python GUI tcl/tk ウィンドウ全体リサイズ時にフォームサイズも伸縮させる
# GUIレイアウト配置でgrid や　pack　のオプションを適切に設定して
# ユーザーがウィンドウをリサイズした際に配置された各部品(フォーム) が同時にサイズ伸縮するようにした例。
# 設定していないと、フォームのサイズが変わらず、違和感のある表示になってしまう。
#
import os
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("GUIlayout_expand")
        self.master.geometry("600x400")

        self.g_padx=2
        self.g_pady=2

        # 全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame01 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame02 = ttk.Frame(self.master, relief='groove', borderwidth=2)

        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")  # sticky設定でウィンドウ全体リサイズに追従させる
        self.frame01.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.frame02.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # ユーザーによる画面リサイズ時にウィジェット大きさが追従するように設定
        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 縦のリサイズ追従
        self.master.rowconfigure(2, weight=1)     # 横のリサイズ追従 # 画面リサイズ時の、部品リサイズ追従は frame02=canvasのみ

        # 補足　↑この例では1列のみなので columnconfigure で 0列目だけ設定しているが、複数行ある場合はその全てに設定する
        # 3列の場合
        # self.master.columnconfigure(0, weight=1)
        # self.master.columnconfigure(1, weight=1)
        # self.master.columnconfigure(2, weight=1)
        # もしくは
        #　for i in range(3):
        #   self.master.columnconfigure(i, weight=1)

        msg = "GUIレイアウト配置でgrid や　pack　のオプションを適切に設定して\n"
        msg += "ユーザーがウィンドウをリサイズした際に配置された各部品(フォーム) が同時にサイズ伸縮するようにした例\n"
        msg += "\n"
        msg += "設定していないと、フォームのサイズが変わらず、違和感のある表示になってしまう"

        # -------------------------
        # Labelframe and Label 1, 2
        # 0行目
        # 部品定義
        self.label1 = ttk.Label(self.frame00, text=msg, justify='left')  # justifyで複数行メッセージを左寄せ
        # 部品配置
        self.label1.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # 1行目
        # 部品定義
        self.button1 = ttk.Button(self.frame01, text="テスト1", command=self.func_button1_clicked)
        self.button2 = ttk.Button(self.frame01, text="テスト2", command=self.func_button2_clicked)
        # 部品配置
        self.button1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # 2行目
        # 部品定義
        self.canvas1 = tk.Canvas(self.frame02, relief='groove', borderwidth='2')
        # 部品配置
        self.canvas1.pack(side='left', fill="both", expand=True)  # fill, expand設定で配置箇所いっぱいに広げる

    def func_button1_clicked(self):
        tk.messagebox.showinfo("info", "[DEBUG]clicked 1")

    def func_button2_clicked(self):
        tk.messagebox.showinfo("info", "[DEBUG]clicked 2")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()


