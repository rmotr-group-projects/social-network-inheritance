class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for _ in self.following:
            timeline += _.posts
        return sorted(timeline, key=lambda p: p.timestamp, reverse=False)

    def follow(self, other):
        self.following.append(other)



