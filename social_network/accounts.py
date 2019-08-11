
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
        self.timeline = []
        
    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def add_post(self, post):
        self.posts.append(post)
        return self.posts

    def get_timeline(self):
        timeline = []

        for i in self.following:
            timeline += i.posts
#             timeline.append(i.posts)
        return timeline


    def follow(self, other):
        self.following.append(other)
        return self.following
