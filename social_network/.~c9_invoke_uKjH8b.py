from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        # super(Subclass, BaseClass).__init__(attributes)  
        super(TextPost, self).__init__(text)
        self.user = None
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp

    def __str__(self):
        # ''' '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017' '''
        return ('@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime("%A, %b %d, %Y")))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text)
        self.image_url = image_url
        self.user = None
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp

    def __str__(self):
        #@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017
        return ('@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp.strftime("%A, %b %d, %Y")))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text)
        self.user = None
        self.latitude = latitude
        self.longitude = longitude
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp
        

    def __str__(self):
        # '''''@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'''''
        return ('@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.ser.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime("%A, %b %d, %Y")))


        