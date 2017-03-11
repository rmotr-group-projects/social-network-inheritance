from datetime import datetime


class Post(object):
     def __init__(self, text, timestamp=None):
         self.text = text
         self.timestamp = timestamp
         self.user = None

     def set_user(self, user):
         self.user = user 

class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        #'@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'
        return '@{first_name} {last_name}: "{text}"\n\t{time}'.format(
            first_name=self.user.first_name, last_name=self.user.last_name,
            text=self.text, time=self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        
    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{image_url}\n\t{time}'.format(
            first_name=self.user.first_name, last_name=self.user.last_name,
            text=self.text, image_url=self.image_url, time=self.timestamp.strftime('%A, %b %d, %Y'))
#'@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'
# stamp = self.timestamp.strftime('%A %b %d, %Y')
# #post_2 = PicturePost("Check my new submarine.", image_url='imgur.com/submarine.jpg')
# ="-9.2222")


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

# '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
    def __str__(self):
        return '@{first_name} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{time}'.format(
            first_name=self.user.first_name, text=self.text,
            latitude = self.latitude, longitude=self.longitude, 
            time=self.timestamp.strftime('%A, %b %d, %Y'))
# @Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
