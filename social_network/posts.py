from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        
        
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        return "@{} {}: \"{}\"\n\t{}".format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime('%A, %b %d, %Y'))

#'@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp
        self.user = None
        
    def __str__(self):
        return "@{} {}: \"{}\"\n\t{}\n\t{}".format(self.user.first_name, self.user.last_name, self.text,self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))

# dt.strftime('%m/%d/%Y')
# http://stackoverflow.com/questions/10624937/convert-datetime-object-to-a-string-of-date-only-in-python


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        return "@{} Checked In: \"{}\"\n\t{}, {}\n\t{}".format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime('%A, %b %d, %Y'))
