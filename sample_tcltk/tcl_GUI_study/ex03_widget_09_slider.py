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
        # Scale 
        # 部品定義
        self.label_exScale1 = ttk.Label(self.frame00, text="■ slider (tk.Scale)")
        self.frame_exScale1 = ttk.Frame(self.frame00)
        self.frame_exScale2 = ttk.Frame(self.frame00)
        self.spinbox_exScale1 = ttk.Spinbox(self.frame_exScale1, from_=0, to=100, width=5, command=self.func_on_spinbox_exScale1_valueChanged)
        self.GUIvalue_exScale1 = tk.DoubleVar()
        self.scale_exScale1 = tk.Scale(self.frame_exScale1, from_=-100, to=100, orient=tk.HORIZONTAL, resolution=0.1, length=300, showvalue=True, variable=self.GUIvalue_exScale1, command=self.func_on_scale_exScale1_valueChanged)  # length=GUIサイズ※widthではない label=記述なしでラベル表示しない、通常はshowvalue=Falseで値表示させない
        self.label_exScaleMin = ttk.Label(self.frame_exScale2, text="Min")
        self.entry_exScaleMin = ttk.Entry(self.frame_exScale2, width=5)
        self.label_exScaleMax = ttk.Label(self.frame_exScale2, text="Max")
        self.entry_exScaleMax = ttk.Entry(self.frame_exScale2, width=5)
        self.label_exScaleStep = ttk.Label(self.frame_exScale2, text="Step")
        self.entry_exScaleStep = ttk.Entry(self.frame_exScale2, width=5)
        self.label_exScaleValue = ttk.Label(self.frame_exScale2, text="Value")
        self.entry_exScaleValue = ttk.Entry(self.frame_exScale2, width=5)
        self.button_exScale1 = ttk.Button(self.frame_exScale2, text="入力欄の値をセット", command=self.func_on_button_exScale1_clicked)
        self.button_exScale2 = ttk.Button(self.frame_exScale2, text="スライダー値を表示", command=self.func_on_button_exScale2_clicked)
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

    # ------------------------
    # tk.Scale = slider
    def func_on_scale_exScale1_valueChanged(self, in_value):
        self.spinbox_exScale1.delete(0, tk.END)
        self.spinbox_exScale1.insert(0, self.scale_exScale1.get())

    def func_on_spinbox_exScale1_valueChanged(self):
        self.GUIvalue_exScale1.set(self.spinbox_exScale1.get())

    def func_on_button_exScale1_clicked(self):
        try:
            self.spinbox_exScale1['increment'] = float(self.entry_exScaleStep.get())  # spinboxのステップは 'increment'
            self.spinbox_exScale1['from'] = float(self.entry_exScaleMin.get())
            self.spinbox_exScale1['to'] = float(self.entry_exScaleMax.get())
            self.spinbox_exScale1.set(float(self.entry_exScaleValue.get()))
            #
            self.scale_exScale1['resolution'] = float(self.entry_exScaleStep.get())  # scaleのステップは 'resolution'
            self.scale_exScale1['from'] = float(self.entry_exScaleMin.get())
            self.scale_exScale1['to'] = float(self.entry_exScaleMax.get())
            self.scale_exScale1.set(float(self.entry_exScaleValue.get()))

        except ValueError:
            print("正しい整数値を入力してください")

    def func_on_button_exScale2_clicked(self):
        msg = "spinbox value\n"
        msg += "min: " + str(self.spinbox_exScale1['from']) + "\n"   # 設定は from, from_どちらでも良いが、取得は from（アンダーバーなし）のみ使える
        msg += "max: " + str(self.spinbox_exScale1['to']) + "\n"
        msg += "step: " + str(self.spinbox_exScale1['increment']) + "\n"
        msg += "value:" + str(self.spinbox_exScale1.get()) + "\n"
        #
        msg += "\n"
        msg += "scale value\n"
        msg += "min: " + str(self.scale_exScale1['from']) + "\n"   # 設定は from, from_どちらでも良いが、取得は from（アンダーバーなし）のみ使える
        msg += "max: " + str(self.scale_exScale1['to']) + "\n"
        msg += "step: " + str(self.scale_exScale1['resolution']) + "\n"
        msg += "value:" + str(self.scale_exScale1.get()) + "\n"
        #
        tk.messagebox.showinfo("info", msg)

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()