from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text=text
        self.timestamp=timestamp
        self.user=None

    def set_user(self, user):
        self.user=user


class TextPost(Post): 
    def __init__(self, text, timestamp=None):
        self.text=text
        self.timestamp=timestamp
        self.user=None

    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  
    def __init__(self, text, image_url, timestamp=None):
        self.text=text
        self.timestamp=timestamp
        self.user=None
        self.image_url=image_url

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url,self.timestamp.strftime("%A, %b %d, %Y")
)



class CheckInPost(Post): 
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text=text
        self.timestamp=timestamp
        self.user=None
        self.latitude=latitude
        self.longitude=longitude

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime("%A, %b %d, %Y"))
