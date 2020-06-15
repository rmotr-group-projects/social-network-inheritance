
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
        pass

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
        pass

    def get_timeline(self):
        result = []
        for followed_user in self.following:
            for post in followed_user.posts:
                result.append(post)
        return sorted(result, reverse=True)
        pass

    def follow(self, other):
        self.following.append(other)
        pass

    
    def __repr__(self):
        return "<User: {} {}>".format(self.first_name, self.last_name)
        
