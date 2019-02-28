from data import *
from slide import *

H = 'H'
V = 'V'

class Img:
    def __init__(self, orientation, tags, index):
        assert orientation in (H, V) and type(tags) == set
        self.orientation = orientation
        self.tags = tags
        self.i = index

    def get_index(self):
        return self.i
    
    def orientation(self):
        return self.orientation
    
    def tags(self):
        return copy.copy(self.tags)