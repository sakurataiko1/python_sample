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
        # Spinbox 9
        # 部品定義
        self.label_exSpin1 = ttk.Label(self.frame00, text="■ spinbox")
        #self.GUIvalue_spinbox_exSpin1 = tk.IntVar()
        self.spinbox_exSpin1 = ttk.Spinbox(self.frame00, from_=0, to=100,  width=5) #　textvariable=self.GUIvalue_spinbox_exSpin1　を設定することもできる
        self.label_exSpinMin = ttk.Label(self.frame00, text="Min")
        self.entry_exSpinMin = ttk.Entry(self.frame00, width=5)
        self.label_exSpinMax = ttk.Label(self.frame00, text="Max")
        self.entry_exSpinMax = ttk.Entry(self.frame00, width=5)
        self.label_exSpinStep = ttk.Label(self.frame00, text="Step")
        self.entry_exSpinStep = ttk.Entry(self.frame00, width=5)
        self.label_exSpinValue = ttk.Label(self.frame00, text="Value")
        self.entry_exSpinValue = ttk.Entry(self.frame00, width=5)
        self.button_exSpin1 = ttk.Button(self.frame00, text="入力欄の値をスピンボックスにセット", command=self.func_on_button_exSpin1_clicked)
        self.button_exSpin2 = ttk.Button(self.frame00, text="スピンボックス値を表示", command=self.func_on_button_exSpin2_clicked)
        #button_exSpin2 = ttk.Button(self.frame00, text="Add Spinboxes", command=self.func_on_button_exSpin2_clicked)
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

    # ------------------------
    def func_on_button_exSpin1_clicked(self):
        try:
            self.spinbox_exSpin1['to'] = int(self.entry_exSpinMax.get())  # 以前に入っている値のため　min>max　とならないように先に to から設定する
            self.spinbox_exSpin1['from'] = int(self.entry_exSpinMin.get())
            self.spinbox_exSpin1['increment'] = int(self.entry_exSpinStep.get())
            value = int(self.entry_exSpinValue.get())
            self.spinbox_exSpin1.delete(0, tk.END)
            self.spinbox_exSpin1.insert(0, value)
            #self.GUIvalue_spinbox_exSpin1.set(value)   # 例：オプションで textvariable 記述した場合の書式
        except ValueError:
            print("正しい整数値を入力してください")
            
    def func_on_button_exSpin2_clicked(self):
        msg = "spinbox value\n"
        msg += "min: " + str(self.spinbox_exSpin1['from']) + "\n"   # 設定は from, from_どちらでも良いが、取得は from（アンダーバーなし）のみ使える
        msg += "max: " + str(self.spinbox_exSpin1['to']) + "\n"
        msg += "step: " + str(self.spinbox_exSpin1['increment']) + "\n"
        msg += "value:" + str(self.spinbox_exSpin1.get()) + "\n"
        tk.messagebox.showinfo("info", msg)

if __name__ == "__main__":
    root = tk.Tk()
    #app = Application(master=root)
    app = MainWindow(master=root)
    app.mainloop()