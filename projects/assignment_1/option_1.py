import numpy as np

filename = 'QB_Projections.csv'

columns = np.genfromtxt(filename, 
                        delimiter=',', 
                        dtype=None, 
                        names=True, 
                        encoding='utf-8-sig')

# How to access a specific column
print(columns['YDS'])
