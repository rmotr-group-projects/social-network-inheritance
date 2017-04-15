from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None, image_url=None, latitude=None, longitude=None):
        self.text = text
        self.user = None
        if timestamp:
            self.timestamp = timestamp.strftime("%A, %b %d, %Y") 
            # Friday, Feb 03, 2017 (format)
        if image_url:
            self.image_url = image_url  
        if latitude:
            self.latitude = latitude
        if longitude:
            self.longitude = longitude  # image_url and latitude are both at argument[1] in methods

    def set_user(self, user):
        self.user = user


class TextPost(Post):  
    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp)


class PicturePost(Post):  # Inherit properly
#    def __init__(self, text, image_url, timestamp=None):
#        self.image_url = image_url

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp)


class CheckInPost(Post):  # Inherit properly
#    def __init__(self, text, latitude, longitude, timestamp=None):
#        self.latitude = latitude
#        self.longitude = longitude

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp)
