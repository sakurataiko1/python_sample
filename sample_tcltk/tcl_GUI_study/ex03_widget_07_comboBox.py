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
        # Combobox
        # 部品定義
        self.label7_1 = ttk.Label(self.frame00, text='■ ComboBox')
        self.GUIvalue_combobox7_1 = tk.StringVar()
        self.GUIlist_combobox7_1 = ["アイテム0", "アイテム1", "アイテム2"]
        self.combobox7_1 = ttk.Combobox(self.frame00, textvariable=self.GUIvalue_combobox7_1, values=self.GUIlist_combobox7_1, state="readonly")  # style="office.TCombobox")
        self.combobox7_1.bind('<<ComboboxSelected>>', self.func_on_combobox7_1_changed)
        self.button7_1 = ttk.Button(self.frame00, text="アイテム1にセットします", command=lambda: self.GUIvalue_combobox7_1.set("アイテム1") )
        # 部品配置
        self.label7_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.combobox7_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button7_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        #
        self.GUIvalue_combobox7_1.set("アイテム0")  # 初期値設定

    def func_on_combobox7_1_changed(self, e):
        msg = "コンボボックス " + str(self.combobox7_1.current()) + "番目\n"
        msg += self.GUIvalue_combobox7_1.get() + "\nが選択されました"
        tk.messagebox.showinfo("info", msg)


if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()