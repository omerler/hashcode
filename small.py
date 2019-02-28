import data
import slide
from score import *
import random
import img
import naive
import numpy as np
SA_RANDOM_ITERATIONS = 50
Tmin = 0.001
alpha = 0.995
initial_p = 0.95

def probability(T, energy):
    debug = np.exp(-energy / T)
    return random.random() < np.exp(-energy/T)

def replace_two_slides(slides,slide_ind_x, slide_ind_y):
    tmp_slide = slides[slide_ind_x]
    slides[slide_ind_y] = slides[slide_ind_x]
    slides[slide_ind_y] = tmp_slide

def switch_random_slides(slides, T):
    slide_ind_x = random.randint(0, 80000 - 1)
    slide_ind_y = random.randint(0, 80000 - 1)
    s = score()
    currentscore = s.score_two(slides[slide_ind_x -1],slides[slide_ind_x])
    currentscore += s.score_two(slides[slide_ind_x], slides[slide_ind_x +1])
    currentscore += s.score_two(slides[slide_ind_y -1],slides[slide_ind_y])
    currentscore += s.score_two(slides[slide_ind_y], slides[slide_ind_y +1])
    newscore     =  s.score_two(slides[slide_ind_x -1],slides[slide_ind_y])
    newscore     += s.score_two(slides[slide_ind_y], slides[slide_ind_x + 1])
    newscore     +=  s.score_two(slides[slide_ind_y -1],slides[slide_ind_x])
    newscore     += s.score_two(slides[slide_ind_x], slides[slide_ind_y + 1])
    if newscore > currentscore:
        replace_two_slides(slides,slide_ind_x,slide_ind_y);
        return
    chance = probability(T, (new_price - price))
    if chance == True:
        return
    else:
        replace_two_slides(slides,slide_ind_x,slide_ind_y);
        return

def run_sa(slides):
    T0 = -80000/ np.log(initial_p)
    for sa_random_iteration in range(SA_RANDOM_ITERATIONS):
        print "iteration %d" % sa_random_iteration
        T = T0
        random.shuffle(slides)
        while T > Tmin:
            switch_random_slides(slides, T)
            T *= alpha

if __name__ == '__main__':
    data = data.Data("b_lovely_landscapes.txt")
    s1 = naive.combine_vertical_imgs_naive(data.get_v())
    s2 = naive.make_slides_of_horz_img(data.get_h())
    print len(s1)
    slides = s1 + s2
    run_sa(slides)
