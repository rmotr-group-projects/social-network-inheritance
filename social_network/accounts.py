# PYTHONPATH=. py.test tests/testfile::TestCase::test_function_name
# PYTHONPATH=. py.test tests/test_accounts.py::TestUser::test_user_creation

class User(object):
    def __init__(self, first_name, last_name, email):
        # attributes assigned to each individual instance
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []


    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post) 
        
    def get_timeline(self):
        follower_posts = []
        for person in self.following:
            for post in person.posts:
                follower_posts.append(post)  
        follower_posts = sorted(follower_posts, key=lambda post: post.timestamp)
        return follower_posts
        
    def follow(self, other):
        # following attribute, add to list
        self.following.append(other)