
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
    
    def add_post(self, post):
        self.posts.append(post)
    
    def follow(self, other):
        if other not in self.following:
            self.following.append(other)
        
    def get_timeline(self):
        timeline = []
        
        for user in self.following:
            timeline.extend(user.posts)
        return sorted(timeline, key = lambda x: x.timestamp)
