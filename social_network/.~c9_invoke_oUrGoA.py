from datetime import datetime
fr

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = datetime.d.strftime("%A, %B %d, %Y")

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        # super(Subclass, BaseClass).__init__(attributes)  
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        # ''' '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017' '''
        return ('@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        #@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017
        return ('@{} {}: {} \n\t {} \n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        

    def __str__(self):
        # '''''@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'''''
        return ('@{} Checked In: {} \n\t{} {} \n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp))


        