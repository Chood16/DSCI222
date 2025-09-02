import numpy as np
Player = Team = ATT = CMP = YDS = TDS = INTS = RUSH_ATT = RUSH_YDS = RUSH_TDS = FL = FPTS = None

filename = 'QB_Projections.csv'

columns = np.genfromtxt(filename, 
                        delimiter=',', 
                        dtype=None, 
                        names=True, 
                        encoding='utf-8-sig')

for name in columns.dtype.names:
    col_data = columns[name]
    globals()[name] = [str(x) for x in col_data]

# How to access a specific column
print(YDS)
