注意！此工具现在被废弃，我使用 C++ 重写了此工具以移除对运行时的要求，而且还修复了壁纸重启后失效的 Bug

# 自动设置必应壁纸

依赖： 

- python3
- pip install requests pypiwin32

# 说明：

- .py 文件是用来设置壁纸的，但是重启后系统会恢复以前的壁纸，所以每次开机都要运行一遍。而且这个脚本如果检测到今天已经下载过壁纸的话，会直接用下载好的壁纸
- .vbs 里的路径要设置为 .py 文件的路径，然后复制到“C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp”目录下
