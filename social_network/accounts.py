
class User(object):
    first_name=None
    last_name=None
    email=None
    following=[]
    timeline=[]
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts=[]
        
    def add_post(cls, post):
        post.set_user(cls)
        cls.posts.append(post)
           
    @classmethod
    def get_timeline(self):   
        vtime = []
        for uuser in self.following:
            print(uuser.first_name)
            for i in uuser.posts:
                vtime.append(i)
        return vtime

    def follow(self, other):
        self.following.append(other)
