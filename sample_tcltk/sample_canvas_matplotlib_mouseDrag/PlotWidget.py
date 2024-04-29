import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib import pyplot as plt
import cv2
from matplotlib.patches import Rectangle  # 矩形描画

class PlotWidget(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #org-ok# self.fig = Figure(figsize=(5, 4), dpi=100)
        #org-ok# self.ax = self.fig.add_subplot(111)
        self.fig, self.ax = plt.subplots()
        #self.canvas = FigureCanvas(self.fig)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas_widget.bind("<Button-1>", self.func_on_canvas_click)
        self.canvas_widget.bind("<Button1-Motion>", self.func_mouse_onMotion)  # 画面上でマウスドラッグした場合のイベント
        self.canvas_widget.bind("<ButtonRelease-1>", self.func_mouse_onRelease)  # 画面上でマウスボタンを離した場合のイベント
        self.canvas.draw()

        # 矩形描画のための変数
        self.rect_start = None
        self.rect_end = None
        self.rect_id = None

        # マウスドラッグで矩形描画のための変数
        self.pressed = False # Lock to stop the motion event from behaving badly when the mouse isn't pressed
        self.rect = Rectangle((0, 0), 1, 1, facecolor='None', edgecolor='green')
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.ax.add_patch(self.rect) # matplotlib への紐づけ

    def func_on_canvas_click(self, event):
        # Canvas上でマウスクリック時の処理
        # マウス 2点クリックで矩形描画の場合
        if event.x is not None and event.y is not None:
            # Upon initial press of the mouse record the origin and record the mouse as pressed
            self.pressed = True
            self.rect.set_linestyle('dashed')
            self.x1 = event.x
            self.y1 = event.y
            # 前回描いたものを消す
            if self.rect_id is not None:
                self.canvas_widget.delete(self.rect_id)

    def func_draw_rectangle_Drag(self):
        # 矩形を描画
        x1, y1 = self.rect_start
        x2, y2 = self.rect_end
        self.rect_id = self.canvas_widget.create_rectangle(x1, y1, x2, y2, outline="red", width=2)

    def func_mouse_onMotion(self, event):
        # マウスドラッグ時の処理
        '''Callback to handle the motion event created by the mouse moving over the canvas'''

        # 輪郭取得　通常モード　矩形で範囲選択　mouseMode == RectSelect
        # If the mouse has been pressed draw an updated rectangle when the mouse is moved so
        # the user can see what the current selection is
        if self.pressed:
            # Check the mouse was released on the canvas, and if it wasn't then just leave the width and
            # height as the last values set by the motion event
            if event.x is not None and event.y is not None:
                self.x2 = event.x
                self.y2 = event.y
            # Set the width and height and draw the rectangle
            self.rect.set_width(self.x2 - self.x1)
            self.rect.set_height(self.y2 - self.y1)
            self.rect.set_xy((self.x1, self.y1))
            #　描画反映
            # 前回描いたものを消す
            if self.rect_id is not None:
                self.canvas_widget.delete(self.rect_id)
            # 今回クリックされた座標に描く
            self.rect_id = self.canvas_widget.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="green", width=2)

        # -end- if self.pressed:

    def func_mouse_onRelease(self, event):
        # マウスボタンが離された時の処理

        # 輪郭取得　通常モード　矩形で範囲選択 mouseMode == RectSelect
        '''Callback to handle the mouse being released over the canvas'''
        if self.pressed:
            # Upon release draw the rectangle as a solid rectangle
            #
            # Check that the mouse was actually pressed on the canvas to begin with and this isn't a rouge mouse
            # release event that started somewhere else
            self.pressed = False
            self.rect.set_linestyle('solid')

            # Check the mouse was released on the canvas, and if it wasn't then just leave the width and
            # height as the last values set by the motion event
            if event.x is not None and event.y is not None:
                self.x2 = event.x
                self.y2 = event.y

            # Set the width and height and origin of the bounding rectangle
            self.boundingRectWidth = self.x2 - self.x1
            self.boundingRectHeight = self.y2 - self.y1
            self.bouningRectOrigin = (self.x1, self.y1)

            # Draw the bounding rectangle
            self.rect.set_width(self.boundingRectWidth)
            self.rect.set_height(self.boundingRectHeight)
            self.rect.set_xy((self.x1, self.y1))
            #　描画反映
            #self.canvas_widget.draw()
            # 前回描いたものを消す
            if self.rect_id is not None:
                self.canvas_widget.delete(self.rect_id)
            # 今回クリックされた座標に描く
            self.rect_id = self.canvas_widget.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="green", width=2)

    def func_plot_graph1(self):
        # グラフを描画する
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        #self.ax.clear()  # 画像と重ねるため、グラフクリアはしない
        self.ax.plot(x, y)
        #self.canvas.draw()  # 画像と重ねるため, ここでの反映はしない

    def func_plot_graphOnly(self):
        # グラフを描画する
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()  # 描画反映

    def func_setImage_cv2(self, workfilepath):
        # 画像表示　画像のみ、グラフ重ねて表示の場合は別処理
        # 　　※in_xlim, in_ylim で画像を、グラフ位置に調整して重ねる　この記述がないとずれてしまって重なって見えない場合がある
        image = cv2.imread(workfilepath)
        self.ax.imshow(image, aspect='auto', alpha=0.6)

    def func_addImage_cv2(self, workfilepath, in_xlim, in_ylim):
        # グラフ描画後、画像を重ねて表示する
        # 　　※in_xlim, in_ylim で画像を、グラフ位置に調整して重ねる　この記述がないとずれてしまって重なって見えない場合がある
        image = cv2.imread(workfilepath)
        self.ax.imshow(image, extent=[*in_xlim, *in_ylim], aspect='auto', alpha=0.6)
