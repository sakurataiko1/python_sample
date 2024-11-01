@echo off

rem コマンドプロンプトを最小化して実行する
rem @if not "%~0"=="%~dp0.\%~nx0" start /min cmd /c,"%~dp0.\%~nx0" %* & goto :eof

rem 実行ディレクトリを取得
set current_dir=%~dp0
cd %current_dir%

echo ""
echo "ツール実行中はこの画面は閉じないで下さい"

rem @echo on
c:\PythonEmbed395\python.exe 02_MainWindow_WinScroll.py

