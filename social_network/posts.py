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
        return '@{fname} {lname}: "{text}"\n\t{time}'.format(fname=self.user.first_name, lname=self.user.last_name,
                                                             text=self.text,
                                                             time=self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, timestamp,image_url):
        super(PicturePost, self).__init__(text)
        self.timestamp = timestamp
        self.image_url = image_url



    def __str__(self):
        return '@{fname} {lname}: "{text}"\n\t{img}\n\t{time}'.format(fname=self.user.first_name, lname=self.user.last_name,
                                                             text=self.text, img = self.image_url,
                                                             time=self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, timestamp, latitude, longitude):
        super(CheckInPost, self).__init__(text)
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{fname} Checked In: "{text}"\n\t{lat}, {lon}\n\t{time}'.format(fname=self.user.first_name,
                                                                      text=self.text, lat=self.latitude, lon=self.longitude,
                                                                      time=self.timestamp.strftime("%A, %b %d, %Y"))
