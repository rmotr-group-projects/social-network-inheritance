class User(object):
    def __init__(self, first_name, last_name, email, following=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = following
        self.posts = []
    
    def __repr__(self):
        return '@{} {}'.format(self.first_name, self.last_name)
        
    def __str__(self):
        return '@{} {}'.format(self.first_name, self.last_name)

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    def get_timeline(self):
        results = []
        results += self.posts
        for user in self.following:
            results += user.posts
        return results

    def follow(self, other):
        self.following.append(other)
        
