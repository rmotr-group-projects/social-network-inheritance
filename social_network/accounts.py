
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.posts=[]
        self.following=[]

    def add_post(self, post):
        user1=User(self.first_name, self.last_name, self.email)
        self.posts.append(post)

    def get_timeline(self):
        userposts=[]
        for users in self.following:
            userposts+=users.posts 
        return userposts

    def follow(self, other):
        self.following.append(other)
