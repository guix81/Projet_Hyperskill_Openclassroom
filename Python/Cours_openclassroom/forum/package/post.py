import time
import package as pac


class Post(pac.Shell):
    def __init__(self, content, name_user, date_in=""):
        self.content = content
        self.name_user = name_user
        self.date = time.asctime(time.localtime())
        if date_in != "":
            self.date = date_in

    def __str__(self):
        return f"   {self.date} par {self.name_user}\n   Content: {self.content}"
    
    def __repr__(self):
        return [self.date, self.name_user, self.content]