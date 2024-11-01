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
        # Label
        # 部品定義
        # -------------------------
        self.label01_1 = ttk.Label(self.frame00, text="■ Label")
        self.g_count_labelChange = 0
        self.label01_2 = ttk.Label(self.frame00, text="0")
        self.button01_labelChange = ttk.Button(self.frame00, text="ラベル書き換え", command=self.func_01_1_labelChange) # 関数に()はつけてはいけない
        self.button01_2 = ttk.Button(self.frame00, text="ラベルテキスト表示", command=lambda: tk.messagebox.showinfo("メッセージ", "ラベル文字: " + self.label01_2['text']))
        # # 部品配置
        self.label01_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label01_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button01_labelChange.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button01_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_01_1_labelChange(self):
        self.g_count_labelChange += 1
        self.label01_2['text'] = str(self.g_count_labelChange)

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()