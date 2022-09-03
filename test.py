import filehelper
p=r"C:\Users\Administrator\Desktop\Github\python"
res=filehelper.get_files(p,recu=False)
for i in res:
    print(i)

