from datetime import datetime


class Post(object):
   def __init__(self, text, timestamp=None):
      pass
    
   def set_user(self, user = None):
      self.user = user


class TextPost(Post):  
    def __init__(self, text, timestamp=None):
       self.text = text
       self.timestamp = timestamp or datetime.now()
       self.user = None
    
    def __str__(self):
       return '@{} {}: "{}"\n\t{}'.format(self.user.first_name,\
       self.user.last_name, self.text, self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):  
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp or datetime.now()
        self.user = None

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name,\
        self.user.last_name, self.text, self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):  
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp or datetime.now()
        self.user = None

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name,\
        self.text, self.latitude, self.longitude, self.timestamp.strftime('%A, %b %d, %Y'))
