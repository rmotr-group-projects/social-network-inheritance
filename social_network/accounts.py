
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        # call post.set_user(self) sometime in this method
        self.posts.append(post)
        post.set_user(self)
    
    def get_timeline(self):
        time_line_posts = []
        for user in self.following:
            for post in user.posts:
                time_line_posts.append(post)
        # how to sort time_line_posts? 
        return time_line_posts
        



    def follow(self, other):
        self.following.append(other)
    
