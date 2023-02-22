#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas
data = pandas.read_csv("./Data/AllinOne_Data1.csv")

print (data.shape)
#len = len(data.rows)


# In[21]:


# Get 30 Samples in each user/action
import numpy as np
import gc
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
        #print ('{0} and {1}'.format(t, len_row))
        emg = emgData.loc[x+t]
        #print(emg.shape)
        len(emgData.loc[x+t])
        emg1 = emg[1:3000] #to avoid the outlier  in 0th position
        # plot 3000 samples in 5 seconds 3000/5
        time1 = np.array([i/600 for i in range(0, emg1.size, 1)]) #sampling rate 500Hz    
        emg2 = emg[3001:6000]
        
        
        fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
        # Remove horizontal space between axes
        fig.subplots_adjust(hspace=0)
        axs[0].plot(time1, emg1)   
        axs[0].title.set_text('Electrode 1')
        
        axs[1].plot(time1, emg2, 'C1')
        axs[1].title.set_text('Electrode 2')
        plt.ylim(-5,5)  #fix range
        plt.xlabel('Time (sec)')
        plt.ylabel('EMG ')       
        fig_name = y.iloc[x+t]
        print('{0},{1}'.format( x, t))
        fig_name = fig_name + '_' + str(t)
        fig.suptitle(fig_name, fontsize=16)
        fig.set_size_inches(w=20,h=7)
        #plt.show()
        fig.savefig('2019_Plot_CMI_EMG_Data1_SameRange/' + fig_name) 
        plt.close()
        gc.collect() #explicit garbage collection
       


# In[4]:


# Get 30 Samples in each user/action
import numpy as np
import gc
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
        emg = emgData.loc[x+t]
        print ('t ={0}, len={1}, mean={2}'.format(t, len_row, np.mean(emg)))
        
        
        emg = emg[1:] #to avoid the outlier  in 0th position
        time = np.array([i/600 for i in range(0, emg.size, 1)]) #sampling rate 500Hz    
    gc.collect() #explicit garbage collection


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





# In[ ]:




