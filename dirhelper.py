from pathlib import WindowsPath

def get_files(directoryName,filter="*.*",recu=True):
    wp=WindowsPath(directoryName)
    func=wp.rglob if recu else wp.glob
<<<<<<< HEAD:dirhelper.py
    return [str(file) for file in func(filter)]  
=======
    return [str(file) for file in func(filter)]
    
>>>>>>> ac2bb3dbf733700ea3c9baf73940e1d43940056a:filehelper.py

