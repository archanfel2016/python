from pathlib import WindowsPath

class FileInfo():
    def __init__(self,filePathStr) -> None:
        self.filePath=filePathStr
        self.fileObj=WindowsPath(filePathStr)

    def read_all_text(self,encoding="gbk"):
        return self.fileObj.read_text(encoding,errors=None)
