
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    def get_timeline(self):
        list_of_posts = []
        for u in self.following:
            list_of_posts += u.posts
            
        return list_of_posts

    def follow(self, other):
        self.following.append(other)
    
    def __repl__(self):
        return 'User: "{} {}"'.format(self.first_name,self.last_name)
