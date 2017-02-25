
class User(object):
    
    def __init__(self, first_name, last_name, email, posts = None, following = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for other in self.following:
            timeline += other.posts
        timeline.sort(key = lambda x: x.timestamp)
        return timeline

    def follow(self, other):
        self.following.append(other)