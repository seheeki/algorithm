
# coding: utf-8

# In[18]:


year = int(input());


# In[19]:


if ((year%4==0 and year%100!=0) or (year%400==0)):
    print(1);
else:
    print(0);

