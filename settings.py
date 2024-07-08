"""
这个python文件的目的是通过Settings类进行配置，
编写一个class
"""


class Settings:
    def __init__(self, **kwargs):
        self.url = 'http://localhost:11434'
        self.encoding = "utf-8"
        self.model = None
        self.__dict__.update(kwargs)
