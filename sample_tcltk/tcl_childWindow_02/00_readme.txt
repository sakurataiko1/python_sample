
〇 ボタン押下で mode 指定して、子ウィンドウ起動
　 モード指定により、画面GUIが違うものとして表示される

〇 ChildWindowが既に存在する場合はメッセージボックスで通知し、新たに開かないようにする 

〇 childWin.py で mode を引数として受け取る

〇 childWin 起動後、画面が閉じられるまで、次の処理は実行されないようにする

〇 00_main.py と childWin.py で情報受け渡しする

◆ childWin.py func_initを複数用意することで、GUI表示や、渡す引数を自由度高く切り替えできるようにする
　 例）↓これらを 00_mainWin.py から呼び出す
　 func_init_01(), 
　 func_init_02(self, 引数リストなど, 引数, 引数）
