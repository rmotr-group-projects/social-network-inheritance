from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    user=None
    def __init__(self, text, timestamp=None):
        self.text=text
        if timestamp:
            self.timestamp=timestamp
    @classmethod
    def set_user(self, user):
        self.user=user

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        self.text=text
        self.timestamp=timestamp
    def __str__(self):
        return "@{} {}: \"{}\"\n\t{}, {} {}, {}".format(self.user.first_name,self.user.last_name,self.text.strip(),self.timestamp.strftime("%A"), self.timestamp.strftime("%b"),self.timestamp.day,self.timestamp.year)

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text=text
        self.image_url=image_url
        self.timestamp=timestamp

    def __str__(self):
        return "@{} {}: \"{}\"\n\t{}\n\t{}, {} {}, {}".format(self.user.first_name,self.user.last_name, self.text.strip(), self.image_url ,self.timestamp.strftime("%A"), self.timestamp.strftime("%b"),self.timestamp.day,self.timestamp.year)


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text=text
        self.latitude=latitude
        self.longitude=longitude
        self.timestamp=timestamp

    def __str__(self):
       return "@{} Checked In: \"{}\"\n\t{}, {}\n\t{}, {} {}, {}".format(self.user.first_name,self.text.strip(),self.latitude,self.longitude,self.timestamp.strftime("%A"), self.timestamp.strftime("%b"),self.timestamp.day,self.timestamp.year)