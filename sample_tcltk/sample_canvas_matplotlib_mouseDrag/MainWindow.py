import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib import pyplot as plt
import cv2
from matplotlib.patches import Rectangle  # 矩形描画

from PlotWidget import PlotWidget

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matplotlib Graph with Rectangle Drawing")

        #　部品定義： GUI全体レイアウトのためのフレーム　縦にならべる(row)
        self.frame00 = tk.Frame(self.root)
        self.frame01 = tk.Frame(self.root)
        # 部品配置
        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.frame01.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        # ユーザーによる画面サイズ変更に追従して、GUI部品も伸縮するようにする
        for i in range(2):
            self.root.columnconfigure(i, weight=1)  # 横方向へのサイズ伸縮
        self.root.rowconfigure(1, weight=1)  # 縦方向へのサイズ伸縮　は canvas=plotwidget配置する段のみ

        # 部品定義　1段目
        self.button_clear = ttk.Button(self.frame00, text="画面クリア", command=self.func_on_button_clear_clicked)
        self.button_plot1 = ttk.Button(self.frame00, text="Plot1", command=self.func_on_button_plot1_clicked)
        self.button_image1 = ttk.Button(self.frame00, text="image1", command=self.func_on_button_image1_clicked)
        self.button_graphAndImage1 = ttk.Button(self.frame00, text="plot and Image", command=self.func_on_button_graphAndImage1_clicked)
        # 部品配置　1段目
        self.button_clear.pack(side='left', padx=2)
        self.button_plot1.pack(side='left', padx=2)
        self.button_image1.pack(side='left', padx=2)
        self.button_graphAndImage1.pack(side='left', padx=2)
 
        # レイアウト2段目：Matplotlibのグラフを表示するCanvas
        # 部品定義　2段目
        self.plot_canvas1 = PlotWidget(self.frame01)
        # 部品配置　2段目
        self.plot_canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def func_on_button_clear_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()

    def func_on_button_plot1_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()
        # 描画
        self.func_plot_graph1()

    def func_on_button_image1_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()
        # 描画
        self.func_draw_image1()

    def func_on_button_graphAndImage1_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()
        # グラフ描画
        self.func_plot_graph1()
        # 画像描画
        self.func_draw_image1()

    def func_plot_graph1(self):
        # グラフを描画するダミーのデータ
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]

        # Canvasのクリア
        #self.plot_canvas1.ax.clear()

        # グラフ描画
        self.plot_canvas1.ax.plot(x, y)

        # Canvasに反映
        self.plot_canvas1.canvas.draw()

    def func_draw_image1(self):
        # Canvasのクリア
        #self.plot_canvas1.ax.clear()

        # 画像を描画する　グラフに重ねる
        workfilepath = "test_image01.png"
        xlim = self.plot_canvas1.ax.get_xlim()
        ylim = self.plot_canvas1.ax.get_ylim()
        self.plot_canvas1.func_addImage_cv2(workfilepath, xlim, ylim)
        self.plot_canvas1.canvas.draw()  #　描画反映



if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
