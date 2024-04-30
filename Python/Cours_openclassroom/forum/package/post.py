import time
import package as pac


class Post(pac.Shell):
    def __init__(self, content, obj_user):
        self.content = content
        self.obj_user = obj_user

    def __str__(self):
        return f"   {time.asctime(time.localtime())} par {self.obj_user.name}\n   Content: {self.content}"