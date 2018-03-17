
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        self.timeline = []

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    def get_timeline(self):
        for user in self.following:
            self.timeline.extend(user.posts)

        self.timeline = list(set(self.timeline))
        return self.timeline

    def follow(self, other):
        if other not in self.following:
            self.following.append(other)
            self.timeline.extend(other.posts)

    def __str__(self):
        return '<User: "{0} {1}">'.format(self.first_name, self.last_name).title()

    __repr__ = __str__

    def __contains__(self, item):
        if item.__class__ == 'User':
            return item in self.following
        return item in self.get_timeline()
