
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
        return self.posts 

    def get_timeline(self):
        timeline = []
        for person in self.following:
            timeline += person.posts
        return timeline

    def follow(self, other):
        self.following.append(other)
        return self.following
