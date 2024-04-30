import time

import package as pac


class Thread(pac.Shell):
    def __init__(self, title, name_user):
        self.title = title
        self.posts = []
        self.name_user = name_user
        post = pac.Post(input("Veuillez saisir un texte: "), name_user)
        self.posts.append(post)

    def display(self):
        print("------------------------------------------------------------------")
        print(f"{time.asctime(time.localtime())} par {self.name_user}\nTitle: {self.title}")
        print("------------------------------------------------------------------")
        for post in self.posts:
            print(post.__str__())
            print("..................................................................")

    def __str__(self):
        return f"{time.asctime(time.localtime())} par {self.name_user}\nTitle: {self.title}"

    