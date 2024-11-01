#  全体ウィンドウにスクロールバーを付ける例
# 　LensTool で使用している例　の抜粋
# 　LensToolは横幅、縦幅とも画面いっぱい使用するようなGUIなので適用できるが
#   一般的なウィンドウに収まるサイズのウィンドウでは適当ではない

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

        # GUIレイアウト
        self.func_defaulCreate_GUIlayout()

    def func_on_scrollbarV_scrolled(self, *args):
        # スクロールバーが動いた時の処理
        self.scrollbarV.set(*args)  # スクロールバーがユーザー操作した位置にセットされるようにする　（これがないと動かしたのに元の位置に戻ってしまう）
        #
        # MainWindow の全体スクロールバーが動作することでシグナルスロットが発生し　GUIフォーム値が変わっていないのに動作してしまうことの防止
        self.flag_wintop_scroll = 1
        #print(DEBUGstr, self.scrollbarV.get()[1]) # スクロールの現在位置
        #print(DEBUGstr, " flag_wintop_scroll=", self.flag_wintop_scroll)
        self.after(5000, self.func_flagset_scrollbarStop)  # 5000ミリ秒(=5秒)待ってから、関数実行

    def func_flagset_scrollbarStop(self):
        self.flag_wintop_scroll = 0

    def func_on_mouse_wheel(self, event):
        self.canvas_wintop.yview_scroll(-1 * int((event.delta / 120)), "units")

    def func_defaulCreate_GUIlayout(self):
        self.master.title("sample_TopWindow_ScrollBar")

        # グローバルフォント設定 フォントサイズ button,labelには適用されるが、entry, comboBoxに適用されない
        #default_font = font.nametofont("TkDefaultFont")
        #default_font.configure(size=10)
        # フォントサイズ指定する場合は g_font を各ウィジェット生成時:entry,comboBox に font=self.g_font として指定する
        # self.g_font = tk.font.Font(size=10)

        self.g_padx_def = 2  # デフォルトの部品間余白サイズ　横
        self.g_pady_def = 5  # デフォルトの部品間余白サイズ 縦
        #self.root.option_add("*Font*", "areal 11") # ウィンドウ全てのフォント設定　フォント種類とサイズ

        self.g_pady_frame_STEMload = 1  #frame_STEM_load1, frame_STEM_load1 は余白=5 では広すぎるので数値を小さくする


        self.g_size_plotframe_default = 500  # frame_widget_plot1の縦サイズ=500前提
        self.g_winsizeW = 1550  # 全体部品が入るサイズ
        self.g_winsizeH = 1000 + self.g_size_plotframe_default # 1960  # 全体部品が入るサイズ  # プロット画面サイズ=500前提
        #str_sizeWH = str(self.g_winsizeW) + "x" + str(self.g_winsizeH)
        # ↓全体部品が入るサイズは　1760 だが、スクロールバーがあるためウィンドウ起動はそれより小さくする。スクロールバー範囲は全体部品がはいるようにpackする
        #str_sizeWH = "600x400"
        str_sizeWH = str(self.g_winsizeW) + "x" + str(self.g_winsizeH)
        self.master.geometry(str_sizeWH)

        # self.master.resizable(False, True)  # 縦方向には伸縮可能、横方向には伸縮不可にする
        self.master.wm_maxsize(width=self.g_winsizeW, height=self.g_winsizeH)

        # -start- 全体スクロールバー設定
        self.canvas_wintop = tk.Canvas(self.master)
        self.frame_wintop = tk.Frame(self.canvas_wintop)
        self.scrollbarV = tk.Scrollbar(
            self.canvas_wintop, orient=tk.VERTICAL, command=self.canvas_wintop.yview
        )
        # スクロールの設定
        self.flag_wintop_scroll = 0
        self.canvas_wintop.configure(scrollregion=(0, 0, self.g_winsizeW, self.g_winsizeH)) # スクロールできる範囲を設定　#サイズ決め打ち #部品が入りきらないサイズにならないようにするため、プロット画面サイズがユーザー入力で変更された場合にも処理を入れることが必要

        self.canvas_wintop.configure(yscrollcommand=self.func_on_scrollbarV_scrolled)

        # 水平方向スクロールバー
        self.scrollbarH = tk.Scrollbar(
            self.canvas_wintop, orient=tk.HORIZONTAL, command=self.canvas_wintop.xview
        )
        self.canvas_wintop.configure(xscrollcommand=self.scrollbarH.set)

        # 諸々を配置
        self.scrollbarV.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbarH.pack(side=tk.BOTTOM, fill=tk.X)  # 水平方向スクロールバー
        self.canvas_wintop.pack(expand=True, fill=tk.BOTH)

        # Canvas上の座標(0, 0)に対してFrameの左上（nw=north-west）をあてがうように、Frameを埋め込む
        #self.canvas_wintop.create_window((0, 0), window=self.frame_wintop, anchor="nw", width=self.g_winsizeW, height=self.g_winsizeH)
        self.canvas_wintop.create_window((0, 0), window=self.frame_wintop, anchor="nw")  # GUI部品が全部入るサイズを確保するため、width,heightでの決め打ちしない　　後述する→self.canvas_wintop.config(scrollregion=self.canvas_wintop.bbox("all"))
        # -end- 全体スクロールバー設定

        # マウスホイールイベントをバインド
        self.canvas_wintop.bind_all("<MouseWheel>", self.func_on_mouse_wheel)

        # マウススクロールするための全体フレーム
        #　部品定義　と　部品配置
        self.frame_wintop2 = tk.Frame(self.frame_wintop, relief='groove', bd=2)  # relief=枠線スタイル bd=枠線太さ
        self.frame_wintop2.grid(row=0, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")

        # GUI部品配置
        self.func_defaulCreate_GUIlayout_sub1()


    def func_winsize_update(self):
        # ウィンドウ全体のスクロール範囲を更新　
        #    GUI部品の表示・非表示切り替えで、ウィンドウ全体幅が足りなくなって表示が切れたり、余白ができたりすることを防ぐ　　
        self.frame_wintop2.update_idletasks()  # 全部品おいている内部フレームのサイズを更新する。　配置した部品が全て表示できるサイズになる。
        self.canvas_wintop.config(scrollregion=self.canvas_wintop.bbox("all"))  # スクロール範囲を更新する

    def func_defaulCreate_GUIlayout_sub1(self):
        # 全体レイアウトのためのフレーム　縦にならべる(row)
        # 部品定義
        self.frame00 = tk.Frame(self.frame_wintop2, relief='groove', bd=2)  # relief=枠線スタイル bd=枠線太さ
        self.frame01 = tk.Frame(self.frame_wintop2, relief='groove', bd=2)
        # 部品配置
        self.frame00.grid(row=0, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame01.grid(row=1, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        root.columnconfigure(0, weight=1)  # 列数＝1なので使ってないので 1つだけ設定
        root.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # ウィンドウ全体がリサイズされた時に、内部部品も追従するようにする
        # 効かないので一旦コメントアウト # self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        #==========================
        # 全体画面 0行目
        # 部品定義
        self.label_msgDEBUG1 = tk.Label(self.frame00, text="msgDEBUG1")
        self.lineEdit_DEBUG1 = ttk.Entry(self.frame00, width=60)
        # 部品配置
        self.label_msgDEBUG1.pack(side='left', padx=2, pady=2)
        self.lineEdit_DEBUG1.pack(side='left', padx=2, pady=2)

        #==========================
        # 全体画面 1行目 全体幅調整用
        # 部品定義
        self.frame_brank_forWinAllSize = ttk.Frame(self.frame01, width=self.g_winsizeW - 50, height=self.g_winsizeH -20, relief='groove', borderwidth=2)
        # 部品配置
        self.frame_brank_forWinAllSize.pack(side='left', padx=2, pady=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()