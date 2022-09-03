import filehelper
p=r"C:\BaiduNetdiskDownload\PyQt5开发与实战视频教程\PyQt5开发与实战（1）"
res=filehelper.get_files(p,recu=False)
for i in res:
    print(i)

