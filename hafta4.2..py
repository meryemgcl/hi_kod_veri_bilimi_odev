#!/usr/bin/env python
# coding: utf-8

# In[15]:


def yas_hesapla(dogum_yili):
    yas = 2024 - dogum_yili    
    return yas    
print(yas_hesapla(2004))


# In[22]:


def dairenin_alani():    
    pi = input("pi sayısını giriniz: ")    
    yari_cap = input("yarıçap değerinini giriniz: ")    
    d_alan = float(pi) * (float(yari_cap)**2)    
    return(round(d_alan))    
dairenin_alani()


# In[32]:


def faktoriyel(parametre):    
    factorial = 1    
    k = parametre
    while k > 0:    
        factorial = factorial * k    
        k = k - 1    
        return(str(parametre) + "sayısının faktoriyeli {} sayısıdır.".format(str(factorial)))    
faktoriyel(4)    


# In[45]:


def yas_hesaplama(dogum_yili):
    from datetime import datetime
    mevcut_yil = datetime.now().year
    return mevcut_yil - dogum_yili

def emeklilik(dogum_yili, isim):    
    yas = yas_hesaplama(dogum_yili)    
    if yas >= 65:    
        print("Emekli oldunuz.")    
    else:    
        kalan_yil = 65 - yas     
        print(f"{isim}, emeklilik için {kalan_yil} yılın kaldı.")  

emeklilik(1991, "Meryem")


#    

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




