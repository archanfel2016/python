from pathlib import WindowsPath

def get_files(directoryName,filter="*.*",recu=True):
    wp=WindowsPath(directoryName)
    func=wp.rglob if recu else wp.glob
    return [str(file) for file in func(filter)]
    

