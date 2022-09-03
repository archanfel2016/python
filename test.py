# import dirhelper
# p=r"C:\Users\Administrator\Desktop\Github\python"
# res=dirhelper.get_files(p,recu=False)
# for i in res:
#     print(i)
import filehelper
fi=filehelper.FileInfo(r"C:\Users\Administrator\Desktop\Github\python\dirhelper.py")
print(fi.read_all_text())

