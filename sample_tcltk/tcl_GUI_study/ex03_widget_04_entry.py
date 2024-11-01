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
        self.frame01 = tk.Frame(self.master, relief='groove', borderwidth=1)  # relief=枠線スタイル bd=枠線太さ
        self.frame02 = tk.Frame(self.master, relief='groove', borderwidth=1)  # relief=枠線スタイル bd=枠線太さ

        # 部品配置
        self.frame00.grid(row=0, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")
        self.frame01.grid(row=1, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")
        self.frame02.grid(row=2, column=0, padx=self.g_padx, pady=self.g_pady, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 列数＝1なので使ってないので 1つだけ設定
        #self.master.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # ウィンドウ全体がリサイズされた時に、内部部品も追従するようにする
        # 効かないので一旦コメントアウト # self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        # -------------------------
        # Entry 4
        # 部品定義
        self.label4 = ttk.Label(self.frame00, text="■ Entry")
        self.entry4 = ttk.Entry(self.frame01)
        self.entry4.bind('<Return>', self.func_on_entry4_editingFinished)
        self.button4_1 = ttk.Button(self.frame01, text="input", command=self.func_on_button4_1_clicked)
        self.button4_2 = ttk.Button(self.frame01, text="output", command=lambda: tk.messagebox.showinfo("title_dialog", self.entry4.get()))
        #
        self.entry4_3 = ttk.Entry(self.frame02, state='readonly')
        self.button4_3 = ttk.Button(self.frame02, text="1段目入力欄の値を反映", command=self.func_on_button4_3_clicked)
        # 部品配置
        self.label4.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry4.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button4_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button4_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry4_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button4_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_on_button4_1_clicked(self):
        self.entry4.delete(0, tk.END)  # テキストボックスクリア
        self.entry4.insert(tk.END, 'test input1')

    def func_on_button4_3_clicked(self):
        self.entry4_3['state'] = 'normal'  # readonlyにしているものは書き換え前に一旦 normalにする必要あり
        self.entry4_3.delete(0, tk.END)  # テキストボックスクリア
        self.entry4_3.insert(tk.END, 'test input1')
        self.entry4_3['state'] = 'readonly'

    def func_on_entry4_editingFinished(self, e):
        # bindで呼び出される関数は 引数に e （Event引数）が必要
        tk.messagebox.showinfo("info", self.entry4.get() + "が入力されました")

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()