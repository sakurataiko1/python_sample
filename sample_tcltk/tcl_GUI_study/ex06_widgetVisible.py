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
        self.master.columnconfigure(0, weight=1)
        #self.master.rowconfigure(2, weight=1)  # 縦方向の伸縮は不要なのでコメントアウト

        # -------------------------
        # Labelframe and Label 1, 2
        # 0行目
        # 部品定義
        msg = "ウィジェットの表示・非表示を切り替える"
        self.label1 = ttk.Label(self.frame00, text=msg, justify='left')  # justifyで複数行メッセージを左寄せ
        # 部品配置
        self.label1.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # 1行目　
        # 部品定義
        self.label1_1 = ttk.Label(self.frame01, text="例1 正常動作")
        self.buttonOn1 = ttk.Button(self.frame01, text="表示", command=self.func_buttonOn1_clicked)
        self.buttonOff1 = ttk.Button(self.frame01, text="非表示", command=self.func_buttonOff1_clicked)
        self.frame_visible1a = ttk.Frame(self.frame01)  # 位置を覚えておくためのフレームA
        self.frame_visible1b = ttk.Frame(self.frame_visible1a) # 複数ウィジェットをまとめるためのフレームB
        self.entry1_1 = ttk.Entry(self.frame_visible1b, width=20)
        self.checkbutton1_1 = ttk.Checkbutton(self.frame_visible1b, text="A")
        self.checkbutton1_2 = ttk.Checkbutton(self.frame_visible1b, text="B")
        self.label1_2 = ttk.Label(self.frame01, text="非表示状態ですきま無し")
        # 部品配置
        self.label1_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.buttonOn1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.buttonOff1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_visible1a.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_visible1b.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry1_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkbutton1_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkbutton1_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label1_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # 2行目
        # 部品定義
        self.label2_1 = ttk.Label(self.frame02, text="例2 動作NG")
        self.buttonOn2 = ttk.Button(self.frame02, text="表示", command=self.func_buttonOn2_clicked)
        self.buttonOff2 = ttk.Button(self.frame02, text="非表示", command=self.func_buttonOff2_clicked)
        self.frame_visible2a = ttk.Frame(self.frame02)  # 位置を覚えておくためのフレームA
        self.frame_visible2b = ttk.Frame(self.frame_visible2a) # 複数ウィジェットをまとめるためのフレームB
        self.entry2_1 = ttk.Entry(self.frame_visible2b, width=20)
        self.checkbutton2_1 = ttk.Checkbutton(self.frame_visible2b, text="A")
        self.checkbutton2_2 = ttk.Checkbutton(self.frame_visible2b, text="B")
        self.label2_2 = ttk.Label(self.frame02, text="非表示状態ですきまが空いてしまう")
        # 部品配置
        self.label2_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.buttonOn2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.buttonOff2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_visible2a.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_visible2b.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry2_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkbutton2_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkbutton2_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label2_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # 3行目
        # 部品定義
        self.label3_1 = ttk.Label(self.frame03, text="例3 動作NG")
        self.buttonOn3 = ttk.Button(self.frame03, text="表示", command=self.func_buttonOn3_clicked)
        self.buttonOff3 = ttk.Button(self.frame03, text="非表示", command=self.func_buttonOff3_clicked)
        self.frame_visible3a = ttk.Frame(self.frame03)  # 位置を覚えておくためのフレームA
        #self.frame_visible2b = ttk.Frame(self.frame_visible2a) # 複数ウィジェットをまとめるためのフレームB
        self.entry3_1 = ttk.Entry(self.frame_visible3a, width=20)
        self.checkbutton3_1 = ttk.Checkbutton(self.frame_visible3a, text="A")
        self.checkbutton3_2 = ttk.Checkbutton(self.frame_visible3a, text="B")
        self.label3_2 = ttk.Label(self.frame03, text="再表示後に位置が変わってしまう")
        # 部品配置
        self.label3_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.buttonOn3.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.buttonOff3.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_visible3a.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        #self.frame_visible2b.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry3_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkbutton3_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkbutton3_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label3_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_buttonOn1_clicked(self):
        self.func_visible(1)

    def func_buttonOff1_clicked(self):
        self.func_visible(0)

    def func_buttonOn2_clicked(self):
        self.func_visible_NG2(1)

    def func_buttonOff2_clicked(self):
        self.func_visible_NG2(0)

    def func_buttonOn3_clicked(self):
        self.func_visible_NG3(1)

    def func_buttonOff3_clicked(self):
        self.func_visible_NG3(0)

    def func_visible(self, in_flag):
        # 非表示について、propageteなどの前設定により、隙間があかないように表示される
        # 再表示について、位置を覚えておくためのフレームA, # 複数ウィジェットをまとめるためのフレームB　の2つを使うことで再表示後ももとの位置に表示される
        #
        if (in_flag == 0):
            # 非表示のための設定
            self.frame_visible1a.propagate(False) #　無効にする：サイズを中に配置されたウィジェットサイズに合わせる設定
            self.frame_visible1a['width'] = 2     # 非表示の時に隙間が空かないようにする
            # 非表示にする
            self.frame_visible1b.pack_forget()
        else:
            # 表示のための設定
            self.frame_visible1a.propagate(True) # 有効にする：frameサイズを中に配置されたウィジェットサイズに合わせる
            # 非表示にする
            self.frame_visible1b.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_visible_NG2(self, in_flag):
        # NG例　propageteなどの記述がない場合、非表示にした時に隙間が空く
        if (in_flag == 0):
            # 非表示のための設定
            #self.frame_visible2a.propagate(False) #　無効にする：サイズを中に配置されたウィジェットサイズに合わせる設定
            #self.frame_visible2a['width'] = 2     # 非表示の時に隙間が空かないようにする
            # 非表示にする
            self.frame_visible2b.pack_forget()
        else:
            # 表示のための設定
            #self.frame_visible2a.propagate(True) # 有効にする：frameサイズを中に配置されたウィジェットサイズに合わせる
            # 非表示にする
            self.frame_visible2b.pack(side='left', padx=self.g_padx, pady=self.g_pady)

    def func_visible_NG3(self, in_flag):
        # NG例　frama_visible　を2つ使わずに、1つだけでは　再表示後に位置が変わってしまう
        if (in_flag == 0):
            # 非表示のための設定
            self.frame_visible3a.propagate(False) #　無効にする：サイズを中に配置されたウィジェットサイズに合わせる設定
            self.frame_visible3a['width'] = 2     # 非表示の時に隙間が空かないようにする
            # 非表示にする
            self.frame_visible3a.pack_forget()
        else:
            # 表示のための設定
            self.frame_visible3a.propagate(True) # 有効にする：frameサイズを中に配置されたウィジェットサイズに合わせる
            # 非表示にする
            self.frame_visible3a.pack(side='left', padx=self.g_padx, pady=self.g_pady)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()


