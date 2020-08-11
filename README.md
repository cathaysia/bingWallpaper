# 自动设置必应壁纸

依赖： 

- python3
- pip install requests pypiwin32

# 说明：

- .py 文件是用来设置壁纸的，但是重启后系统会恢复以前的壁纸，所以每次开机都要运行一遍。而且这个脚本如果检测到今天已经下载过壁纸的话，会直接用本地的壁纸（如果被删掉的话，没有做检查）
- .vbs 里的路径要设置为 .py 文件的路径，然后复制到“C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp”目录下