from datetime import datetime



class Post(object):
    def __init__(self, text, user = None, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = user

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
#     def __init__(self, text, timestamp=None):
#         Post.__init__(self, text, timestamp=None)
        

    def __str__(self):
        string = '@{f_name} {l_name}: "{text}"\n\t{date}'.format(f_name= self.user.first_name, l_name= self.user.last_name, text=self.text, date = self.timestamp.strftime("%A, %b %d, %Y"))
        return string


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost,self).__init__(text,timestamp=timestamp)
        self.image_url = image_url

    def __str__(self):
        string = '@{f_name} {l_name}: "{text}"\n\t{url}\n\t{date}'.format(f_name= self.user.first_name, l_name= self.user.last_name, text=self.text,url = self.image_url, date = self.timestamp.strftime("%A, %b %d, %Y"))
        return string


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost,self).__init__(text, timestamp = timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        string = '@{f_name} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{date}'.format(f_name= self.user.first_name, text=self.text,latitude = self.latitude, longitude = self.longitude, date = self.timestamp.strftime("%A, %b %d, %Y"))
        return string
