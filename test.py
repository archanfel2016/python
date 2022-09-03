import dirhelper
p=r"C:\Users\Administrator\Desktop\Github\python"
res=dirhelper.get_files(p,recu=False)
for i in res:
    print(i)

