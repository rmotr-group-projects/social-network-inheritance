from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

        if not self.timestamp:
            self.timestamp = datetime.now()

    def set_user(self, user):
        self.user = user

    def __repr__(self):
        return "'{}'".format(self.text)


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        ftimestamp = self.timestamp.strftime('%A, %b %d, %Y')
        return '@{0.first_name} {0.last_name}: "{1}"\n\t{2}'.format(
            self.user, self.text, ftimestamp)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        ftimestamp = self.timestamp.strftime('%A, %b %d, %Y')
        return '@{0.first_name} {0.last_name}: "{1}"\n\t{2}\n\t{3}'.format(
            self.user, self.text, self.image_url, ftimestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        ftimestamp = self.timestamp.strftime('%A, %b %d, %Y')
        return '@{0.first_name} Checked In: "{1}"\n\t{2}, {3}\n\t{4}'.format(
            self.user, self.text, self.latitude, self.longitude, ftimestamp)
