from data import *
from slide import *

H = 'H'
V = 'V'

class Img:
    def __init__(self, orientation, tags):
        assert orientation in (H, V) and type(tags) == set
        self.orientation = orientation
        self.tags = tags
    
    def orientation(self):
        return self.orientation
    
    def tags(self):
        return copy.copy(self.tags)