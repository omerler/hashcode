#!/usr/bin/env python

# --------------------------------------- Imports -------------------------------------

import                                          numpy as np
import                                          pandas as pd
import                                          matplotlib.pyplot as plt
from matplotlib.ticker import                   MaxNLocator
import                                          pickle
import                                          PIL
import                                          scipy
import                                          sklearn
import                                          pyaudio
import                                          plotly
import                                          time, datetime
# import                                          keras
import copy
# --------------------------------------- Class -------------------------------------
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
        

class Data:
    def __init__(self, source_file, sep=' ', output=None):
        self._sep = sep
        self._verticals = []
        self._orizontals = []
        self._init_input(source_file)
        self._output_path = output
        self._output_data = []
        
    def _init_input(self, source_file):
        self.images
        with open(source_file, 'r') as f:
            for line in f.readlines():
                
        self._data_array = pd.read_csv(source_file, sep=self._sep, header=None).values
        
    def show(self, title='', save=False, show_values=False):
        fig, ax = plt.subplots()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        fig.tight_layout()
        im = ax.imshow(self._data_array)
        cur_time = datetime.datetime.fromtimestamp(time.time())
        ax.set_title('{} ({})'.format(title, cur_time.strftime('%H:%M:%S')))
        if save:
            plt.savefig('{}_{}'.format(title, cur_time.strftime('%H_%M_%S')))
        if show_values:
            r, c = self._data_array.shape
            for i in range(r):
                for j in range(c):
                    im.ax.text(j, i, self._data_array[i, j], ha="center", va="center", color="w")
        plt.show()
            
    def set(self, x, y, value):
        self._data_array[x, y] = value
        
    def get(self, x, y):
        return self._data_array[x, y]
    
    def get_data_array(self):
        """ Returns a copy (!) """
        return self._data_array.copy()
    
    def set_data_array(self, new_data):
        self._data_array = new_data
            
    def add_solution_line(self, line_str):
        self._output_data.append(line_str)
        
    def dump(self, output_path=None, output_data=None):
        if not output_path and not self._output_path:
            raise ValueError('no output file defined')
        with open(output_path if output_path else self._output_path, 'w') as f:
            for data_line in output_data if output_data else self._output_data:
                f.write(data_line + '\n')

# --------------------------------------- Run -------------------------------------
        
if __name__ == '__main__':
    source_file = 'data_example.txt'
    data = Data(source_file)
    print(data.get(1, 1))
    print(data.get(2, 1))
    data.show(title='our data is beautiful', save=True)
    data.add_solution_line('1: 2, 3')
    data.add_solution_line('3: 4, 4')
    data.dump('test_output.txt')