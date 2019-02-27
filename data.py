
# --------------------------------------- Imports -------------------------------------

import              numpy as np
import              pandas as pd
import              matplotlib.pyplot as plt
import              pickle
import              PIL
import              keras
import              scipy
import              sklearn
import              pyaudio
import              plotly

# --------------------------------------- Class -------------------------------------

class Data:
    def __init__(self, source_file, sep=' ', output=None):
        self._sep = sep
        self._init_input(source_file)
        self._output_path = output
        self._output_data = []
        
    def _init_input(self, source_file):
        self._data_array = pd.read_csv(source_file, sep=self._sep, header=None).values
        
    def show(self):
        plt.imshow(self._data_array)
        plt.show()
        
    def set(self, x, y, value):
        self._data_array[x, y] = value
        
    def get(self, x, y):
        return self._data_array[x, y]
    
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
    data.show()
    data.add_solution_line('1: 2, 3')
    data.add_solution_line('3: 4, 4')
    data.dump('test_output.txt')