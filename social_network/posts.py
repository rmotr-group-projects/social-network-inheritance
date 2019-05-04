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
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        #print('@{}: "{}"\n\t{}'.format(str(self.user), self.text, self.timestamp.strftime("%A, %b %d, %Y")))
        return str('@{}: "{}"\n\t{}'.format(str(self.user), self.text, self.timestamp.strftime("%A, %b %d, %Y")))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.image_url = image_url
        self.user = None

    def __str__(self):
        return str('@{}: "{}"\n\t{}\n\t{}'.format(str(self.user), self.text, self.image_url, self.timestamp.strftime("%A, %b %d, %Y")))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.user = None

    def __str__(self):
        return str('@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, str(self.latitude), str(self.longitude), self.timestamp.strftime("%A, %b %d, %Y")))
