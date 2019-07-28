from datetime import datetime


class Post(object):
    def __init__(self, user=None, text=None, timestamp=None):
        self.user = user
        self.text = text
        self.timestamp = timestamp

    def set_user(self, user):
        self.user = user
        
    def __repr__(self):
        return '{}'.format(self)


class TextPost(Post):
    def __init__(self, user=None, text=None, timestamp=None):
        super(TextPost, self).__init__(user, text, timestamp)

    def __str__(self):
        return '{}: "{}"\n\t{}'.format(self.user, self.text, self.timestamp.strftime('%A, %b %d, %Y'))

class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(self, text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '{}: "{}"\n\t{}\n\t{}'.format(self.user, self.text, self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(self, text, timestamp)
        self.lat = latitude
        self.long = longitude

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.lat, self.long, self.timestamp.strftime('%A, %b %d, %Y'))