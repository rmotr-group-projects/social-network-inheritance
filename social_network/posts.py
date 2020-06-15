from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp

    def set_user(self, user):
        self.user = user
        
        
class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        #super().__init__(text, timestamp) -Python3
        super(TextPost, self).__init__(text, timestamp)
        self.user = None
        
    def __str__(self):
        return '@{f_name} {l_name}: "{text}"\n\t{timestamp}'.format(
            f_name=self.user.first_name, l_name=self.user.last_name,
            text=self.text, timestamp=self.timestamp.strftime("%A, %b %d, %Y"))
            
        
class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        #super().__init__(text, timestamp) -Python3
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{f_name} {l_name}: "{text}"\n\t{image}\n\t{timestamp}'.format(
            f_name=self.user.first_name, l_name=self.user.last_name,
            text=self.text, image=self.image_url,
            timestamp=self.timestamp.strftime("%A, %b %d, %Y"))
            

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        #super().__init__(text, timestamp) -Python3
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return ('@{f_name} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t'
            '{timestamp}').format(
                f_name=self.user.first_name, l_name=self.user.last_name,
                text=self.text, latitude=self.latitude, longitude=self.longitude,
                timestamp=self.timestamp.strftime("%A, %b %d, %Y"))
