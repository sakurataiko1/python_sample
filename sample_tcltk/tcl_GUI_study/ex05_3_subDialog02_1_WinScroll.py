#
# 全体ウィンドウにスクロールバーを設定する　（子ダイアログ）
#

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

class subDialog02_1_WinScroll:
    #　 プログラム内容
    #      子ダイアログ Window全体にスクロールバーを設定する
    #
    def __init__(self, master, parent):
        #super().__init__(master)
        self.master = master
        self.parent = parent
        #self.mode = mode

        self.window = None

        #self.init_ui_dialog2()

    def func_this_window_close(self):
        self.window.withdraw()
        # ↓これをしないと、子ウィンドウを閉じた後に、再度開くことが出来なくなる。
        #self.window = None
        #self.parent.obj_dialog_AFMsd1 = None# 親Windowで持っているChildWindow情報のリセット
        self.window.quit()  # エラーメッセージが出るがこれを入れないと、親ウィンドウで次の処理がされない self.window.mainloop()の終了
        self.window.destroy()
        return "break"

    def func01_init_ui_dialog2(self):
        if not self.window:
            self.window = tk.Toplevel(self.master)

        # ×ボタンの処理をカスタマイズする
        self.window.protocol('WM_DELETE_WINDOW', self.func_this_window_close)

        # GUIレイアウト
        self.func_defaulCreate_GUIlayout()

        # GUI画面を起動したままにする
        self.window.mainloop()

    def func_defaulCreate_GUIlayout(self):
        # メインウィンドウの作成
        self.window.title("Resizable TextBox with self.scrollbar")
        self.window.geometry("400x300")  # 初期ウィンドウサイズ

        # Canvasを作成し、スクロールバーを追加
        self.canvas_wintop = tk.Canvas(self.window)
        #self.scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.canvas_wintop.yview)
        self.scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.canvas_wintop.yview)
        print("[DEBUG]1928")
        self.canvas_wintop.configure(yscrollcommand=self.scrollbar.set)

        # スクロールバーとキャンバスをグリッドに配置
        self.canvas_wintop.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # フレームの作成とキャンバスに配置
        self.frame_wintop = tk.Frame(self.canvas_wintop)
        self.canvas_wintop.create_window((0, 0), window=self.frame_wintop, anchor="nw")

        # Textボックスをフレーム内に配置
        # text_box = tk.Text(self.frame_wintop, wrap="word", width=200, height=100)
        # text_box.grid(row=0, column=0, sticky="nsew")

        self.frame_wintop2 = tk.Frame(self.frame_wintop)
        self.frame_wintop2.grid(row=0, column=0, sticky="nsew")
        # ウィンドウのリサイズ時にTextボックスが自動でリサイズされるように設定
        self.frame_wintop.grid_rowconfigure(0, weight=1)
        self.frame_wintop.grid_columnconfigure(0, weight=1)

        # self.frame00 ～ xx ウィジェット配置のためのフレーム
        self.frame00 = tk.Frame(self.frame_wintop2)
        self.frame01 = tk.Frame(self.frame_wintop2)
        self.frame00.grid(row=0, column=0, sticky="nsew")
        self.frame01.grid(row=1, column=0, sticky="nsew")
        # ウィンドウのリサイズ時に自動でリサイズされるように設定
        self.frame_wintop2.grid_rowconfigure(0, weight=1)
        self.frame_wintop2.grid_columnconfigure(0, weight=1)

        # self.frame00に配置
        # 部品定義
        self.button2_1 = ttk.Button(self.frame00, text="test1")
        entry2 = ttk.Entry(self.frame00)
        # 部品配置
        self.button2_1.pack(side='left', padx=2, pady=2)
        entry2.pack(side='left', padx=2, pady=2, fill="x", expand=True)

        # self.frame00に配置
        # 部品定義
        self.text_box2 = tk.Text(self.frame01, wrap="word", width=200, height=100)
        # 部品配置
        self.text_box2.pack(side="left")

        # Canvas内のフレームもリサイズ可能に設定
        self.canvas_wintop.bind("<Configure>", lambda e: self.canvas_wintop.configure(scrollregion=self.canvas_wintop.bbox("all")))

        # メインウィンドウのリサイズ設定
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)


# if __name__ == "__main__":
#     root = tk.Tk()
#     #app = Application(master=root)
#     app = MainWindow(master=root)
#     app.mainloop()