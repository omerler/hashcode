from data import *
from img import *

class Slide:
    def __init__(self, s1, s2=None):
        if s2 is not None:
            assert s1.orientation == s2.orientation == V
            self._tags = s1.tags.union(s2.tags)
            self._n = 2
        else:
            assert (s1 is not None)
            self._tags = s1.tags
            self._n = 1
        self._s1 = s1
        self._s2 = s2
    
    def get_imgs(self):
        return (self._s1, self._s2)
    
    def get_img1(self):
        return self._s1
    
    def get_img2(self):
        return self._s2
    
    def get_tags(self):
        return copy.copy(self._tags)
    
    def num_imgs(self):
        return self._n