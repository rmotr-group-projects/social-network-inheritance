from social_network.accounts import User
from social_network.posts import TextPost, PicturePost, CheckInPost

from datetime import datetime,date

john = User("John", "Lennon", "john@rmotr.com")
text_post = TextPost("All you need is love!")
text_post.user == None  # Important! Since the post has no user yet, the user attribute should be None.

john.add_post(text_post)

text_post.user == john  # Important!
len(john.posts)

john = User("John", "Lennon", "john@rmotr.com")
paul = User("Paul", "McCartney", "paul@rmotr.com")

john.follow(paul)
print(john.following)

john = User("John", "Lennon", "john@rmotr.com")
paul = User("Paul", "McCartney", "paul@rmotr.com")
george = User("George", "Harrison", "george@rmotr.com")

john.follow(paul)
john.follow(george)

paul.add_post(TextPost("Post 1",datetime.now()))
george.add_post(TextPost("Post 2",datetime.now()))
paul.add_post(TextPost("Post 3",datetime.now()))

print(john.following)

print(john.get_timeline())
for entry in john.get_timeline():
    print(entry.text, entry.timestamp)



text_post_1 = TextPost("All you need is love!")
picture_post_2 = PicturePost("Check my new submarine.", image_url='imgur.com/submarine.jpg')
checkin_post_3 = CheckInPost("At Abbey Road Studios", latitude="19.111", longitude="-9.2222")
john.add_post(text_post_1)
john.add_post(picture_post_2)
john.add_post(checkin_post_3)


print(text_post_1)


print(picture_post_2)

print(checkin_post_3)
