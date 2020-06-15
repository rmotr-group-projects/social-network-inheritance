

class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        time = []
        for i in self.following:
            for j in i.posts:
                time.append(j)
        return time

    def follow(self, other):
        self.following.append(other)
