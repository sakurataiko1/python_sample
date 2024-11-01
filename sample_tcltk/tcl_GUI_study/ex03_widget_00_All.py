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
        #print("[DEBUG]func_flagset_scrollbarStop")

    def func_on_mouse_wheel(self, event):
        self.canvas_wintop.yview_scroll(-1 * int((event.delta / 120)), "units")

    def func_defaulCreate_GUIlayout(self):
        self.master.title("sample all tk-widget")

        # グローバルフォント設定 フォントサイズ button,labelには適用されるが、entry, comboBoxに適用されない
        #default_font = font.nametofont("TkDefaultFont")
        #default_font.configure(size=10)
        # フォントサイズ指定する場合は g_font を各ウィジェット生成時:entry,comboBox に font=self.g_font として指定する
        # self.g_font = tk.font.Font(size=10)

        self.g_padx_def = 2  # デフォルトの部品間余白サイズ　横
        self.g_pady_def = 5  # デフォルトの部品間余白サイズ 縦
        #self.root.option_add("*Font*", "areal 11") # ウィンドウ全てのフォント設定　フォント種類とサイズ

        self.g_pady_frame_STEMload = 1  #frame_STEM_load1, frame_STEM_load1 は余白=5 では広すぎるので数値を小さくする

        #self.master.geometry("1910x1700")  #   必ず、全部の部品が見えるサイズ以上にする

        self.g_winsizeW = 1800  # 全体部品が入るサイズ
        self.g_winsizeH = 2000
        #str_sizeWH = str(self.g_winsizeW) + "x" + str(self.g_winsizeH)
        # ↓全体部品が入るサイズは　1760 だが、スクロールバーがあるためウィンドウ起動はそれより小さくする。スクロールバー範囲は全体部品がはいるようにpackする
        str_sizeWH = "800x800"
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
        self.frame_wintop2 = tk.Frame(self.frame_wintop)  
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
        self.frame00 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)  # relief=枠線スタイル bd=枠線太さ
        self.frame01 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame02 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame03 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame04 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame05 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame06 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame07 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame08 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame09 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame10 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame11 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame12 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame13 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame14 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        self.frame15 = tk.Frame(self.frame_wintop2, relief='groove', borderwidth=1)
        # 部品配置
        self.frame00.grid(row=0, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame01.grid(row=1, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame02.grid(row=2, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame03.grid(row=3, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame04.grid(row=4, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame05.grid(row=5, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame06.grid(row=6, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame07.grid(row=7, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame08.grid(row=8, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame09.grid(row=9, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame10.grid(row=10, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame11.grid(row=11, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame12.grid(row=12, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame13.grid(row=13, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame14.grid(row=14, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")
        self.frame15.grid(row=15, column=0, padx=5, pady=self.g_pady_def, sticky="nsew")

        # グリッドの設定  全体ウィンドウの伸縮に、各部品が追従するにはこれが必須
        self.master.columnconfigure(0, weight=1)  # 列数＝1なので使ってないので 1つだけ設定
        self.master.rowconfigure(1, weight=1) # 画面リサイズ時の、縦方向の部品リサイズ追従は 1のみ(canvasを含むもの)

        # ウィンドウ全体がリサイズされた時に、内部部品も追従するようにする
        # 効かないので一旦コメントアウト # self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        #==========================
        # Frmame and LabelFrame
        # 部品定義
        self.label00_1 = ttk.Label(self.frame00, text="■ Frame and LabelFrame")
        self.frame00_1 = ttk.Frame(self.frame00, width=200, relief='groove', borderwidth=1)
        self.button00_1 = ttk.Button(self.frame00_1, text="button1")
        self.frame00_2 = ttk.Frame(self.frame00, width=200, height="50", relief='groove', borderwidth=1)
        self.frame00_2.propagate(False) # frameサイズを、中に配置された部品のサイズに自動設定する設定をOFFする。デフォルトではONで、width設定しても無効になる。
        self.button00_2 = ttk.Button(self.frame00_2, text="button2")
        self.labelframe00_1 = ttk.LabelFrame(self.frame00, text="LabelFrame") # relief='groove', borderwidth=1)
        self.button00_3 = ttk.Button(self.labelframe00_1, text="button1")
        # 部品配置
        self.label00_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')  # anchorで左寄せ
        self.frame00_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button00_1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor="w")
        self.frame00_2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button00_2.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='nw') # anchorで左・上寄せ
        self.labelframe00_1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor='w')
        self.button00_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        #==========================
        # Label
        # 部品定義
        # -------------------------
        self.label01_1 = ttk.Label(self.frame01, text="■ Label")
        self.g_count_labelChange = 0
        self.label01_2 = ttk.Label(self.frame01, text="0")
        self.button01_labelChange = ttk.Button(self.frame01, text="ラベル書き換え", command=self.func_01_1_labelChange) # 関数に()はつけてはいけない
        self.button01_2 = ttk.Button(self.frame01, text="ラベルテキスト表示", command=lambda: tk.messagebox.showinfo("メッセージ", "ラベル文字: " + self.label01_2['text']))
        # # 部品配置
        self.label01_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label01_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button01_labelChange.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button01_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # -------------------------
        # Button
        # 部品定義
        self.label03_1 = ttk.Label(self.frame03, text="■ Button")
        self.g_count_button = 0
        self.button03_1 = ttk.Button(self.frame03, text="[1] ボタン1 テキストを書き換え 引数なし", command=self.func_button03_1_clicked) # 関数に()はつけてはいけない　# lamda付けない場合、引数指定不可
        self.button03_2 = ttk.Button(self.frame03, text="[2] ボタン1 テキストを書き換え 引数あり", command=lambda: self.func_button03_test(2))
        self.button03_3 = ttk.Button(self.frame03, text="[3] ボタン1のテキストを取得", command=lambda: tk.messagebox.showinfo("メッセージ", "button1のテキスト：" + self.button03_1['text']))
        # 部品配置
        self.label03_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button03_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # -------------------------
        # Entry 4
        # 部品定義
        self.label4 = ttk.Label(self.frame04, text="■ Entry")
        self.frame4 = ttk.Frame(self.frame04)
        self.entry4 = ttk.Entry(self.frame04)
        self.entry4.bind('<Return>', self.func_on_entry4_editingFinished)
        self.button4_1 = ttk.Button(self.frame04, text="Input1", command=self.func_on_button4_1_clicked)
        self.button4_2 = ttk.Button(self.frame04, text="output", command=lambda: tk.messagebox.showinfo("title_dialog", self.entry4.get()))
        # 部品配置
        self.label4.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame4.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry4.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button4_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button4_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # -----------------------------------------------------
        # Checkbutton 5
        # 部品定義
        self.label5 = ttk.Label(self.frame05, text="■ CheckButton")
        self.GUIvalue_check5 = tk.BooleanVar(value=False)
        self.checkButton5 = ttk.Checkbutton(self.frame05, text="A", command=self.func_on_checkButton5_clicked, variable=self.GUIvalue_check5)
        self.entry5 = ttk.Entry(self.frame05, width=50)
        self.button_check5_1 = tk.Button(self.frame05, text="チェックボックスON", command=lambda: self.GUIvalue_check5.set(True))
        self.button_check5_2 = tk.Button(self.frame05, text="チェックボックスOFF", command=lambda: self.GUIvalue_check5.set(False))
        # 部品配置
        self.label5.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.checkButton5.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry5.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_check5_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_check5_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        #
        self.GUIvalue_check5.set(True) # デフォルト状態　チェックONにする

        # -----------------------------------------------------
        # radioButton 6
        # 部品定義
        self.label6 = ttk.Label(self.frame06, text="■ RadioButton")
        self.frame_for_radio = ttk.Frame(self.frame06)
        self.radioButton6_value = tk.IntVar()
        self.radioButton6_value.set(1)
        self.radioButton6_1 = ttk.Radiobutton(self.frame_for_radio, text="a", value=1, variable=self.radioButton6_value)
        self.radioButton6_2 = ttk.Radiobutton(self.frame_for_radio, text="b", value=2, variable=self.radioButton6_value)
        self.radioButton6_3 = ttk.Radiobutton(self.frame_for_radio, text="c", value=3, variable=self.radioButton6_value)
        self.button6_1 = ttk.Button(self.frame_for_radio, text="ラジオボタンB 選択", command=lambda: self.radioButton6_value.set(2))
        self.button6_2 = ttk.Button(self.frame_for_radio, text="表示 選択されたラジオボタン", command=lambda: tk.messagebox.showinfo("info", "選択されているラジオボタンは\n" + str(self.radioButton6_value.get()) + "番目です"))
        # 部品配置
        self.label6.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.frame_for_radio.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.radioButton6_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.radioButton6_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.radioButton6_3.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button6_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button6_2.pack(side='left', padx=self.g_padx, pady=self.g_pady)


        # -----------------------------------------------------
        # Combobox
        # 部品定義
        self.label7_1 = ttk.Label(self.frame07, text='■ ComboBox')
        self.GUIvalue_combobox7_1 = tk.StringVar()
        self.GUIlist_combobox7_1 = ["アイテム0", "アイテム1", "アイテム2"]
        self.combobox7_1 = ttk.Combobox(self.frame07, textvariable=self.GUIvalue_combobox7_1, values=self.GUIlist_combobox7_1, state="readonly")  # style="office.TCombobox")
        self.combobox7_1.bind('<<ComboboxSelected>>', self.func_on_combobox7_1_changed)
        self.button7_1 = ttk.Button(self.frame07, text="アイテム1にセットします", command=lambda: self.GUIvalue_combobox7_1.set("アイテム1") )
        # 部品配置
        self.label7_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.combobox7_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button7_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        #
        self.GUIvalue_combobox7_1.set("アイテム0")  # 初期値設定




        # -----------------------------------------------------
        # Spinbox 9
        # 部品定義
        self.label_exSpin1 = ttk.Label(self.frame09, text="■ spinbox")
        #self.GUIvalue_spinbox_exSpin1 = tk.IntVar()
        self.spinbox_exSpin1 = ttk.Spinbox(self.frame09, from_=0, to=100,  width=5) #　textvariable=self.GUIvalue_spinbox_exSpin1　を設定することもできる
        self.label_exSpinMin = ttk.Label(self.frame09, text="Min")
        self.entry_exSpinMin = ttk.Entry(self.frame09, width=5)
        self.label_exSpinMax = ttk.Label(self.frame09, text="Max")
        self.entry_exSpinMax = ttk.Entry(self.frame09, width=5)
        self.label_exSpinStep = ttk.Label(self.frame09, text="Step")
        self.entry_exSpinStep = ttk.Entry(self.frame09, width=5)
        self.label_exSpinValue = ttk.Label(self.frame09, text="Value")
        self.entry_exSpinValue = ttk.Entry(self.frame09, width=5)
        self.button_exSpin1 = ttk.Button(self.frame09, text="入力欄の値をスピンボックスにセット", command=self.func_on_button_exSpin1_clicked)
        self.button_exSpin2 = ttk.Button(self.frame09, text="スピンボックス値を表示", command=lambda: tk.messagebox.showinfo("info", str(self.spinbox_exSpin1.get())))
        #button_exSpin2 = ttk.Button(self.frame09, text="Add Spinboxes", command=self.func_on_button_exSpin2_clicked)
        #　部品配置
        self.label_exSpin1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.spinbox_exSpin1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exSpinMin.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exSpinMin.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exSpinMax.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exSpinMax.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exSpinStep.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exSpinStep.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exSpinValue.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exSpinValue.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_exSpin1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_exSpin2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        # 初期値　設定
        self.spinbox_exSpin1.delete(0, tk.END)
        self.spinbox_exSpin1.insert(0, 0)
        self.entry_exSpinMin.delete(0, tk.END)
        self.entry_exSpinMin.insert(0, "0")
        self.entry_exSpinMax.delete(0, tk.END)
        self.entry_exSpinMax.insert(0, "10")
        self.entry_exSpinStep.delete(0, tk.END)
        self.entry_exSpinStep.insert(0, "1")
        self.entry_exSpinValue.delete(0, tk.END)
        self.entry_exSpinValue.insert(0, "5")

        # -----------------------------------------------------
        # Scale 10
        # 部品定義
        self.label_exScale1 = ttk.Label(self.frame10, text="■ slider (tk.Scale)")
        self.frame_exScale1 = ttk.Frame(self.frame10)
        self.frame_exScale2 = ttk.Frame(self.frame10)
        self.spinbox_exScale1 = ttk.Spinbox(self.frame_exScale1, from_=0, to=100, width=5, command=self.func_on_spinbox_exScale1_valueChanged)
        self.GUIvalue_exScale1 = tk.DoubleVar()
        self.scale_exScale1 = tk.Scale(self.frame_exScale1, from_=-100, to=100, orient=tk.HORIZONTAL, resolution=0.1, length=300, showvalue=True, variable=self.GUIvalue_exScale1, command=self.func_on_scale_exScale1_valueChanged)  # length=GUIサイズ※widthではない label=記述なしでラベル表示しない、通常はshowvalue=Falseで値表示させない
        self.label_exScaleMin = ttk.Label(self.frame_exScale2, text="Min")
        self.entry_exScaleMin = ttk.Entry(self.frame_exScale2, width=5)
        self.label_exScaleMax = ttk.Label(self.frame_exScale2, text="Max")
        self.entry_exScaleMax = ttk.Entry(self.frame_exScale2, width=5)
        self.label_exScaleStep = ttk.Label(self.frame_exScale2, text="Max")
        self.entry_exScaleStep = ttk.Entry(self.frame_exScale2, width=5)
        self.label_exScaleValue = ttk.Label(self.frame_exScale2, text="Value")
        self.entry_exScaleValue = ttk.Entry(self.frame_exScale2, width=5)
        self.button_exScale1 = ttk.Button(self.frame_exScale2, text="入力欄の値をセット", command=self.func_on_button_exScale1_clicked)
        self.button_exScale2 = ttk.Button(self.frame_exScale2, text="スライダー値を表示", command=lambda: tk.messagebox.showinfo("info", str(self.scale_exScale1.get())))
        #　部品配置
        self.label_exScale1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor="nw")
        self.frame_exScale1.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor="nw")
        self.frame_exScale2.pack(side='top', padx=self.g_padx, pady=self.g_pady, anchor="nw")
        self.spinbox_exScale1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.scale_exScale1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exScaleMin.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exScaleMin.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exScaleMax.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exScaleMax.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exScaleStep.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exScaleStep.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.label_exScaleValue.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry_exScaleValue.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_exScale1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.button_exScale2.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        # 初期値　設定
        self.spinbox_exScale1['from_'] = 0
        self.spinbox_exScale1['to'] = 100
        self.spinbox_exScale1['increment'] = 1
        self.scale_exScale1['from_'] = 0
        self.scale_exScale1['to'] = 100
        self.scale_exScale1['resolution'] = 1
        self.spinbox_exScale1.delete(0, tk.END)
        self.spinbox_exScale1.insert(0, 0)
        self.entry_exScaleMin.delete(0, tk.END)
        self.entry_exScaleMin.insert(0, "0")
        self.entry_exScaleMax.delete(0, tk.END)
        self.entry_exScaleMax.insert(0, "10")
        self.entry_exScaleStep.delete(0, tk.END)
        self.entry_exScaleStep.insert(0, "1")
        self.entry_exScaleValue.delete(0, tk.END)
        self.entry_exScaleValue.insert(0, "5")

        # -----------------------------------------------------
        # Message 11
        # 部品定義
        # label11 = ttk.Label(self.frame11, text="11: Message")
        # message11 = tk.Message(self.frame11, text="私の名前は中村です")
        # # 部品配置
        # label11.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        # message11.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # -----------------------------------------------------
        # Text 12
        # 部品定義
        label12 = tk.Label(self.frame12, text="■ Text")
        text12 = tk.Text(self.frame12, width=20, height=6)
        text12.insert(tk.END, "sample text\n1\n2\n3")
        # 部品配置
        label12.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        text12.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        #-----------------------
        # ■　Listbox & ScrollBar"
        # 部品定義
        self.label_exListBox_1 = ttk.Label(self.frame13, text="■ Listbox & ScrollBar")
        self.scrollbar_frame = ttk.Frame(self.frame13)

        list_value = tk.StringVar()
        list_value.set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
        # selectmodeの種類(single:1つだけ選択できる、multiple:複数選択できる、extended：複数選択可能＋ドラッグでも選択可能)
        self.listbox_ex1 = tk.Listbox(self.scrollbar_frame, height=5, listvariable=list_value, selectmode="multiple")
        # 例まで、Listboxの内容設定は以下のようにもできる
        # for i in range(1000):
        #     self.listbox_ex1.insert(tk.END, i)
        self.scroll_bar = tk.Scrollbar(self.scrollbar_frame, command=self.listbox_ex1.yview)
        self.listbox_ex1.config(yscrollcommand=self.scroll_bar.set)
        self.button_exlb_result = ttk.Button(self.frame13, text="選択されたものを表示", command=self.func_on_button_exlb_result_clicked)
        self.button_exlb_allselect = ttk.Button(self.frame13, text="全選択", command=self.func_on_button_exlb_allselect_clicked)
        self.button_exlb_allclear = ttk.Button(self.frame13, text="全クリア", command=self.func_on_button_exlb_allclear_clicked)
        # 部品配置
        self.label_exListBox_1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.scrollbar_frame.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.listbox_ex1.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.button_exlb_result.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.button_exlb_allselect.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        self.button_exlb_allclear.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')

        # -----------------------------------------------------
        # Canvas 14
        # 部品定義
        label14 = ttk.Label(self.frame14, text="■ Canvas")
        canvas = tk.Canvas(self.frame14, bg='white', width=200, height=100)
        canvas.create_oval(25, 15, 180, 60, fill='red')
        canvas.create_oval(25, 45, 180, 85, fill='blue')
        canvas.create_text(100, 90, text='Canvasウィジェット', fill="green")
        # 部品配置
        label14.pack(side='left', padx=self.g_padx, pady=self.g_pady, anchor='n')
        canvas.pack(side='left', padx=self.g_padx, pady=self.g_pady)

        # PanedWindow 15
        #label15 = ttk.Label(self.frame15, text="15: PanedFrame")
        # panedwindow_frame = ttk.Frame(self.frame15)
        # #panedwindow_frame.grid(row=6, column=3, padx=10, pady=10)
        # panedwindow1 = ttk.PanedWindow(panedwindow_frame)
        # text1 = ttk.Text(panedwindow1, height=6, width=15)
        # text1.insert(tk.END, "中村拓男")
        # panedwindow1.add(text1)
        # panedwindow2 = tk.PanedWindow(panedwindow1)
        # text2 = ttk.Text(panedwindow1, height=6, width=15)
        # text2.insert(tk.END, "中村香織")
        # panedwindow2.add(text2)
        # panedwindow1.add(panedwindow2)
        #　部品配置
        #label15.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        # panedwindow_frame.pack(self.frame15)
        # panedwindow1.pack(fill=tk.BOTH, expand=2)

    # ------------------------
    # 関数
    def func_01_1_labelChange(self):
        self.g_count_labelChange += 1
        self.label01_2['text'] = str(self.g_count_labelChange)

    def func_button03_1_clicked(self):
        self.func_button03_test(1)

    def func_button03_test(self, in_int):
        self.g_count_button += in_int
        self.button03_1['text'] = "button1 " + str(self.g_count_button)

    def func_on_button4_1_clicked(self):
        self.entry4.delete(0, tk.END)  # テキストボックスクリア
        self.entry4.insert(tk.END, 'test input1')

    def func_on_entry4_editingFinished(self, e):
        # bindで呼び出される関数は 引数に e （Event引数）が必要
        tk.messagebox.showinfo("info", self.entry4.get() + "が入力されました")

    def func_4_3(self):
        tk.messagebox.showinfo("info", self.entry4.get())

    # ------------------------
    def func_on_checkButton5_clicked(self):
        tmp_value = self.GUIvalue_check5.get()
        # print(f"チェックの状態は {self.value_check5} です")
        self.entry5.delete(0, tk.END)
        self.entry5.insert(tk.END, f"チェックの状態は {tmp_value} です")

    def func_on_combobox7_1_changed(self, e):
        msg = "コンボボックス " + str(self.combobox7_1.current()) + "番目\n"
        msg += self.GUIvalue_combobox7_1.get() +  "\nが選択されました"
        tk.messagebox.showinfo("info", msg)

    # ------------------------
    def func_on_button_exlb_result_clicked(self):
        # ボタンを押したら選択しているアイテムを表示する
        text_check = self.listbox_ex1.curselection()
        if(len(text_check) < 1):
            return
        tmpstr = ""
        for i in text_check:
            tmpstr += self.listbox_ex1.get(i) + " "
        tk.messagebox.showinfo("info", tmpstr + "\nが選択されました")

    def func_on_button_exlb_allselect_clicked(self):
        # 全選択する
        self.listbox_ex1.select_set(0, tk.END)

    def func_on_button_exlb_allclear_clicked(self):
        # 全クリアする
        self.listbox_ex1.select_clear(0, tk.END)

    # ------------------------
    # spinbox
    def func_on_button_exSpin1_clicked(self):
        try:
            self.spinbox_exSpin1['from_'] = int(self.entry_exSpinMin.get())
            self.spinbox_exSpin1['to'] = int(self.entry_exSpinMax.get())
            self.spinbox_exSpin1['increment'] = int(self.entry_exSpinStep.get())
            value = int(self.entry_exSpinValue.get())
            self.spinbox_exSpin1.delete(0, tk.END)
            self.spinbox_exSpin1.insert(0, value)
            #self.GUIvalue_spinbox_exSpin1.set(value)   # 例：オプションで textvariable 記述した場合の書式
        except ValueError:
            print("正しい整数値を入力してください")

    # ------------------------
    # tk.Scale = slider
    def func_on_scale_exScale1_valueChanged(self, in_value):
        self.spinbox_exScale1.delete(0, tk.END)
        self.spinbox_exScale1.insert(0, self.scale_exScale1.get())

    def func_on_spinbox_exScale1_valueChanged(self):
        self.flag_NoSignalSlot_slider = 1  # シグナルスロット動作, 一時無効にする
        self.GUIvalue_exScale1.set(self.spinbox_exScale1.get())

    def func_on_button_exScale1_clicked(self):
        try:
            self.spinbox_exScale1['from_'] = float(self.entry_exScaleMin.get())
            self.spinbox_exScale1['to'] = float(self.entry_exScaleMax.get())
            self.spinbox_exScale1['increment'] = float(self.entry_exScaleStep.get()) # spinboxのステップは 'increment'
            #self.GUIvalue_exScale1.set(self.spinbox_exScale1.get())
            self.spinbox_exScale1.delete(0, tk.END)
            self.spinbox_exScale1.insert(0, self.entry_exScaleValue.get())
            #
            self.scale_exScale1['from_'] = float(self.entry_exScaleMin.get())
            self.scale_exScale1['to'] = float(self.entry_exScaleMax.get())
            self.scale_exScale1['resolution'] = float(self.entry_exScaleStep.get())  # スライダーのステップは 'resolution'
            self.scale_exScale1.set(float(self.entry_exScaleValue.get()))

        except ValueError:
            print("正しい整数値を入力してください")



if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()