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

# --------------------------------------- Class -------------------------------------


class Data:
    def __init__(self, source_file, sep=' ', output=None):
        self._sep = sep
        self._init_input(source_file)
        self._output_path = output
        self._output_data = []
        
    def _init_input(self, source_file):
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