import factory
from datetime import datetime

from social_network import accounts, posts


class UserFactory(factory.Factory):
    class Meta:
        model = accounts.User

    first_name = factory.Iterator(['Kevin', 'Joe', 'Ervin', 'Daniel'])
    last_name = factory.Iterator(['Watson', 'Fowler', 'Roberts', 'Wiley'])
    email = factory.LazyAttribute(lambda u: '{}.{}@fake-domain.com'.format(
        u.first_name, u.last_name))


class PostFactory(factory.Factory):
    class Meta:
        model = posts.Post

    text = 'Sample post text'
    timestamp = datetime(2017, 1, 10)


class TextPostFactory(PostFactory):
    class Meta:
        model = posts.TextPost


class PicturePostFactory(PostFactory):
    class Meta:
        model = posts.PicturePost

    image_url = 'http://fake-domain.com/images/sample.jpg'


class CheckInPostFactory(PostFactory):
    class Meta:
        model = posts.CheckInPost

    latitude = -34.603722
    longitude = -58.381592

    
# user = UserFactory(first_name='Kevin', last_name='Watson')
# post1 = TextPostFactory()
# post1.set_user(user)

# print(str(post1))

# post3 = CheckInPostFactory()
# post3.set_user(user)

# print(str(post3))

user1 = UserFactory()
user2 = UserFactory()
user3 = UserFactory()
user4 = UserFactory()

user2_post1 = TextPostFactory()
user2_post2 = TextPostFactory()
user3_post1 = PicturePostFactory()
user4_post1 = TextPostFactory()

user2.add_post(user2_post1)
user2.add_post(user2_post2)
user3.add_post(user3_post1)
user4.add_post(user4_post1)
user1.follow(user2)
user1.follow(user3)
print(len(user1.get_timeline()))
print(user1.get_timeline())