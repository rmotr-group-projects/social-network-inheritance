
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name =first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
        #self.timeline = []
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    __repr__ = __str__

    def add_post(self, a_post):
        self.posts.append(a_post)
        return self.posts

    def get_timeline(self):
        result = []
        if self.following:
            for user in self.following:
                for post in user.posts:
                    result.append(post)
            return result

    def follow(self, other):
        self.following.append(other)
        return self.following
    
    def __setitem__(self, key, value):
        self.timeline[key] = value
