from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        
        if self.timestamp == None:
            self.timestamp = ""
        

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)


    def __str__(self):
        return '@{}: "{}"\n\t{}'.format(self.user, self.text, self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{}: "{}"\n\t{}\n\t{}'.format(self.user, self.text, self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime('%A, %b %d, %Y'))
    
    

