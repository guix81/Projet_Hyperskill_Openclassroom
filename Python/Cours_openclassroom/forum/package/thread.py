import time

import package as pac


class Thread(pac.Shell):
    def __init__(self, title, name_user, date_in=""):
        self.title = title
        self.posts = []
        self.name_user = name_user
        post = pac.Post(input("Veuillez saisir un texte: "), name_user)
        self.posts.append(post)
        self.date = time.asctime(time.localtime())
        if date_in != "":
            self.date = date_in

    def display(self):
        print("------------------------------------------------------------------")
        print(f"{self.date} par {self.name_user}\nTitle: {self.title}")
        print("------------------------------------------------------------------")
        for post in self.posts:
            print(post.__str__())
            print("..................................................................")

    def __str__(self):
        return f"{self.date} par {self.name_user}\nTitle: {self.title}"
    
    def __repr__(self):
        return self.date, self.name_user, self.title, self.posts

    