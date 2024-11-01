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

        self.g_count_button = 0

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

        # -------------------------
        # Button
        # 部品定義
        self.label03_1 = ttk.Label(self.frame00, text="■ button")
        self.button03_1 = ttk.Button(self.frame00, text=str(self.g_count_button))
        self.button03_2 = ttk.Button(self.frame00, text="[1] ボタン1 テキストを書き換え 関数呼び出し", command=self.func_button03_2_clicked) # 関数に()はつけてはいけない　# lamda付けない場合、引数指定不可
        self.button03_3 = ttk.Button(self.frame00, text="[2] ボタン1 テキストを書き換え 引数あり", command=lambda: self.func_button03_test(2))
        self.button03_4 = ttk.Button(self.frame00, text="[3] ボタン1のテキストを取得", command=lambda: tk.messagebox.showinfo("メッセージ", "button1のテキスト：" + self.button03_1['text']))
        # 部品配置
        self.label03_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_4.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_button03_2_clicked(self):
        self.func_button03_test(1)

    def func_button03_test(self, in_int):
        self.g_count_button += in_int
        self.button03_1['text'] = str(self.g_count_button)


if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()