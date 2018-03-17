
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
            self.follow(user)

        self.timeline.sort(key=lambda x: x.timestamp)
        return self.timeline

    def follow(self, other):
        if other not in self.following:
            self.following.append(other)

        if other.posts:
            filter_posts = [x for x in other.posts if x not in self.timeline]
            self.timeline.extend(filter_posts)
            del filter_posts

    def __str__(self):
        return '<User: "{0} {1}">'.format(self.first_name, self.last_name).title()

    __repr__ = __str__

    def __contains__(self, item):
        if item.__class__ == 'User':
            return item in self.following
        return item in self.get_timeline()
