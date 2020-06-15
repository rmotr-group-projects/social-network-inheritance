
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.timeline =[]
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        return self.timeline

    def follow(self, other):
        if other not in self.following:
            self.following.append(other)
        for post in other.posts:
            self.timeline.append(post)
