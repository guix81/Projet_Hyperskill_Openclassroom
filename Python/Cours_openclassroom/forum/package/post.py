import time
import package as pac


class Post(pac.Shell):
    def __init__(self, content, shell_list_username, date_in="", id_=''):
        self.content = content
        self.shell_list_username = shell_list_username
        self.date = time.asctime(time.localtime())
        if date_in != "":
            self.date = date_in
        self.id = id_
        if id_ == '':
            self.id = 'p' + pac.add_id(pac.Shell.list_posts)
        pac.maj_data(self.__repr__(), pac.Shell.list_posts, 'data_posts.csv')

    def __str__(self):
        return f"   {self.date} par {self.shell_list_username}\n   Content: {self.content}"
    
    def __repr__(self):
        return [self.content, self.shell_list_username, self.date, self.id]