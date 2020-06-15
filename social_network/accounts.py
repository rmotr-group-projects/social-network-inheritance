class User(object):

    # Giving the user class initial properties.
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []

    # Adding the ability for the user to add a post using append.
    def add_post(self, post):
        self.posts.append(post)

    # Ability to refresh the user's timeline using a for loop to gather posts from  followed accounts.
    def get_timeline(self):
        timeline = []
        for _ in self.following:
            timeline += _.posts
        return sorted(timeline, key=lambda p: p.timestamp, reverse=False)

    # Adding the ability to follow using append
    def follow(self, other):
        self.following.append(other)