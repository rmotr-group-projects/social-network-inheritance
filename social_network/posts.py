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
        #for python 3 super().__init__(text, timestamp) below for Python 3
        super(TextPost, self).__init__(text, timestamp)
        
    def __str__(self):
        return '@{f} {l}: "{p}"\n\t{ts}'.format(f=self.user.first_name, 
        l=self.user.last_name, p=self.text, 
        ts=self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{f} {l}: "{pt}"\n\t{turl}\n\t{ts}'.format(f=self.user.first_name, 
        l=self.user.last_name, pt=self.text, turl=self.image_url, 
        ts=self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{f} Checked In: "{pt}"\n\t{lat}, {lng}\n\t{ts}'.format(
        f=self.user.first_name, pt=self.text, lat=self.latitude, lng=self.longitude, 
        ts=self.timestamp.strftime("%A, %b %d, %Y"))
