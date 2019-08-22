
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
        feed=[]
        for user in self.following:
            feed+=user.posts
        
        return sorted(feed, key=lambda user: user.timestamp, reverse=False)

    def follow(self, other):
        return self.following.append(other)
        
