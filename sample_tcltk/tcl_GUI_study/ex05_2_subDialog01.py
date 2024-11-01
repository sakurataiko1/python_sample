import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

class subDialog01:
    #　 プログラム内容
    #       子ウィンドウ起動例、レイアウト配置の基礎
    #
    def __init__(self, master, parent):
        #super().__init__(master)
        self.master = master
        self.parent = parent
        #self.mode = mode

        self.window = None

    def func_this_window_close(self):
        self.window.withdraw()
        # ↓これをしないと、子ウィンドウを閉じた後に、再度開くことが出来なくなる。
        #self.window = None
        #self.parent.obj_dialog_AFMsd1 = None# 親Windowで持っているChildWindow情報のリセット
        self.window.quit()  # エラーメッセージが出るがこれを入れないと、親ウィンドウで次の処理がされない self.window.mainloop()の終了
        self.window.destroy()
        return "break"

    def init_ui_dialog1(self, in_tmpstr):
        if not self.window:
            self.window = tk.Toplevel(self.master)

        # ×ボタンの処理をカスタマイズする
        self.window.protocol('WM_DELETE_WINDOW', self.func_this_window_close)

        #　GUI画面作成
        self.func_create_widget()

        # 初期値設定
        self.label_msg1['text'] = in_tmpstr

        # GUI画面を起動したままにする
        self.window.mainloop()

    def func_create_widget(self):
        # グローバルフォント設定 フォントサイズ button,labelには適用されるが、entry, comboBoxに適用されない
        #default_font = font.nametofont("TkDefaultFont")
        #default_font.configure(size=10)
        # フォントサイズ指定する場合は g_font を各ウィジェット生成時:entry,comboBox に font=self.g_font として指定する
        # self.g_font = tk.font.Font(size=10)
        self.window.title("subDialog1")
        #self.window.resize(800, 420)
        self.window.geometry('400x300')

        # 部品定義　全体レイアウト　フレーム構成
        # 全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = tk.Frame(self.window, bd=2)   # relief='groove' 枠線スタイル bd=枠線太さ
        self.frame01 = tk.Frame(self.window, bd=2)
        self.frame02 = tk.Frame(self.window, bd=2)

        # 部品配置　全体レイアウト　フレーム構成
        # ユーザーによる画面リサイズ時にウィジェット大きさが追従するように設定
        self.frame00.grid(row=0, column=0, padx=5, pady=2, sticky="nsew")
        self.frame01.grid(row=1, column=0, padx=5, pady=2, sticky="nsew")
        self.frame02.grid(row=2, column=0, padx=5, pady=2, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.window.columnconfigure(0, weight=1) #　列ブロック配置 0列だけ使う
        self.window.rowconfigure(2, weight=1)  # 行ブロック配置　画面リサイズ時の、部品リサイズ追従は 2=canvasのみ

        # 部品定義 0行目
        self.label01 = ttk.Label(self.frame00, text="入力")
        self.lineEdit01 = ttk.Entry(self.frame00)
        self.lineEdit01.bind('<Return>', self.func_on_lineEdit01_editingFinished)
        self.button01 = ttk.Button(self.frame00, text='OK', command=self.func_on_button01_clicked)
        # 部品配置 0行目
        self.label01.pack(side='left', padx=2, pady=5)
        self.lineEdit01.pack(side='left', padx=2, pady=5)
        self.button01.pack(side='left', padx=2, pady=5)

        # 部品定義 1行目
        self.label_msg1 = ttk.Label(self.frame01, text="msg")
        # 部品配置 1行目
        self.label_msg1.pack(side="top", fill="both", expand=True)

        # 部品定義 2行目
        #self.label_msg2 = ttk.Label(self.frame02, text="msg2")
        #self.canvas1 = tk.Canvas(self.frame02, width=200, height=200, relief='groove')
        self.textbox01 = tk.Text(self.frame02) #, width=20, height=6)
        #部品配置 2行目
        #self.canvas1.pack(side="top", fill="both", expand=True)
        self.textbox01.pack(side="top", fill="both", expand=True)

    def func_on_button01_clicked(self):
        self.func_sendStrToParent()

    def func_on_lineEdit01_editingFinished(self):
        self.func_sendStrToParent()

    def func_sendStrToParent(self):
        self.parent.entry1.delete(0, tk.END)
        self.parent.entry1.insert(0, self.lineEdit01.get())