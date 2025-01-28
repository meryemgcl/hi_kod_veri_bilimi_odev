#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd    

sozluk = {
    "Kategori": ["Giyim", "Giyim", "Ayakkabı", "Aksesuar", "Ayakkabı", "Giyim", "Aksesuar", "Aksesuar", "Ayakkabı", "Giyim"],    
    "Ürün":["Kazak", "T-shirt", "Sandalet", "Küpe", "Spor Ayakkabı", "Pantalon", "Kolye", "Yüzük", "Çizme", "Ceket"],     
    "Fiyat": [300,180,450,50,700,400,150,80,850,900]
}    
          #yukarıdaki sözlüğü bir DataFrame haline getirin    
sozluk_df = pd.DataFrame(sozluk)
sozluk_df


# In[14]:


sozluk_df.loc[2,"Kategori"]    
sozluk_df.iloc[2,0]


# In[15]:


sozluk_df.loc[2,"Ürün"]    
sozluk_df.iloc[2,1]


# In[17]:


sozluk_df.iloc[4:9,:]    
sozluk_df.loc[4:8,"Kategori":"Fiyat"]


# In[18]:


sozluk_df.iloc[1:6,1]    
sozluk_df.loc[1:5,"Ürün"]


# In[19]:


sozluk_df[sozluk_df["Kategori"]=="Giyim"]


# In[20]:


sozluk_df["Kategori"]=="Ayakkabı"


# In[21]:


sozluk_df[sozluk_df["Kategori"]=="Aksesuar"][["Ürün"]]


# In[24]:


sozluk_df[(sozluk_df["Kategori"]=="Giyim") & (sozluk_df["Fiyat"]>300)]


# In[25]:


sozluk_df[(sozluk_df["Kategori"]=="Ayakkabı") & (sozluk_df["Fiyat"]<600)]


# In[26]:


sozluk_df[(sozluk_df["Kategori"]=="Aksesuar") & (sozluk_df["Fiyat"]>100)]


# In[ ]:




