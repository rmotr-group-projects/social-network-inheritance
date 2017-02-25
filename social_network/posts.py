from datetime import datetime
from accounts import User
import time

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if not timestamp: 
            self.timestamp = datetime.now()
        else: 
            self.timestamp = timestamp

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
        self.user = None
       
    def __str__(self):
        return "@" + self.user.first_name + " " + self.user.last_name + ": " + '"' + self.text + '"' + "\n\t" + str(self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        self.user = None

        
    def __str__(self):
        return "@" + self.user.first_name + " " + self.user.last_name + ": " + '"' + self.text + '"' + "\n\t" + str(self.image_url) + "\n\t"  + str(self.timestamp.strftime("%A, %b %d, %Y"))

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        self.user = None

    def __str__(self):
        return "@" + self.user.first_name + " Checked In: " + '"' + self.text + '"' + "\n\t" + str(self.latitude) + ", " + str(self.longitude) + "\n\t" + str(self.timestamp.strftime("%A, %b %d, %Y")) 
