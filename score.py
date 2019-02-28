from slide import *
from img import *
from data import *

class score:
    
    def __init__(self):
        pass
    
    def score_two(self, s1, s2):
        s1_tags = s1.tags()
        s2_tags = s2.tags()
        inter = s1_tags.intersection(s2_tags)
        left = s1_tags - s2_tags
        right = s2_tags - s1_tags
        return min([inter, left, right])
    
    def score_all(self, solution):
        total_score = 0
        for i in range(len(solution)-1):
            total_score += self.score_two(solution[i], solution[i+1])
        return total_score
