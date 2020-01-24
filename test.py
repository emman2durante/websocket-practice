import datetime
class Holiday:

    def __init__(self):
        self.date_now = datetime.datetime.now()

    def get_theme(self):
        d_24 = datetime.datetime(2019, 12, 24) 
        d_25 = datetime.datetime(2019, 12, 25) 

        if self.date_now in [d_24, d_25]:
            return "Christmas"
        else:
            return "Not Christmas"
