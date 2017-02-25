from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
    def set_user(self, user):
        self.user = user


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        if self.user is not None:
            str_stamp = self.timestamp.strftime('%A, %b %d, %Y')
            return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, str_stamp)
        


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        if self.user is not None:
            str_stamp = self.timestamp.strftime('%A, %b %d, %Y')
            return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, str_stamp)


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.user = None
    
    def __str__(self):
        if self.user is not None:
            str_stamp = self.timestamp.strftime('%A, %b %d, %Y')
            return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, str_stamp)
