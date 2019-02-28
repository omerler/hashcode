from slide import *
from img import *
from data import *


def score_two(s1, s2):
    s1_tags = s1.get_tags()
    s2_tags = s2.get_tags()
    inter = s1_tags.intersection(s2_tags)
    left = s1_tags - s2_tags
    right = s2_tags - s1_tags
    return min([inter, left, right])

def score_all(solution):
    total_score = 0
    for i in range(len(solution)-1):
        total_score += score_two(solution[i], solution[i+1])
    return total_score
