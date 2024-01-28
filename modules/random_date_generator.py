from random import randrange
from datetime import datetime
from datetime import timedelta

class RandomDateGenerator:
    now : str
    
    def __str__(self):
         d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
         d2 = datetime.strptime('1/1/2024 4:50 AM', '%m/%d/%Y %I:%M %p')
         self.now = self.random_date(d1, d2)
         
         return self.now.strftime("%d%m%Y%H%M%S")

    def random_date(self, start, end):
        """
        This function will return a random datetime between two datetime 
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)