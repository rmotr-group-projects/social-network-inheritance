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
        #super().__init__(text, timestamp)
        super(TextPost,self).__init__(text,timestamp)

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{timestamp}'.format(first_name=self.user.first_name,last_name=self.user.last_name,text=self.text,timestamp=self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.image_url = image_url
        #super().__init__(text,timestamp)
        super(PicturePost,self).__init__(text,timestamp)

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{image_url}\n\t{timestamp}'.format(first_name=self.user.first_name,last_name=self.user.last_name,text=self.text,image_url=self.image_url,timestamp=self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude
        #super().__init__(text, timestamp)
        super(CheckInPost,self).__init__(text,timestamp)

    def __str__(self):
        return '@{first_name} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(first_name=self.user.first_name,text=self.text,latitude=self.latitude,longitude=self.longitude,timestamp=self.timestamp.strftime("%A, %b %d, %Y"))

