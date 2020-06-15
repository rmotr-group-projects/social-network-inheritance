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
#         super(Post, self).__init__(text)
        
        self.text = text
        self.timestamp = timestamp
        self.user = None
        

    def __str__(self):
        return str('@{first_name} {last_name}: "{text}"\n\t{date}'.format(
            first_name = self.user.first_name, ### How is there a link with the class User that makes it so we can access self.user.first_name?
            last_name = self.user.last_name, 
            text = self.text, 
            date = self.timestamp.strftime("%A, %b %d, %Y")))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp

    def __str__(self):
        return str('@{first_name} {last_name}: "{text}"\n\t{img}\n\t{date}'.format(
            first_name = self.user.first_name,
            last_name = self.user.last_name, 
            text=self.text, 
            img = self.image_url, 
            date = self.timestamp.strftime("%A, %b %d, %Y")))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def __str__(self):
        return str('@{first_name} Checked In: "{text}"\n\t{lat}, {long}\n\t{date}'.format(
            first_name = self.user.first_name,
            text=self.text, 
            lat = self.latitude,
            long = self.longitude, 
            date = self.timestamp.strftime("%A, %b %d, %Y")))
