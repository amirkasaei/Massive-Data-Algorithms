import time
import numpy as np

def read_array(x, rand_index, mode):

    if mode == 'Sequential':
        for y in x:
            z=y 
    else:
        for i in rand_index:
            z= x[i]
        
        
        

def main():
    sizes = {
    '1M': 1_000_000, 
    '10M': 10_000_000, 
    '100M': 100_000_000, 
    '1G': 1_000_000_000
    }
    
    modes = ['Sequential', 'Random']
    
    for mode in modes:
        print('-'*20, mode, '-'*20)
        
        for s in sizes.keys():
            # create a random array with given number of elements
            x = list(np.random.randn(sizes[s]))
            
            rand_index = None
            if mode == 'Random': # generate random indicies
                rand_index = np.arange(sizes[s]) # indiceis from 0 to N-1
                np.random.shuffle(rand_index) # shuffle to get random indicies


            start_time = time.time() # start time
            read_array(x, rand_index, mode) # read array
            end_time = time.time() # end time
            
            elapsed_time = end_time-start_time # access time
            
            print(f"Array size {s} read time: {elapsed_time:.4f} seconds")


main()
