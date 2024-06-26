import time

import package as pac


class Thread(pac.Shell):
    def __init__(self, title, username, date_in="", id_='', list_id_posts=''):
        self.title = title
        self.list_id_posts = list_id_posts
        self.obj_posts = []
        self.username = username
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
        pac.Shell.list_obj_thread.append(self)

    def display(self):
        print("------------------------------------------------------------------")
        print(f"{self.date} par {self.username}\nTitle: {self.title}")
        print("------------------------------------------------------------------")
        for post in self.obj_posts:
            print(post.__str__())
            print("..................................................................")

    def __str__(self):
        return f"{self.date} par {self.username}\nTitle: {self.title}"
    
    def __repr__(self):
        return {"title_thread": self.title, "username_thread": self.username, "date_trhead": self.date, "id": self.id, "liste_id_post": self.list_id_posts}

    