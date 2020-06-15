
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
        temp_posts = []
        for user in self.following:
            temp_posts += user.posts
        
        return temp_posts
        ### another option - need to understand lambda better
        # return sorted(temp_posts, key=lambda p: p.timestamp, reverse=False)

    def follow(self, other):
        self.following.append(other)

