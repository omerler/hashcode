import data
import random
SA_RANDOM_ITERATIONS = 50
Tmin = 0.001
alpha = 0.995
initial_p = 0.95
erez
def probability(T, energy):
    debug = np.exp(-energy / T)
    return random.random() < np.exp(-energy/T)

def replace_two_slides(slides,slide_ind_x, slide_ind_y):
    tmp_slide = slides[slide_ind_x]
    slides[slide_ind_y] = slides[slide_ind_x]
    slides[slide_ind_y] = tmp_slide

def switch_random_slides(slides, T):
    slide_ind_x = find_index(slides, random.randint(0, 80000 - 1))
    slide_ind_y = find_index(slides, random.randint(0, 80000 - 1))
    currentscore = score_two(slide_ind_x -1,slide_ind_x)
    currentscore += score_two(slide_ind_x, slide_ind_x +1)
    currentscore += score_two(slide_ind_y -1,slide_ind_y)
    currentscore += score_two(slide_ind_y, slide_ind_y +1)
    newscore =  score_two(slide_ind_x -1,slide_ind_y)
    newscore += score_two(slide_ind_y, slide_ind_x + 1)
    newscore +=  score_two(slide_ind_y -1,slide_ind_x)
    newscore += score_two(slide_ind_x, slide_ind_y + 1)
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
            switch_random_unit(racks, T, connection_array, price)
            T *= alpha

if __name__ == '__main__':
