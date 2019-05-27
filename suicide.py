import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('master.csv')



x= df.groupby(['country', 'year']).suicides_no.sum().reset_index()

x.rename(columns = {'suicides_no': 'Suicide number'}, inplace= True)


