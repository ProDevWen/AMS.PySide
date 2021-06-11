rem 调用pyinstaller生成可执行程序的脚本
rem 执行pip install pyinstaller安装需求库
@echo off
pyinstaller --clean
pyinstaller -wF AMS.py --specpath output
pyinstaller -wD AMS.py --specpath output
pyinstaller -F AMS.py --specpath output -n AMS.debug
pyinstaller -D AMS.py --specpath output -n AMS.debug
@echo on