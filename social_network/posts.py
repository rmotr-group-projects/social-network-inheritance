class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp:
            timestamp = timestamp.strftime("%A, %b %d, %Y") 
        self.timestamp = timestamp
        self.user = None
    
    def set_user(self, user):
        self.user = user

class TextPost(Post):  # Inherit properly
    def __str__(self):
        return '@{}: \"{}\"\n\t{}'.format(self.user, self.text, self.timestamp)

class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url
    
    def __str__(self):
        return '@{}: \"{}\"\n\t{}\n\t{}'.format(self.user, self.text, self.image_url, self.timestamp)

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self):
        return '@{} Checked In: \"{}\"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp)
        
        
        
        
        
        
