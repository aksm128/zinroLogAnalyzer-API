import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class DriveFileStream:
    def __init__(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)
        self.rootPath = "1UYFcpHPmQCjYGCaPeCYtRaUHR05hvV-h"
        self.rawPath = "1fBnc2kKf0msus4N7-TYZEUha503pgtly"
        self.minifyPath = "1wMQQIUNx5qKkkZth-cjfypWqtAj-Ys6J"
        self.errorLogPath = "1aRaYF9-erEV-Vnya36eRzLl43MVpgZw9"

    def get_id(self, path):
        dirid = ""
        folder, title = path.split("/")
        if folder == "raw":
            dirid = self.rawPath
        elif folder == "minify":
            dirid = self.minifyPath
        elif folder == "root":
            dirid = self.rootPath
        elif folder == "errorLog":
            dirid = self.errorLogPath
        return dirid, title

    def search_cloud_file(self, path):
        dirid, title = self.get_id(path)
        file_list = self.drive.ListFile({"q": "'%s' in parents and title = '%s'" % (dirid, title)}).GetList()
        return file_list

    def get_file(self, path):
        file_list = self.search_cloud_file(path)
        if len(file_list) != 0:
            file = self.drive.CreateFile({"id": file_list[0]["id"]})
            return file
        else:
            dirid, title = self.get_id(path)
            file = self.drive.CreateFile({"parents": [{"id": dirid}], "title": title})
            return file

    def load_file(self, path):
        file = self.get_file(path)
        return file.GetContentString()

    def save_file(self, path, content):
        file = self.get_file(path)
        file.SetContentString(content)
        file.Upload()


drive = DriveFileStream()
drive.save_file("errorLog/hoge.txt", "hogehoge")
