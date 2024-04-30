import time
import package as pac


class Post(pac.Shell):
    def __init__(self, content, name_user):
        self.content = content
        self.name_user = name_user

    def __str__(self):
        return f"   {time.asctime(time.localtime())} par {self.name_user}\n   Content: {self.content}"