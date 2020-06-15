
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following =[]
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        list_follow = []
        for user in self.following:
            # list_follow += user.posts
            for post in user.posts:
                list_follow.append(post)
        return list_follow
    

    def follow(self, other):
        self.following.append(other)
