# coding:utf-8

class BaseParse(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path

    def parse(self, conf):
        return None
