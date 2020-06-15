from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):

    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __str__(self):
        date = self.timestamp.strftime('%A, %b %d, %Y')
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, date)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.image_url = image_url
        self.timestamp = timestamp
    def __str__(self):
        date = self.timestamp.strftime('%A, %b %d, %Y')
        return '@{} {}: "Sample post text"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name,
                                                               self.image_url, date)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
    def __str__(self):
        date = self.timestamp.strftime('%A, %b %d, %Y')
        return '@{} Checked In: "Sample post text"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.latitude,
                                                                           self.longitude, date)
