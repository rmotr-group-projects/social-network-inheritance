
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        self.following = []
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    def get_timeline(self):
        posts = []
        for user in self.following:
            posts += user.posts
        
        return posts

    def follow(self, other):
        self.following.append(other)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    