from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=datetime.now()):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        
    def set_user(self, user):
        self.user = user


class TextPost(Post): 
    def __init__(self, text, timestamp):
        Post.__init__(self, text, timestamp)

    def __str__(self):
        return ('@{} {}: "{}"\n\t{}'.format(
                self.user.first_name,
                self.user.last_name, 
                self.text, 
                self.timestamp.strftime(
                "%A, %b %d, %Y"))
                )


class PicturePost(Post): 
    def __init__(self, text, image_url, timestamp):
        Post.__init__(self, text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return ('@{} {}: "{}"\n\t{}\n\t{}'.format(
                self.user.first_name, 
                self.user.last_name, 
                self.text, 
                self.image_url, 
                self.timestamp.strftime(
                "%A, %b %d, %Y"))
                )


class CheckInPost(Post): 
    def __init__(self, text, latitude, longitude, timestamp):
        Post.__init__(self, text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return ('@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(
                self.user.first_name,
                self.text, 
                self.latitude, 
                self.longitude, 
                self.timestamp.strftime(
                "%A, %b %d, %Y"))
                )
