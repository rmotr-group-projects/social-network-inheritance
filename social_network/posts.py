from datetime import datetime
from social_network.accounts import *


class Post(object):
    def __init__(self, text, timestamp=None or datetime.now()):
        pass

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None or datetime.now()):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        

    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name,\
        self.text, self.timestamp.strftime("%A, %b %d, %Y"))
        

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None or datetime.now()):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp
        self.user = None
        

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name,\
        self.text, self.image_url, self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None or datetime.now().strftime("%A, %B %d, %Y")):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name,\
        self.text, self.latitude, self.longitude, self.timestamp.strftime("%A, %b %d, %Y"))
