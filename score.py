from slide import *
from img import *
from data import *

def score_two_prev(s1, s2):
    s1_tags = s1.get_tags()
    s2_tags = s2.get_tags()
    inter = len(s1_tags.intersection(s2_tags))
    left = len(s1_tags - s2_tags)
    right = len(s2_tags - s1_tags)
    return min(inter, left, right)

def score_two(s1, s2):
    s1_vec = s1.get_vec()
    s2_vec = s2.get_vec()
    inter = np.sum(s1_vec & s2_vec)
    left = np.sum(s1_vec & (~s2_vec))
    right = np.sum((~s1_vec) & s2_vec)
    return np.min([inter, left, right]).astype(int)

def score_all_prev(solution):
    total_score = 0
    for i in range(len(solution)-1):
        total_score += score_two_prev(solution[i], solution[i+1])
    return total_score


def score_all(solution):
    total_score = 0
    for i in range(len(solution)-1):
        total_score += score_two(solution[i], solution[i+1])
    return total_score

