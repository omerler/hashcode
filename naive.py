import random
from data import *
from img import *
from slide import *
def combine_vertical_imgs_naive(vert_imgs):
    """ Get a list of vertical_imgs and return a list of slides"""
    slides = []
    for i in range(vert_imgs/2):
        slides.append(Slide(vert_imgs(2*i),vert_imgs(2*i+1)))
    return slides
def combine_vertical_imgs_diver(vert_imgs):
    slides = []
    while len(vert_imgs)>0:
        cur_img = vert_imgs.pop(0)
        for img in vert_imgs:
            if img.tags.intersection(img0.tags) == set():
                slides.append(Slide(cur_img,img))
                vert_imgs.remove(img)
                break
    return slides
def make_slides_of_horz_img(horz_imgs):
    slides = []
    for img in horz_imgs:
        slides.append(Slide(img))
    return slides
def greedy(slides):
    res_slides = []
    s0 = random.choice(slides)
    res_slides.append(s0)
    slides.remove(s0)
    best_score = 0
    best_slide = 0
    while len(slides)>0:
        for slide in slides:
            score = score_two(s0,slide)
            if score > best_score:
                best_score = score
                best_slide = slide
        res_slides.append(slide)
        slides.remove(slide)
        if len(slides)%100==0:
            print len(slides)
    return res_slides
    
            
    
