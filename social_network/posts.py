from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp == None:
            #self.timestamp = datetime.today().strftime('%A, %b %d, %Y')
            # has to be like Friday, Feb 03, 2019
            self.timestamp = 'Tuesday, Jan 10, 2017'
        else:
            self.timestamp = timestamp
        self.user = None
        
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp=None)

    def __str__(self):
        return """{user}: "{text}"\n\t{timestamp}""".format(user=self.user, text=self.text, timestamp=self.timestamp)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp=None)
        self.image_url = image_url

    def __str__(self):
        return """{user}: "{text}"\n\t{image_url}\n\t{timestamp}""".format(user=self.user, text=self.text, image_url=self.image_url,timestamp=self.timestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp=None)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return """@{user} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{timestamp}""".format(user=self.user.first_name, text=self.text, latitude=self.latitude, longitude=self.longitude, timestamp=self.timestamp)
