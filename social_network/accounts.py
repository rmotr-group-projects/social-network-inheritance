
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)

    def get_timeline(self):
        tl = []
        for u in self.following:
            for post in u.posts:
                tl.append(post)
        return sorted(tl, key=lambda p:p.timestamp, reverse=False)

    def follow(self, other):
        return self.following.append(other)
