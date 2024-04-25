from abc import ABC

class Shell(ABC):
    pass
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
    pass
#------------------------
class User(Shell):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        pass

    def post(self, thread, content, file=None):
        if file:
            post = FilePost(self, "now", content, file)
        else:
            post = Post(self, "now", content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        post = Post(self, "now", content)
        return Thread(title, "now", post)
    
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
    def __init__(self, user, time_posted, content, file=None):
        self.file = file
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        print(f"Message de {self.user} posté le {self.time_posted}")
        print(self.content + '\n')

class FilePost(Post):
    def init(self, user, time_posted, content, file):
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        super().display()
        self.file.display()
#------------------------
class Thread(Shell):
    def __init__(self, title, time_posted, posts):
        self.title = title
        self.time_posted = time_posted
        self.posts = [posts]

    def display(self):
        print(f"Thread: {self.title}, posté le {self.time_posted}")
        print()
        for post in self.posts:
            post.display()

    def add_post(self, post):
        self.posts.append(post)



