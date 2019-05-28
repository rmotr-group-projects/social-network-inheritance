from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp is not None:
            self.timestamp = timestamp.strftime('%A, %b %d, %Y')
        else:
            self.timestamp = timestamp
    def set_user(self, user=None):
        self.user = user

#TextPostFactory.set_user(UserFactory(first_name = 'Kevin',last = 'Watson')
class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost,self).set_user()
        super(TextPost,self).__init__(text, timestamp)
               
    def __str__(self):       
        return "@{first} {last}: \"{text}\"\n\t{timestamp}".format(
            first = self.user.first_name, 
            last = self.user.last_name, 
            text = self.text, 
            timestamp = self.timestamp)

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost,self).set_user()
        super(PicturePost,self).__init__(text, timestamp)
        self.image_url = image_url
        
    def __str__(self):
         return "@{first} {last}: \"{text}\"\n\t{url}\n\t{timestamp}".format(
             first = self.user.first_name, 
             last = self.user.last_name, 
             text = self.text, 
             url = self.image_url,
             timestamp = self.timestamp)

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost,self).set_user()
        super(CheckInPost,self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        #self.timestamp = timestamp.strftime('%A, %b %d, %Y')
    def __str__(self):
        return "@{first} Checked In: \"{text}\"\n\t{lat}, {lon}\n\t{timestamp}".format(
             first = self.user.first_name, 
             last = self.user.last_name, 
             text = self.text, 
             lat = self.latitude,
             lon = self.longitude,
             timestamp = self.timestamp)

