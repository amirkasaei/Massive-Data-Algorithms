import time
import numpy as np
import os

def read_file(f, file_size, rand_index, mode):

    if mode == 'Random':
        for i in rand_index:
            f.seek(i) # random point of file
            f.read(1) # read one byte
    else:
        for _ in range(file_size):
            f.read(1) # read one byte
              
        

def main():
    sizes = ['10M', '100M', '1G', '10G']
    modes = ['Sequential', 'Random']
    
    for mode in modes:
        print('-'*20, mode, '-'*20)
    
        for size in sizes:
            with open(f'D:/University/Master/Massive Data Algorithms/project 1/file_{size}.csv') as file:
                # get size of file (number of bytes)
                file_size = file.seek(0, os.SEEK_END)
        
                # random indicies
                rand_index = None
                if mode == 'Random': # generate random indicies
                    rand_index = np.arange(file_size) # indiceis from 0 to N-1
                    np.random.shuffle(rand_index) # shuffle to get random indicies
                
                file.seek(0) # reset file cursor 
                
                start_time = time.time() # start time
                read_file(file, file_size, rand_index, mode) # read file
                end_time = time.time() # end time
                
                elapsed_time = end_time-start_time # access time
                
                print(f"File size {size} read time: {elapsed_time:.4f} seconds")
                    
                file.close()




main()

