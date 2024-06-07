import pandas as pd
import numpy as np

def create_csv_file(n):
    array = np.arange(sizes[n]-1)+1
    print('creating dataframe')
    df = pd.DataFrame(array)
    print('saving dataframe')
    df.to_csv(f'D:/University/Master/Massive Data Algorithms/project 1/file_{n}.csv', index=False) 
    print('done')


# sizes = [1_000_000, 10_000_000, 100_000_000, 1_000_000_000]
sizes = {
    '10M': 1_262_000, 
    '100M': 11_352_000, 
    '1G': 103_200_000,
    '10G': 990_000_000,
    }
# for s in sizes.keys():
#     create_csv_file(s)
create_csv_file('10G')
