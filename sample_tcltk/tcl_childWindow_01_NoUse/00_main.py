import tkinter as tk
from tkinter import messagebox
import childWin

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.geometry(str(320) + "x" + str(200) + "+" + str(200) + "+" + str(200))
        self.master.geometry("320x280+200+200")
        self.master.title("parent window")

        self.child_window = None  # ChildWindowのインスタンスを保持するための変数

        self.g_parent_str = ""

        self.create_widgets()

    def create_widgets(self):
        # 部品定義
        self.button1 = tk.Button(self, text="Open Child Window (Mode 1)", command=lambda: self.open_child_window(1))
        self.button2 = tk.Button(self, text="Open Child Window (Mode 2)", command=lambda: self.open_child_window(2))
        # 部品配置
        self.button1.pack(side='top', anchor='w', padx=5, pady=5)
        self.button2.pack(side='top', anchor='w', padx=5, pady=5)

        # 部品定義
        self.label1 = tk.Label(self, text='子ウィンドウへの情報送付欄')
        self.entry_p1 = tk.Entry(self)
        # 部品配置
        self.label1.pack(side='top', anchor='w')  #　左寄せ: anchor='w'
        self.entry_p1.pack(side='top', anchor='w')
        #
        self.entry_p1.insert(0,"from paretn test01")

        # 部品定義
        self.label2 = tk.Label(self, text='子ウィンドウから情報受け取り 01')
        self.entry_p2 = tk.Entry(self)
        # 部品配置
        self.label2.pack(side='top', anchor='w')
        self.entry_p2.pack(side='top', anchor='w')

        # 部品定義
        self.label3 = tk.Label(self, text='子ウィンドウから情報受け取り 02')
        self.entry_p3 = tk.Entry(self)
        # 部品配置
        self.label3.pack(side='top', anchor='w')
        self.entry_p3.pack(side='top', anchor='w')

    def open_child_window(self, mode):
        # ChildWindowが既に存在する場合はメッセージボックスで通知し、新たに開かないようにする
        if self.child_window is not None and self.child_window.winfo_exists():
            messagebox.showinfo("Info", "Child Window is already open.")
        else:
            self.child_window = childWin.ChildWindow(self.master, self, mode)
            self.child_window.wait_window()  # ChildWindowが閉じるまで待機
            msg = "from parent\n child window close\n parent g_parent_str=" + self.g_parent_str
            messagebox.showinfo("Info", msg)
            self.entry_p3.delete(0, tk.END)
            self.entry_p3.insert(0, self.g_parent_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.pack()
    app.mainloop()
