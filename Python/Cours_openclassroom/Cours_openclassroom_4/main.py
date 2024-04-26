import time

from abc import ABC

class Shell(ABC):
    def __init__(self, date=time.asctime(time.localtime())):
        self.date = date
#------------------------
class File(Shell):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self):
        print(f"Nom du fichier: {self.name}, size: {self.size}")

    def __str__(self):
        return f"Nom du fichier: {self.name}, size: {self.size}"

class Image(File):

    def display(self):
        print(f"Nom du fichier image: {self.name}, size: {self.size}")

class Jpg(Image):

    def display(self):
        print(f"Nom du fichier image de type JPG: {self.name}, size: {self.size}")

class Gif(Image):

    def display(self):
        print(f"Nom du fichier image de type GIF: {self.name}, size: {self.size}")
#------------------------
class User(Shell):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = time.asctime(time.localtime())

    def login(self):
        pass

    def post(self, thread, content, file=None):
        if file:
            post = FilePost(self, self.date, content, file)
        else:
            post = Post(self, self.date, content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        post = Post(self, self.date, content)
        return Thread(title, self.date, post)
    
    def __str__(self):
        return f"{self.username}"

class Moderator(User):
    def edit(self, post, content):
        post.content = content

    def delete(self, thread, post):
        index = thread.posts.index(post)
        del thread.posts[index]
#------------------------
class Post(Shell):
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.date = time.asctime(time.localtime())

    def display(self):
        print(f"Message de {self.user} posté le {self.date}")
        print(self.content + '\n')

class FilePost(Post):
    def __init__(self, user, content, file=None):
        super().__init__(user, content)
        self.file = file

    def display(self):
        super().display()
        self.file.display()
#------------------------
class Thread(Shell):
    def __init__(self, title, posts):
        self.title = title
        self.posts = [posts]
        self.date = time.asctime(time.localtime())

    def display(self):
        print(f"Thread: {self.title}, posté le {self.date}")
        print()
        for post in self.posts:
            post.display()

    def add_post(self, post):
        self.posts.append(post)


guix = User('guix', 'abab')
modo = Moderator('modo', 'juju')
post1 = Post(guix, "Comment puis je résoudre ce probleme?")
thread = Thread('Comment faire?', post1)
thread.display()
input()
post2 = Post(modo, "Tu te démerde!")
thread.add_post(post2)
thread.display()
input()
post3 = Post(guix, "Vous ête null comme modérateur!")
thread.add_post(post3)
thread.display()
input()
post4 = Post(modo, "C'est hors-sujet!!")
thread.add_post(post4)
modo.delete(thread, post3)
thread.display()
input()
file = Image("WTF", '158 octets')
post5 = FilePost(guix, "c'est n'imp...", file)
thread.add_post(post5)
thread.display()
