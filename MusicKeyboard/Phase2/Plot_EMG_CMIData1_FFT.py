#!/usr/bin/env python
# coding: utf-8

# In[134]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[135]:


import pandas
data = pandas.read_csv("./Data/AllinOne_Data1.csv")

print (data.shape)
#len = len(data.rows)


# In[136]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import gc
# first column in excecl has index and last has results. ignore them for plots
y=data.iloc[:, -1]
emgData = data.iloc[:, :-1]
len_row = len(emgData)
print('{0} and {1} shape'.format( emgData.shape, len_row))
#print(emgData.head(5))
len_row = 900
action = 0

for action in range(action, len_row, 30):
    for trial in range (0, 30, 1):
        #print ('{0} and {1}'.format(t, len_row))
        emg = emgData.loc[action+trial]
        n = len(emg)//2
        #print("len = {0}".format(n))
        emg1 = emg[0:n]
        emg2 = emg[n+1:]
        
        # Number of samplepoints
        N = len(emg1)
        # sample spacing
        T = 1/500
        
        fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
        # Remove horizontal space between axes
        fig.subplots_adjust(hspace=0)
        
        fig_name = y.iloc[action+trial]        
        fig_name = fig_name + '_' + str(trial)
        fig.suptitle(fig_name, fontsize=16)
        
        yf = scipy.fftpack.fft(emg1)
        xf = np.linspace(0.0, 1.0/(2.0*T), N/2)                
        axs[0].plot(xf[1:], 2.0/N * np.abs(yf[1:N//2]))
        axs[0].title.set_text('Electrode 1')
        fig.set_size_inches(w=20,h=7)
        
        yf = scipy.fftpack.fft(emg2)
        xf = np.linspace(0.0, 1.0/(2.0*T), N/2)        
        axs[1].plot(xf[1:], 2.0/N * np.abs(yf[1:N//2]), 'C1')        
        axs[1].title.set_text('Electrode 2')        
        axs[1].set_xlabel('Freq |Hz|')        
        fig.set_size_inches(w=20,h=7)        

        #plt.ylim(0,5)  #fix range
        fig.savefig('2019_Plot_CMI_EMG_Data1_FFT/' + fig_name)         
        plt.close()
        gc.collect() #explicit garbage collection
        


# In[ ]:




