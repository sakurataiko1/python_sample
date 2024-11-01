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
        # radioButton 6
        # 部品定義
        self.label6 = ttk.Label(self.frame00, text="■ RadioButton")
        self.frame_for_radio = ttk.Frame(self.frame00)
        self.GUIvalue_radioButton6 = tk.IntVar()
        self.GUIvalue_radioButton6.set(1)
        self.radioButton6_1 = ttk.Radiobutton(self.frame_for_radio, text="a", value=1, variable=self.GUIvalue_radioButton6)
        self.radioButton6_2 = ttk.Radiobutton(self.frame_for_radio, text="b", value=2, variable=self.GUIvalue_radioButton6)
        self.radioButton6_3 = ttk.Radiobutton(self.frame_for_radio, text="c", value=3, variable=self.GUIvalue_radioButton6)
        self.button6_1 = ttk.Button(self.frame_for_radio, text="ラジオボタンB 選択", command=lambda: self.GUIvalue_radioButton6.set(2))
        self.button6_2 = ttk.Button(self.frame_for_radio, text="表示 選択されたラジオボタン", command=lambda: tk.messagebox.showinfo("info", "選択されているラジオボタンは\n" + str(self.GUIvalue_radioButton6.get()) + "番目です"))
        # 部品配置
        self.label6.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_for_radio.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.radioButton6_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.radioButton6_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.radioButton6_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button6_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button6_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)


if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()