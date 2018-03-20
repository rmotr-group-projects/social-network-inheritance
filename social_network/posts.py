from datetime import datetime


class Post(object):
    user = None
    
    def __init__(self, text, timestamp=None):
        self.text = text
        

    def set_user(self, user):
        self.user = user

    def __repr__(self):
        rep = "{}'s post at {}".format(self.user, self.timestamp.strftime('%A, %b %d, %Y'))
        return rep
    
class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp

    def __str__(self):
        return '@{}: "{}"\n\t{}'.format(self.user, self.text, self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.image_url = image_url

    def __str__(self):
        return '@{}: "{}"\n\t{}\n\t{}'.format(self.user, self.text, self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def __str__(self):
        answer = '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime('%A, %b %d, %Y'))
        print(answer)
        return answer
