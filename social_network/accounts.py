
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
        
    def add_post(self, post):
        #Update post post.user attribute to self.
        post.set_user(self)
        self.posts.append(post)

    def get_timeline(self):
        list_of_posts = []
        #get all posts from followers, add to this list, then sort the list.
        for followed_user in self.following:
            for post in followed_user.posts:
                list_of_posts.append(post)
        return sorted(list_of_posts, key=lambda x: x.timestamp, reverse=True)
        
    def follow(self, other):
        self.following.append(other)


#list = ['a: apple', 2, 1]
#list.sort() !changes list to [1, 2, 3]

#sorted(list_to_be_operated_on, key, reverse=True/False)
#sorted(list_of_posts, !Pseudocode: take an object and return timestamp, reverse )
#Google: sorted list by object attribute
#lambda - an anonyomous function
#
#
#def gets_timestamp_from_object(an_object):
#   return an_object.timestamp
# find_object_timestamp = lambda x : x.timestamp
# for i in list_of_posts