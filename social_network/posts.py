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


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost,self).__init__(text,timestamp)
        
    def __str__(self):
        return '@{first} {last}: "{text}"\n\t{date}'.format(first=self.user.first_name, last=self.user.last_name, text=self.text, date=self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost,self).__init__(text,timestamp)
        self.image_url = image_url
      

    def __str__(self):
        return '@{first} {last}: "{text}"\n\t{img}\n\t{date}'.format(first=self.user.first_name, last=self.user.last_name, text=self.text, img=self.image_url, date=self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost,self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):
        return '@{first} Checked In: "{text}"\n\t{lat}, {log}\n\t{date}'.format(first=self.user.first_name, text=self.text, lat=self.latitude,log=self.longitude, date=self.timestamp.strftime("%A, %b %d, %Y"))

