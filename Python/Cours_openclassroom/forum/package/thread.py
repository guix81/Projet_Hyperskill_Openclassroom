import time

import package as pac


class Thread(pac.Shell):
    def __init__(self, title, post, obj_user):
        self.title = title
        self.post = post
        self.obj_user = obj_user

    def __str__(self):
        return f"{time.asctime(time.localtime())} par {self.obj_user.name}\nTitle: {self.title}\n\n{self.post}"

    