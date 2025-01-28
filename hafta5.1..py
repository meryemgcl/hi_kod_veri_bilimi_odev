#!/usr/bin/env python
# coding: utf-8

# In[9]:


liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]   
liste[3]    


# In[10]:


liste[5]


# In[11]:


liste[7]


# In[12]:


liste[-1]


# In[13]:


liste[2:6]


# In[14]:


liste[4:8]


# In[17]:


yeni_liste = []    
for eleman in liste:    
    if type(eleman) ==str:    
        yeni_liste.append(eleman)    
        
        yeni_liste


# 

# In[19]:


meyveler = ["elma", "armut", "çilek"]    
for index in range(len(meyveler)):    
    print("{}.indexte bulunan meyve: {}".format(index,meyveler[index]))


# In[21]:


meyveler = ["elma", "armut", "çilek"]    
for index, meyve in enumerate(meyveler, 1):    
    print("{}. indexte bulunan meyve: {} ".format(index, meyve))


# In[ ]:




