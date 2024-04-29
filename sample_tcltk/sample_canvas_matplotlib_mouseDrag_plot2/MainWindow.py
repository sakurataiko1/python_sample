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
        self.frame02 = tk.Frame(self.root)
        # 部品配置
        self.frame00.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.frame01.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.frame02.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        # ユーザーによる画面サイズ変更に追従して、GUI部品も伸縮するようにする
        for i in range(3):
            self.root.columnconfigure(i, weight=1)  # 横方向へのサイズ伸縮
        self.root.rowconfigure(2, weight=1)  # 縦方向へのサイズ伸縮　は canvas=plotwidget配置する段のみ

        # 部品定義　0段目
        self.label_msg1 = ttk.Label(self.frame00, text="左画面 プロット1")
        self.button_clear1 = ttk.Button(self.frame00, text="画面クリア", command=lambda: self.func_on_button_clearN_clicked(1))
        self.button_plot1 = ttk.Button(self.frame00, text="Plot1", command=self.func_on_button_plot1_clicked)
        self.button_image1 = ttk.Button(self.frame00, text="image1", command=self.func_on_button_image1_clicked)
        self.button_graphAndImage1 = ttk.Button(self.frame00, text="plot and Image", command=self.func_on_button_graphAndImage1_clicked)
        self.label_msg1_2 = ttk.Label(self.frame00, text="マウスドラッグすると緑色の枠が表示されます")
        # 部品配置　0段目
        self.label_msg1.pack(side='left', padx=2)
        self.button_clear1.pack(side='left', padx=2)
        self.button_plot1.pack(side='left', padx=2)
        self.button_image1.pack(side='left', padx=2)
        self.button_graphAndImage1.pack(side='left', padx=2)
        self.label_msg1_2.pack(side='left', padx=2)

        # 部品定義　1段目
        self.label_msg2 = ttk.Label(self.frame01, text="右画面 プロット2")
        self.button_clear2 = ttk.Button(self.frame01, text="画面クリア", command=lambda: self.func_on_button_clearN_clicked(2))
        self.button_plot2 = ttk.Button(self.frame01, text="Plot2", command=self.func_on_button_plot2_clicked)
        self.button_image2 = ttk.Button(self.frame01, text="image2", command=self.func_on_button_image2_clicked)
        self.button_graphAndImage2 = ttk.Button(self.frame01, text="plot and Image", command=self.func_on_button_graphAndImage2_clicked)
        self.label_msg2_2 = ttk.Label(self.frame01, text="マウスドラッグすると緑色の枠が表示されます")
        # 部品配置　1段目
        self.label_msg2.pack(side='left', padx=2)
        self.button_clear2.pack(side='left', padx=2)
        self.button_plot2.pack(side='left', padx=2)
        self.button_image2.pack(side='left', padx=2)
        self.button_graphAndImage2.pack(side='left', padx=2)
        self.label_msg2_2.pack(side='left', padx=2)

        # レイアウト2段目：Matplotlibのグラフを表示するCanvas
        # 部品定義　2段目
        self.plot_canvas1 = PlotWidget(self.frame02, relief='groove')
        self.plot_canvas2 = PlotWidget(self.frame02, relief='groove')
        # 部品配置　2段目
        self.plot_canvas1.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=1)
        self.plot_canvas2.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=1)

    # ---------------------------
    def func_on_button_clearN_clicked(self, in_mode):
        # Canvasのクリア
        obj_plot_canvas = self.plot_canvas1
        if(in_mode == 2):
            obj_plot_canvas = self.plot_canvas1
        obj_plot_canvas.ax.clear()

    # ---------------------------
    def func_on_button_plot1_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()
        # 描画
        self.func_plot_graph(1)

    def func_on_button_image1_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()
        # 描画
        self.func_draw_image(1)

    def func_on_button_graphAndImage1_clicked(self):
        # Canvasのクリア
        self.plot_canvas1.ax.clear()
        # グラフ描画
        self.func_plot_graph(1)
        # 画像描画
        self.func_draw_image(1)


    # ---------------------------
    def func_on_button_plot2_clicked(self):
        # Canvasのクリア
        self.plot_canvas2.ax.clear()
        # 描画
        self.func_plot_graph(2)

    def func_on_button_image2_clicked(self):
        # Canvasのクリア
        self.plot_canvas2.ax.clear()
        # 描画
        self.func_draw_image(2)

    def func_on_button_graphAndImage2_clicked(self):
        # Canvasのクリア
        self.plot_canvas2.ax.clear()
        # グラフ描画
        self.func_plot_graph(2)
        # 画像描画
        self.func_draw_image(2)

    # ---------------------------
    def func_plot_graph(self, in_mode):
        obj_plot_canvas = self.plot_canvas1
        y = [2, 3, 5, 7, 11]
        if(in_mode == 2):
            obj_plot_canvas = self.plot_canvas2
            y = [2, 4, 6, 8, 10]

        # グラフを描画するダミーのデータ
        x = [1, 2, 3, 4, 5]
        #y = [2, 3, 5, 7, 11]


        # Canvasのクリア
        #self.plot_canvas1.ax.clear()

        # グラフ描画
        obj_plot_canvas.ax.plot(x, y)

        # Canvasに反映
        obj_plot_canvas.canvas.draw()

    def func_draw_image(self, in_mode):
        # Canvasのクリア
        #self.plot_canvas1.ax.clear()
        obj_plot_canvas = self.plot_canvas1
        workfilepath = "test_image01.png"
        if(in_mode == 2 ):
            obj_plot_canvas = self.plot_canvas2
            workfilepath = "test_image02.png"

        # 画像を描画する　グラフに重ねる
        xlim = self.plot_canvas1.ax.get_xlim()
        ylim = self.plot_canvas1.ax.get_ylim()
        #obj_plot_canvas.func_addImage_cv2(workfilepath, xlim, ylim)
        image_org = cv2.imread(workfilepath)
        image_conv = cv2.cvtColor(image_org, cv2.COLOR_BGR2RGB)  # BGR→RGB変換
        obj_plot_canvas.func_addImage_cv2(image_conv, xlim, ylim)
        obj_plot_canvas.canvas.draw()  #　描画反映



if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
