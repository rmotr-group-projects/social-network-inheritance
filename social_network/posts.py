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
        return self.user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text)
        if timestamp:
            self.timestamp = datetime.strftime(timestamp, '%A, %b %d, %Y')

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{date}'.format(first_name=self.user.first_name, last_name=self.user.last_name,text=self.text,date=self.timestamp)


class PicturePost(TextPost):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{image}\n\t{date}'.format(image=self.image_url,first_name=self.user.first_name, last_name=self.user.last_name,text=self.text,date=self.timestamp)



class CheckInPost(TextPost):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{first_name} Checked In: "{text}"\n\t{lat}, {longi}\n\t{date}'.format(first_name=self.user.first_name, text=self.text,lat=self.latitude,longi=self.longitude, date=self.timestamp)

