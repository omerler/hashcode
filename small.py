import data
import slide
from score import *
import random
import img
import naive
import numpy as np
SA_RANDOM_ITERATIONS = 5
Tmin = 0.001
alpha = 0.9995
initial_p = 0.95

def probability(T, energy):
    debug = np.exp(-energy / T)
   # print debug
    return random.random() < np.exp(-energy/T)

def replace_two_slides(slides,a, b):
    #tmp_slide = slides[slide_ind_x]
    slides[b], slides[a] = slides[a], slides[b]
    #slides[slide_ind_y] = slides[slide_ind_x]
    #slides[slide_ind_y] = tmp_slide

def switch_random_slides(slides, T):
    slide_ind_x = random.randint(1, len(slides) -2)
    slide_ind_y = random.randint(1, len(slides) -2)
    currentscore    = score_two(slides[slide_ind_x -1],slides[slide_ind_x])
    currentscore    += score_two(slides[slide_ind_x], slides[slide_ind_x +1])
    currentscore    += score_two(slides[slide_ind_y -1],slides[slide_ind_y])
    currentscore    += score_two(slides[slide_ind_y], slides[slide_ind_y +1])
    newscore        =  score_two(slides[slide_ind_x -1],slides[slide_ind_y])
    newscore        +=  score_two(slides[slide_ind_y], slides[slide_ind_x + 1])
    newscore        +=  score_two(slides[slide_ind_y -1],slides[slide_ind_x])
    newscore        += score_two(slides[slide_ind_x], slides[slide_ind_y + 1])
    if newscore > currentscore:
        replace_two_slides(slides,slide_ind_x,slide_ind_y);
        return 1
    chance = probability(T, (newscore - currentscore))
    if chance == True:
        return
    else:
        replace_two_slides(slides,slide_ind_x,slide_ind_y);
        return

def run_sa(slides, data):
    try:
        dump_slides = slides
        T0 = -80000/ np.log(initial_p)
        best_score = 0
        for sa_random_iteration in range(SA_RANDOM_ITERATIONS):
            print "iteration %d" % sa_random_iteration
            T = T0
            while T > Tmin:
                flag = switch_random_slides(slides, T)
                if flag == 1:
                    debug_score = score_all(slides)
                    print debug_score
                T *= alpha
            new_score = score_all(slides)
            if new_score > best_score:
                best_score = new_score
                print "best score: " + str(best_score)
                dump_slides = slides
        print "iteration %d %d" % sa_random_iteration %best_score
        data.dump(dump_slides)
        random.shuffle(slides)
    except:
        data.dump(dump_slides)
    data.dump(dump_slides)

if __name__ == '__main__':
    data = data.Data("c_memorable_moments.txt")
    s1 = naive.combine_vertical_imgs_diver(data.get_v())
    s2 = naive.make_slides_of_horz_img(data.get_h())
    slides = s1 + s2
    new_score = score_all(slides)
    print new_score
    print score_all_vec(slides)
#    data.dump(slides)
    run_sa(slides, data)
