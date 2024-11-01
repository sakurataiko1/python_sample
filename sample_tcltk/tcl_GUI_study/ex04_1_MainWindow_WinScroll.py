import tkinter as tk
from tkinter import ttk

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
        self.master.title("Resizable TextBox with Scrollbar")
        self.master.geometry("400x300")  # 初期ウィンドウサイズ

        # Canvasを作成し、スクロールバーを追加
        self.canvas_wintop = tk.Canvas(self.master)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas_wintop.yview)
        self.canvas_wintop.configure(yscrollcommand=self.scrollbar.set)

        # スクロールバーとキャンバスをグリッドに配置
        self.canvas_wintop.grid(row=0, column=0, sticky="nsew", padx=self.g_padx, pady=self.g_pady)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # フレームの作成とキャンバスに配置
        self.frame_wintop = tk.Frame(self.canvas_wintop)
        self.canvas_wintop.create_window((0, 0), window=self.frame_wintop, anchor="nw")

        # Textボックスをフレーム内に配置
        # text_box = tk.Text(self.frame_wintop, wrap="word", width=200, height=100)
        # text_box.grid(row=0, column=0, sticky="nsew")

        self.frame_wintop2 = tk.Frame(self.frame_wintop)
        self.frame_wintop2.grid(row=0, column=0, sticky="nsew", padx=self.g_padx, pady=self.g_pady)
        # ウィンドウのリサイズ時にTextボックスが自動でリサイズされるように設定
        self.frame_wintop.grid_rowconfigure(0, weight=1)
        self.frame_wintop.grid_columnconfigure(0, weight=1)

        # self.frame00 ～ xx ウィジェット配置のためのフレーム
        self.frame00 = tk.Frame(self.frame_wintop2)
        self.frame01 = tk.Frame(self.frame_wintop2)
        self.frame00.grid(row=0, column=0, sticky="nsew", padx=self.g_padx, pady=self.g_pady)
        self.frame01.grid(row=1, column=0, sticky="nsew", padx=self.g_padx, pady=self.g_pady)
        # ウィンドウのリサイズ時に自動でリサイズされるように設定
        self.frame_wintop2.grid_rowconfigure(0, weight=1)
        self.frame_wintop2.grid_columnconfigure(0, weight=1)

        # self.frame00に配置
        # 部品定義
        self.button2_1 = ttk.Button(self.frame00, text="test1")
        self.entry2 = ttk.Entry(self.frame00)
        # 部品配置
        self.button2_1.pack(side='left', padx=self.g_padx, pady=self.g_pady)
        self.entry2.pack(side='left', padx=self.g_padx, pady=self.g_pady, fill="x", expand=True)

        # self.frame00に配置
        # 部品定義
        self.text_box2 = tk.Text(self.frame01, wrap="word", width=200, height=100)
        # 部品配置
        self.text_box2.pack(side="left", padx=self.g_padx, pady=self.g_pady)

        # Canvas内のフレームもリサイズ可能に設定
        self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        # メインウィンドウのリサイズ設定
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()