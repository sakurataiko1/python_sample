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

        # -----------------------------------------------------
        # Checkbutton 5
        # 部品定義
        self.label5 = ttk.Label(self.frame00, text="■ CheckButton")
        self.GUIvalue_check5 = tk.BooleanVar(value=False)
        self.checkButton5 = ttk.Checkbutton(self.frame00, text="A", command=self.func_on_checkButton5_clicked, variable=self.GUIvalue_check5)
        self.entry5 = ttk.Entry(self.frame00, width=50)
        self.button_check5_1 = tk.Button(self.frame00, text="チェックボックスON", command=lambda: self.GUIvalue_check5.set(True))
        self.button_check5_2 = tk.Button(self.frame00, text="チェックボックスOFF", command=lambda: self.GUIvalue_check5.set(False))
        # 部品配置
        self.label5.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkButton5.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry5.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_check5_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_check5_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        #
        self.GUIvalue_check5.set(True) # デフォルト状態　チェックONにする


    def func_on_checkButton5_clicked(self):
        tmp_value = self.GUIvalue_check5.get()
        # print(f"チェックの状態は {self.value_check5} です")
        self.entry5.delete(0, tk.END)
        self.entry5.insert(tk.END, f"チェックの状態は {tmp_value} です")


if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()