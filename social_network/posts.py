from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp

    def set_user(self, user=None):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None, user=None):
        # super(TextPost, self).__init__(text, timestamp)
        self.text = text
        self.timestamp = timestamp.strftime('%A, %b %d, %Y')
        self.user = user
        
    def __str__(self):
        return '@{fn} {ln}: "{text}"\n\t{date}'.format(
        fn = self.user.first_name, 
        ln = self.user.last_name, 
        text = self.text, 
        date = self.timestamp)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.timestamp = timestamp.strftime('%A, %b %d, %Y')
        self.url = image_url

    def __str__(self):
        return '@{fn} {ln}: "{text}"\n\t{url}\n\t{date}'.format(
        fn = self.user.first_name, 
        ln = self.user.last_name, 
        text = self.text,
        url = self.url,
        date = self.timestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.timestamp = timestamp.strftime('%A, %b %d, %Y')
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{fn} Checked In: "{text}"\n\t{lat}, {lon}\n\t{date}'.format(
        fn = self.user.first_name, 
        text = self.text, 
        lat = self.latitude,
        lon = self.longitude,
        date = self.timestamp)
