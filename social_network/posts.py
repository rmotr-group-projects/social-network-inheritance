from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user=None):
        self.user = user


class TextPost(Post):  # Inherit properly

    def __str__(self):
        return '@{firstname} {lastname}: "{text}"\n\t{timestamp}'.format(firstname=self.user.first_name, 
        lastname=self.user.last_name, text=self.text, timestamp=self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp

    def __str__(self):
        return '@{firstname} {lastname}: "{text}"\n\t{url}\n\t{timestamp}'.format(firstname=self.user.first_name, 
        lastname=self.user.last_name, text=self.text, url=self.image_url, timestamp=self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        pass

    def __str__(self):
        return '@{firstname} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(firstname=self.user.first_name,
        text=self.text, latitude=self.latitude, longitude=self.longitude, timestamp=self.timestamp.strftime('%A, %b %d, %Y'))