#!/usr/bin/env python

# --------------------------------------- Imports -------------------------------------

# import                                          numpy as np
# import                                          pandas as pd
# import                                          matplotlib.pyplot as plt
# from matplotlib.ticker import                   MaxNLocator
# import                                          pickle
# import                                          PIL
# import                                          scipy
# import                                          sklearn
# import                                          pyaudio
# import                                          plotly
import                                          time, datetime
# import                                          keras
import copy
from slide import *
from img import *
# --------------------------------------- Class -------------------------------------
H = 'H'
V = 'V'
            
class Data:
    
    def __init__(self, source_file, sep=' ', output=None):
        # self._sep = sep
        self._verticals = []
        self._orizontals = []
        self._init_input(source_file)
        if output:
            self._output_path = output
        else:
            cur_time = datetime.datetime.fromtimestamp(time.time())
            self._output_path = 'output_{}'.format(cur_time.strftime('%H:%M:%S'))
        self._output_data = []
        
    def _init_input(self, source_file):
        self.v_images = []
        self.h_images = []
        with open(source_file, 'r') as f:
            for i, line in enumerate(f.readlines()):
                data = line.split()
                if not i:
                    self.num_images = int(line[0])
                    continue
                orientation = data[0]
                cur_tags = set(data[2:])
                cur_img = Img(orientation, cur_tags, i - 1)
                if orientation == H:
                    self.h_images.append(cur_img)
                else:
                    self.v_images.append(cur_img)
    
    def get_v(self):
        return copy.copy(self.v_images)

    def get_h(self):
        return copy.copy(self.h_images)

    def dump(self, solution, output_path=None):
        lines = []
        lines.append(str(len(solution)))
        for slide in solution:
            indices = slide.get_indices()
            lines.append(' '.join(indices))
        with open(output_path if output_path else self._output_path, 'w') as f:
            f.writelines(lines)


        # self._data_array = pd.read_csv(source_file, sep=self._sep, header=None).values
        #
    # def show(self, title='', save=False, show_values=False):
    #     fig, ax = plt.subplots()
    #     ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    #     ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    #     fig.tight_layout()
    #     im = ax.imshow(self._data_array)
    #     cur_time = datetime.datetime.fromtimestamp(time.time())
    #     ax.set_title('{} ({})'.format(title, cur_time.strftime('%H:%M:%S')))
    #     if save:
    #         plt.savefig('{}_{}'.format(title, cur_time.strftime('%H_%M_%S')))
    #     if show_values:
    #         r, c = self._data_array.shape
    #         for i in range(r):
    #             for j in range(c):
    #                 im.ax.text(j, i, self._data_array[i, j], ha="center", va="center", color="w")
    #     plt.show()
    #
    # def set(self, x, y, value):
    #     self._data_array[x, y] = value
    #
    # def get(self, x, y):
    #     return self._data_array[x, y]
    #
    # def get_data_array(self):
    #     """ Returns a copy (!) """
    #     return self._data_array.copy()
    #
    # def set_data_array(self, new_data):
    #     self._data_array = new_data
    #
    # def add_solution_line(self, line_str):
    #     self._output_data.append(line_str)
    #

# --------------------------------------- Run -------------------------------------
        
if __name__ == '__main__':
    source_file = 'a_example.txt'
    data = Data(source_file)
#     print(data.get(1, 1))
#     print(data.get(2, 1))
#     data.show(title='our data is beautiful', save=True)
#     data.add_solution_line('1: 2, 3')
#     data.add_solution_line('3: 4, 4')
#     data.dump('test_output.txt')