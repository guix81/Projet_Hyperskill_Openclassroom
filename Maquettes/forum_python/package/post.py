import time
import package as pac


class Post(pac.Shell):
    def __init__(self, content, username, date_in="", id_=''):
        self.content = content
        self.username = username
        self.date = time.asctime(time.localtime())
        if date_in != "":
            self.date = date_in
        self.id = id_
        if id_ == '':
            self.id = 'p' + pac.add_id(pac.Shell.list_posts)
        pac.maj_data(self.__repr__(), pac.Shell.list_posts, 'data_posts.csv', pac.Shell.head_post)
        pac.Shell.list_obj_post.append(self)

    def __str__(self):
        return f"   {self.date} par {self.username}\n   Content: {self.content}"
    
    def __repr__(self):
        return {"content_post": self.content, "username_post": self.username, "date_post": self.date, 'id': self.id}