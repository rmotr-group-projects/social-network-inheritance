from datetime import datetime

class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        
    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
    
    def get_timeline(self):
        timeline = []
        for user in self.following:
            for p in user.posts:
                timeline.append(p)
        
        return sorted(timeline, key = lambda p: p.timestamp, reverse=False)
        

    def follow(self, other):
        self.following.append(other)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)