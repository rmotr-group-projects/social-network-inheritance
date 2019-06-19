from datetime import datetime



class Post(object):
    def __init__(self, text, timestamp=None, user=None):
        self.text = text
        if timestamp:
            self.timestamp = timestamp.strftime("%A, %b %-d, %Y")
        self.user = user
        

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None, user=None):
        super().__init__(text, timestamp, user)

    def __str__(self):
        str_user1 = str(self.user)
        str_post = '{}: "{}"\n\t{}'.format(str_user1, self.text, self.timestamp)
        return str_post


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None, user=None):
        super().__init__(text, timestamp, user)
        self.image_url = image_url
    def __str__(self):
        pass

    
#     def __repr__(self):
#         str_user = repr(self.user)

    def __str__(self):
        str_user1 = str(self.user)
        str_post = '{}: "{}"\n\t{}\n\t{}'.format(str_user1, self.text, self.image_url, self.timestamp)
        return str_post
    

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None, user=None):
        super().__init__(text, timestamp, user)
        self.latitude = latitude
        self.longitude = longitude
    
#     def __repr__(self):
#         str_user = repr(self.user)

    def __str__(self):
#         str_user1 = str(self.user)
        str_post = '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp)
        return str_post
    
  
