import time

import package as pac


class Thread(pac.Shell):
    def __init__(self, title, shell_list_username, date_in="", id_=''):
        self.title = title
        self.list_id_posts = []
        self.obj_posts = []
        self.shell_list_username = shell_list_username
        self.date = time.asctime(time.localtime())
        if date_in != "":
            self.date = date_in
        self.id = id_
        if id_ == '':
            self.id = 't' + pac.add_id(pac.Shell.list_threads)
        pac.maj_data(self.__repr__(), pac.Shell.list_threads, 'data_threads.csv', pac.Shell.head_thread)
        for obj in pac.Shell.list_obj_post:
            if obj.id in self.list_id_posts:
                self.obj_posts.append(obj)

    def display(self):
        print("------------------------------------------------------------------")
        print(f"{self.date} par {self.shell_list_username}\nTitle: {self.title}")
        print("------------------------------------------------------------------")
        for post in self.obj_posts:
            print(post.__str__())
            print("..................................................................")

    def __str__(self):
        return f"{self.date} par {self.shell_list_username}\nTitle: {self.title}"
    
    def __repr__(self):
        return [self.title, self.shell_list_username, self.date, self.id, self.list_id_posts]

    