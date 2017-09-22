class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
        

    def add_post(self, post):
        post.user = self
        self.posts.append(post)
        
    def get_timeline(self):
        news_feed = []
        for follower in self.following:
            for post in follower.posts:
                news_feed.append(post)
        return news_feed

    def follow(self, other):
        #Keeps track of all users I follow
        self.following.append(other)
