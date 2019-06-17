class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []

    def add_post(self, post):
        self.post = post
        return self.posts.append(self.post)

    def get_timeline(self):
        timeline_posts = []
        for user in self.following:
            for post in user.posts:
                timeline_posts.append(post)
        return timeline_posts

    def follow(self, other):
        return self.following.append(other)
