
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = {}
        self.posts = {}

    def add_post(self, post):
        post.set_user(self)
        self.posts[post] = post.text
        
    
    def get_posts(self): #get the user's posts in a list. Used in get_timeline()
        postlist = []
        for post in self.posts:
          postlist.append(post)
        return postlist

    def get_timeline(self):
        #Get all posts from followed users and append to a list.
        #Sort the list in descending order using timestamp attribute.
        unordered_timeline = []
        for user in self.following:
            for post in user.get_posts():
                unordered_timeline.append(post)
        return sorted(unordered_timeline, key=lambda x: x.timestamp, reverse=True)
            
    def follow(self, other):
        self.following[other] = "{} {}".format(other.first_name, other.last_name)
        return self.following
    
    def get_posts_by_followers(self):
        return self.get_timeline()