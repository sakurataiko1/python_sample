#
# ■　python GUI tcl/tk 右寄せ配置
#
import os
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("GUIlayout_expand")
        #self.master.geometry("600x400")

        self.g_padx=2
        self.g_pady=2

        # 全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame01 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame02 = ttk.Frame(self.master, relief='groove', borderwidth=2)
        self.frame03 = ttk.Frame(self.master, relief='groove', borderwidth=2)

        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")  # sticky設定でウィンドウ全体リサイズに追従させる
        self.frame01.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.frame02.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.frame03.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # ユーザーによる画面リサイズ時にウィジェット大きさが追従するように設定
        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 縦のリサイズ追従
        #self.master.rowconfigure(2, weight=1)     # 横のリサイズ追従

        # 補足　↑この例では1列のみなので columnconfigure で 0列目だけ設定しているが、複数行ある場合はその全てに設定する
        # 3列の場合
        # self.master.columnconfigure(0, weight=1)
        # self.master.columnconfigure(1, weight=1)
        # self.master.columnconfigure(2, weight=1)
        # もしくは
        #　for i in range(3):
        #   self.master.columnconfigure(i, weight=1)

        msg = "右寄せ配置したい場合は pack をコードとして書く順番に注意が必要\n"
        msg += "例1: side=rightのNG例  button2, button1 とも side=right とし 1, 2 の順番で書く\n"
        msg += "例2: packする時に  button2, button1 とも side=right とし 2, 1 の順番で書く\n"
        msg += "例3: packする時に配置用frame_layout1 を side_rightで配置。frama_layout1の中にbutton1, button2は　side=left として 1,2 の順番で書く"

        # -------------------------
        # Labelframe and Label 1, 2
        # 0行目
        # 部品定義
        self.label1 = ttk.Label(self.frame00, text=msg, justify='left')  # justifyで複数行メッセージを左寄せ
        # 部品配置
        self.label1.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # 1行目
        # 部品定義
        self.label1_1 = ttk.Label(self.frame01, text="例1")
        self.button1_1 = ttk.Button(self.frame01, text="テスト1")
        self.button1_2 = ttk.Button(self.frame01, text="テスト2")
        # 部品配置
        self.label1_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button1_1.pack(side='right', padx=self.g_padx, pady=self.g_pady)
        self.button1_2.pack(side='right', padx=self.g_padx, pady=self.g_pady)

        # 2行目
        # 部品定義
        self.label2_1 = ttk.Label(self.frame02, text="例2")
        self.button2_1 = ttk.Button(self.frame02, text="テスト1")
        self.button2_2 = ttk.Button(self.frame02, text="テスト2")
        # 部品配置
        self.label2_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button2_2.pack(side='right', padx=self.g_padx, pady=self.g_pady)
        self.button2_1.pack(side='right', padx=self.g_padx, pady=self.g_pady)

        # 3行目
        # 部品定義
        self.label3_1 = ttk.Label(self.frame03, text="例3")
        self.frame_layout3_1 = ttk.Frame(self.frame03)
        self.button3_1 = ttk.Button(self.frame_layout3_1, text="テスト1")
        self.button3_2 = ttk.Button(self.frame_layout3_1, text="テスト2")
        # 部品配置
        self.label3_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_layout3_1.pack(side='right', padx=self.g_padx, pady=self.g_pady)
        self.button3_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button3_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()


