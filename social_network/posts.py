from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        if not timestamp:
            self.timestamp = datetime.now()
        self.user = None
        pass

    def set_user(self, user):
        self.user = user
        pass
    
    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__,self.text)
        
    def __lt__(self, other):
        return self.timestamp < other.timestamp
        
    def _get_str_date(self):
        return self.timestamp.strftime("%A, %b %d, %Y")
        


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost,self).__init__(text, timestamp)
        

    def __str__(self):
        return "@{} {}: \"{}\"\n\t{}".format(self.user.first_name, self.user.last_name, self.text, self._get_str_date())



class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text,timestamp)
        self.image_url = image_url

#
    def __str__(self):
        return "@{} {}: \"{}\"\n\t{}\n\t{}".format(self.user.first_name, self.user.last_name, self.text,self.image_url, self._get_str_date())


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):
        return "@{} Checked In: \"{}\"\n\t{}, {}\n\t{}".format(self.user.first_name, self.text,self.latitude,self.longitude, self._get_str_date())

