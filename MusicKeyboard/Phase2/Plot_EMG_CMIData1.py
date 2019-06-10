#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
data = pandas.read_csv("./Data/AllinOne_Data1.csv")

print (data.shape)
#len = len(data.rows)


# In[ ]:


#Video To Overlay same picture
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
y=data.iloc[:,-1]
emgData = data.iloc[:, :-1]
len_row = len(emgData)
print('{0} and {1} shape'.format( emgData.shape, len_row))
#Data Experiment 5 sec - 2 Electrode data in One Figure
#for x in range (0, len_row):
len_row = 901
x = 0
for x in range(x, len_row, 1):
    print ('{0} and {1}'.format(x, len_row))
    emg = emgData.loc[x]
    time = np.array([i/600 for i in range(0, emg.size, 1)]) #sampling rate 500Hz    
    fig = plt.figure()
    plt.plot(time, emg)
    plt.xlabel('Time (sec)')
    plt.ylabel('EMG ')        
    fig_name = y.iloc[x]
    print(fig_name)
    fig.suptitle(fig_name, fontsize=16)
    fig.set_size_inches(w=11,h=7)
    fig.savefig(fig_name)    
#    plt.show()    


# In[3]:


# Get 5 Samples in each user/action
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
y=data.iloc[:,-1]
emgData = data.iloc[:, :-1]
len_row = len(emgData)
print('{0} and {1} shape'.format( emgData.shape, len_row))
#Data Experiment 5 sec - 2 Electrode data in One Figure
#for x in range (0, len_row):
len_row = 900
x = 0
for x in range(x, len_row, 30):
    for t in range (0, 30, 1):
        print ('{0} and {1}'.format(t, len_row))
        emg = emgData.loc[x+t]
        time = np.array([i/600 for i in range(0, emg.size, 1)]) #sampling rate 500Hz    
        fig = plt.figure()
        plt.plot(time, emg)
        plt.xlabel('Time (sec)')
        plt.ylabel('EMG ')        
        fig_name = y.iloc[x+t]
        fig_name = fig_name + '_' + str(t)
        print(fig_name)
        fig.suptitle(fig_name, fontsize=16)
        fig.set_size_inches(w=11,h=7)
        fig.savefig(fig_name)    
#    plt.show()    


# In[ ]:


#Extract All Samples
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
y=data.iloc[:,-1]
emgData = data.iloc[:, :-1]
len_row = len(emgData)
print('{0} and {1} shape'.format( emgData.shape, len_row))
#Data Experiment 5 sec - 2 Electrode data in One Figure
#for x in range (0, len_row):
len_row = 901
x = 0
for x in range(x, len_row, 1):
    print ('{0} and {1}'.format(x, len_row))
    emg = emgData.loc[x]
    time = np.array([i/600 for i in range(0, emg.size, 1)]) #sampling rate 500Hz    
    fig = plt.figure()
    plt.plot(time, emg)
    plt.xlabel('Time (sec)')
    plt.ylabel('EMG ')        
    fig_name = y.iloc[x]
    fig_name = fig_name + '_' + str(x)
    print(fig_name)
    fig.suptitle(fig_name, fontsize=16)
    fig.set_size_inches(w=11,h=7)
    fig.savefig(fig_name)    


# In[ ]:




