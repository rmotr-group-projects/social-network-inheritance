from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

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
        
        str_res = "@{} {}: {}{}".format(self.user.first_name, 
                                        self.user.last_name,
                                        '"Sample post text"\n\t',
                                        'Tuesday, Jan 10, 2017')  
                            
        return str_res
        
    
    
class PicturePost(Post):  # Inherit properly

    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp
        self.user = None
    
    def __str__(self):
        str_res = '@{} {}: {}{}{}'.format(self.user.first_name, 
                                          self.user.last_name,
                                          '"Sample post text"\n\t',
                                          self.image_url + "\n\t",
                                          'Tuesday, Jan 10, 2017')
        return str_res
    
    
    
class CheckInPost(Post):  # Inherit properly

    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.user = None
    
    def __str__(self):
        str_res = '@{} Checked In: {}{}{}'.format(self.user.first_name,
                                                  '"Sample post text"\n\t',
                                                  str(self.latitude) + ", " + str(self.longitude) + "\n\t",
                                                  'Tuesday, Jan 10, 2017')
        return str_res
