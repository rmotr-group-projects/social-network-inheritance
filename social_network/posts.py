from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp, user=None):
        self.text = text
        if timestamp:
            a = timestamp.strftime("%A, %b %d, %Y")
            self.timestamp = a
        else: 
            self.timestamp = timestamp
        self.user = user 
        
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp)

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp, user = None):
        super(PicturePost, self).__init__(text, timestamp, user = None)
        self.image_url = image_url
        
    def __str__(self):
       return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp, user = None):
        super(CheckInPost, self).__init__(text, timestamp, user = None)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):     
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp)